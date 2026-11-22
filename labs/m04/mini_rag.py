"""A tiny, dependency-free retrieval demo for Lab 4.

It shows the retrieval half of RAG (chunk -> index -> search -> build a grounded prompt)
with BM25 keyword scoring, so it runs offline with no API key. Swap `search()` for an
embedding or hybrid search and send `build_prompt()`'s output to any approved model.

Usage:
    python mini_rag.py docs/ "How many days of parental leave do we offer?"
"""

from __future__ import annotations

import math
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

WORD = re.compile(r"[a-z0-9]+")
STOP = {"the", "a", "an", "of", "to", "and", "or", "in", "on", "for", "is", "are", "do", "we", "our", "how", "what", "many", "does", "with"}


def tokens(text: str) -> list[str]:
    return [t for t in WORD.findall(text.lower()) if t not in STOP]


@dataclass
class Chunk:
    source: str
    heading: str
    text: str


def chunk_markdown(path: Path) -> list[Chunk]:
    """Split a Markdown file on headings so each chunk is one self-contained section."""
    chunks: list[Chunk] = []
    heading, lines = path.stem, []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("#"):
            if "".join(lines).strip():
                chunks.append(Chunk(path.name, heading, "\n".join(lines).strip()))
            heading, lines = line.lstrip("# ").strip(), []
        else:
            lines.append(line)
    if "".join(lines).strip():
        chunks.append(Chunk(path.name, heading, "\n".join(lines).strip()))
    return chunks


class BM25:
    def __init__(self, chunks: list[Chunk], k1: float = 1.5, b: float = 0.75) -> None:
        self.chunks, self.k1, self.b = chunks, k1, b
        # The heading is part of the indexed text: it often carries the key term.
        self.docs = [Counter(tokens(c.heading + " " + c.text)) for c in chunks]
        self.lengths = [sum(d.values()) for d in self.docs]
        self.avg = sum(self.lengths) / max(len(self.docs), 1)
        df = Counter(term for d in self.docs for term in d)
        n = len(self.docs)
        self.idf = {t: math.log(1 + (n - f + 0.5) / (f + 0.5)) for t, f in df.items()}

    def search(self, query: str, k: int = 3) -> list[tuple[float, Chunk]]:
        scored = []
        for doc, length, chunk in zip(self.docs, self.lengths, self.chunks):
            s = 0.0
            for term in tokens(query):
                tf = doc.get(term, 0)
                if tf:
                    s += self.idf[term] * tf * (self.k1 + 1) / (tf + self.k1 * (1 - self.b + self.b * length / self.avg))
            if s > 0:
                scored.append((s, chunk))
        return sorted(scored, key=lambda x: x[0], reverse=True)[:k]


def build_prompt(question: str, hits: list[tuple[float, Chunk]]) -> str:
    sources = "\n\n".join(
        f'<source id="{i + 1}" file="{c.source}" section="{c.heading}">\n{c.text}\n</source>'
        for i, (_, c) in enumerate(hits)
    )
    return (
        "Answer the question using only the sources below. Cite sources like [1]. "
        "If the sources don't contain the answer, say you don't know.\n\n"
        f"{sources}\n\nQuestion: {question}"
    )


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(__doc__)
        return 2
    folder, question = Path(argv[1]), argv[2]
    chunks = [c for p in sorted(folder.glob("*.md")) for c in chunk_markdown(p)]
    hits = BM25(chunks).search(question)
    if not hits:
        print("No matching chunks: the honest answer is 'I don't know'.")
        return 0
    for score, c in hits:
        print(f"{score:5.2f}  {c.source} › {c.heading}")
    print("\n--- prompt to send to your model ---\n")
    print(build_prompt(question, hits))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
