// Checks every quiz file: ids unique, answers in range, single vs multi answer shapes.
import { readdirSync, readFileSync } from "node:fs";
import { parse } from "yaml";

const dir = new URL("../src/quizzes/", import.meta.url);
let errors = 0;
const fail = (f, m) => { console.error(`${f}: ${m}`); errors++; };
for (const f of readdirSync(dir).filter((n) => n.endsWith(".yaml"))) {
  const q = parse(readFileSync(new URL(f, dir), "utf8"));
  if (!q.title || !Array.isArray(q.questions) || q.questions.length < 5) fail(f, "needs a title and at least 5 questions");
  const ids = new Set();
  for (const item of q.questions ?? []) {
    if (ids.has(item.id)) fail(f, `duplicate id ${item.id}`);
    ids.add(item.id);
    const n = item.choices?.length ?? 0;
    if (n < 2) fail(f, `${item.id}: needs choices`);
    if (!item.explanation) fail(f, `${item.id}: needs an explanation`);
    const answers = item.type === "multi" ? item.answer : [item.answer];
    if (item.type === "multi" && !Array.isArray(item.answer)) fail(f, `${item.id}: multi needs an array answer`);
    if (item.type === "single" && !Number.isInteger(item.answer)) fail(f, `${item.id}: single needs an integer answer`);
    for (const a of answers ?? []) if (!(a >= 0 && a < n)) fail(f, `${item.id}: answer ${a} out of range`);
  }
  console.log(`${f}: ${q.questions?.length ?? 0} questions`);
}
if (errors) { console.error(`${errors} problem(s)`); process.exit(1); }
