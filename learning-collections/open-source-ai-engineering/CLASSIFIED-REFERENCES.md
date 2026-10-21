# Separately classified references

These entries are excluded from the main active open-source list. Their exact component, license, or maintenance status matters.

## Archived Reference

| Project | What to use it for | First exercise | License/scope |
|---|---|---|---|
| [FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise) | Inspect an archived visual-workflow project as a historical reference. | Create a small review interface with explicit unknown and error states. | Archived at verification; not recommended as an active starting point. |

## License Review Needed

| Project | What to use it for | First exercise | License/scope |
|---|---|---|---|
| [microsoft/autogen](https://github.com/microsoft/autogen) | Study agent patterns after resolving component-level license scope. | Build a bounded synthetic task and deliberately trigger one failed tool call. | Repository-level LICENSE is CC-BY-4.0; software component licenses need separate review. |

## Open Source Core

| Project | What to use it for | First exercise | License/scope |
|---|---|---|---|
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | Study provider routing in the MIT core and its integration boundaries. | Simulate a timeout and verify the fallback stays inside the original time/data policy. | MIT outside enterprise/; enterprise/ has separate terms. |
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | Inspect model traces and evaluation workflows in the MIT core. | Trace a synthetic request without logging its full payload; locate a deliberately slow stage. | MIT outside ee/, web/src/ee/, worker/src/ee/; excluded directories have separate terms. |
| [weaviate/weaviate](https://github.com/weaviate/weaviate) | Study search features in the documented open-source core. | Compare exact-ID and paraphrase queries while preserving a tenant filter. | BSD-3-Clause outside wl/; wl/ requires a separate enterprise license. |

## Source Available

| Project | What to use it for | First exercise | License/scope |
|---|---|---|---|
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | Study AI tracing under the repository's source-available terms. | Trace a synthetic request without logging its full payload; locate a deliberately slow stage. | Elastic License 2.0 reviewed; kept outside the open-source main list. |
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | Study workflow orchestration under Sustainable Use and enterprise terms. | Read the current license and identify which proposed uses need further review. | Sustainable Use License plus enterprise exceptions; kept outside the open-source main list. |
| [open-webui/open-webui](https://github.com/open-webui/open-webui) | Inspect a model interface under its custom license conditions. | Read the current license and identify which proposed uses need further review. | Custom Open WebUI License includes branding conditions; kept outside the open-source main list. |

Back: [catalog](README.md).
