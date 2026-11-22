from pathlib import Path

from mini_rag import BM25, build_prompt, chunk_markdown

DOCS = Path(__file__).parent / "docs"
CHUNKS = [c for p in sorted(DOCS.glob("*.md")) for c in chunk_markdown(p)]


def test_chunks_follow_headings():
    headings = [c.heading for c in CHUNKS]
    assert "Parental leave" in headings and "AI tools" in headings
    assert all(c.text for c in CHUNKS)


def test_top_hit_is_the_right_section():
    top = BM25(CHUNKS).search("How many weeks of parental leave?")[0][1]
    assert top.heading == "Parental leave"
    top = BM25(CHUNKS).search("Can I paste customer data into an AI tool?")[0][1]
    assert top.heading == "AI tools"


def test_unrelated_question_finds_nothing():
    assert BM25(CHUNKS).search("quarterly revenue forecast") == []


def test_prompt_is_grounded_and_cited():
    hits = BM25(CHUNKS).search("annual leave carry over")
    prompt = build_prompt("Can I carry over leave?", hits)
    assert '<source id="1"' in prompt and "say you don't know" in prompt
