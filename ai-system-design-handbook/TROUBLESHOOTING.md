# Setup and lab troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `python` is not recognized | Python launcher/path differs | Try `py --version` on Windows or `python3 --version` on macOS/Linux; install Python from its official source if absent |
| `No module named labs` | Terminal is outside the handbook folder | Run `cd ai-system-design-handbook` from the parent FDE repository, or enter the folder containing `labs/` and this README |
| Syntax/import error on old Python | Unsupported interpreter | Use Python 3.11 or newer and verify the interpreter used by your editor |
| Retrieval abstains for a paraphrase | The lab uses lexical overlap | Treat this as a measured limitation; add development cases and compare retrieval approaches |
| Payroll query abstains | Support group lacks access | This is expected; use synthetic `--groups finance` only to explore the allowed path |
| `duplicate` on first visible invoice attempt | Persistent demo database already contains the operation | Inspect the prior record or run with the default fresh in-memory database |
| Changed payload produces `ConflictError` | An existing operation key refers to a different payload | This is intentional; create a new legitimate operation/version under a defined business policy |
| Capacity output seems too cheap | Base model costs exclude other work | Include retries, retrieval, hosting, tools, review, and actual provider billing rules |
| Gateway uses fallback for every demo request | The deterministic primary errors open its breaker | Expected demo behavior; inspect tests for primary success and recovery |
| Test behavior differs after edits | You may have changed a protected boundary | Read the assertion and trace the behavior; do not remove the test just to make output green |

## Investigating a failed experiment

Write the command, interpreter version, expected behavior, actual safe output, and recent change. Reduce to one example. Identify the stage that first diverges from expectation, then fix or document that stage. Avoid publishing private paths, credentials, client data, or full sensitive logs in an issue.

For conceptual failures, use [the revision sheet](CHEATSHEET.md). For contributions, see [CONTRIBUTING.md](CONTRIBUTING.md).
