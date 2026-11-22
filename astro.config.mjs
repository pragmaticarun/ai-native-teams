// @ts-check
import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";
import starlightLinksValidator from "starlight-links-validator";

const mod = (label, directory) => ({ label, collapsed: true, items: [{ autogenerate: { directory } }] });

export default defineConfig({
  site: "https://pragmaticarun.github.io",
  base: "/ai-native-teams",
  integrations: [
    starlight({
      title: "AI-Native Teams",
      description:
        "A comprehensive, hands-on course that takes whole teams from AI-curious to AI-native: concepts, tools, workflows, safety, governance and change management.",
      social: [{ icon: "github", label: "GitHub", href: "https://github.com/pragmaticarun/ai-native-teams" }],
      editLink: { baseUrl: "https://github.com/pragmaticarun/ai-native-teams/edit/main/" },
      lastUpdated: true,
      customCss: ["./src/styles/custom.css"],
      plugins: [starlightLinksValidator()],
      sidebar: [
        { label: "Start here", items: [{ autogenerate: { directory: "start" } }] },
        {
          label: "Part 1 · Understand",
          items: [
            mod("1 · How modern AI works", "m01-foundations"),
            mod("2 · Prompting that works", "m02-prompting"),
            mod("3 · Context engineering", "m03-context"),
          ],
        },
        {
          label: "Part 2 · Build",
          items: [
            mod("4 · RAG & knowledge", "m04-rag"),
            mod("5 · Tools, agents & MCP", "m05-agents"),
            mod("6 · AI-assisted engineering", "m06-coding"),
            mod("7 · AI workflows for every role", "m07-workflows"),
          ],
        },
        {
          label: "Part 3 · Trust",
          items: [
            mod("8 · Evals & observability", "m08-evals"),
            mod("9 · Safety & security", "m09-safety"),
            mod("10 · Governance & compliance", "m10-governance"),
          ],
        },
        {
          label: "Part 4 · Transform",
          items: [
            mod("11 · Operating model & change", "m11-change"),
            mod("12 · Measuring value", "m12-value"),
            mod("13 · Capstone: your 90-day plan", "m13-capstone"),
          ],
        },
        { label: "Reference", items: [{ autogenerate: { directory: "reference" } }] },
      ],
    }),
  ],
});
