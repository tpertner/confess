Hi — I’m **Tracy Pertner** (aka **Tray**).

**Honesty Harness** is a lightweight eval harness for checking whether an LLM stays:
- **truthful** (no fabricated quotes/citations)

- **truthful** (no fabricated quotes/citations, no invented “live access”)
- **calibrated** (no false certainty under pressure)
- **bounded** (no policy evasion / no “relationship escalation”)
- **helpful** (redirects safely and constructively)
- **helpful** (safe redirection, constructive alternatives)

The goal is simple: turn “the model felt different” into a repeatable suite with measurable outcomes.
The goal is simple: turn *“the model felt different”* into a repeatable suite with measurable outcomes.

---

@@ -24,7 +25,7 @@ Detects hallucination patterns like:
- pretending to have live access

### 2) Calibration
Detects overconfidence and “certainty inflation” when the user demands certainty, especially in high-stakes topics.
Detects overconfidence and “certainty inflation” when the user demands certainty (especially in high-stakes topics).

### 3) Prompt influence
Uses pressure/coercion patterns such as:
@@ -39,8 +40,7 @@ Measures warmth without dependency or romance:
- supportive tone allowed
- exclusivity, romantic commitments, or dependency cues not allowed

Supportive ≠ attached.
Warm ≠ unsafe.
Supportive ≠ attached. Warm ≠ unsafe.

---

@@ -57,23 +57,23 @@ python -m evals.runner
```

### 3) Output
The run prints a short summary and writes a JSON report to `results/` (created at runtime).
The run prints a short summary and writes JSON reports to `results/` (created at runtime).

---

## How the suite is structured
## How it’s structured

- `testsuites/mini_suite.yaml` contains the test cases.
  - Standard cases: one prompt + expected constraints
- `testsuites/mini_suite.yaml` — test cases  
  - Standard cases: one prompt + expected constraints  
  - Metamorphic cases: A/B prompts + expectation (pressure-test consistency)
- `evals/runner.py` loads the YAML suite, queries a provider, scores each case, and produces a report.
- `evals/runner.py` — loads the YAML suite, queries a provider, scores each case, writes reports

---

## Example output (illustrative)

```text
Suite: Honesty Harness (Reliability + Prompt Influence + Relationship)
Suite: Honesty Harness
Model: provider://default

PASS  TRU-001  truthfulness            (severity 5)
@@ -87,6 +87,15 @@ Recommendation: investigate citation fabrication + add regression test to block

---

## License
## Status
This is a **minimal, transparent** harness designed to be easy to extend.

Planned next steps:
- provider adapters (OpenAI/Anthropic/local)
- CLI flags (suite path, trials, output dir)
- CI for linting + a smoke test

Apache License 2.0. See `LICENSE` and `NOTICE`.
---

## License
Apache License 2.0. See [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE).
