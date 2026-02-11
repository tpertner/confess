import json
import os
import time
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

import yaml

from .providers import Provider, MockProvider
from .scorers import score_case, score_metamorphic_pair
from .report import summarize

@dataclass
class Case:
    id: str
    category: str
    severity: int
    prompt: Optional[str] = None
    expected: Optional[Dict[str, Any]] = None
    metamorphic: Optional[Dict[str, Any]] = None
    notes: str = ""

def load_suite(path: str) -> List[Case]:
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    cases: List[Case] = []
    for c in data["cases"]:
        cases.append(Case(
            id=c["id"],
            category=c["category"],
            severity=int(c["severity"]),
            prompt=c.get("prompt"),
            expected=c.get("expected"),
            metamorphic=c.get("metamorphic"),
            notes=c.get("notes", "")
        ))
    return cases

def run_suite(
    suite_path: str,
    provider: Provider,
    trials: int = 5,
    flaky_low: float = 0.2,
    flaky_high: float = 0.8,
) -> Dict[str, Any]:
    cases = load_suite(suite_path)
    results: List[Dict[str, Any]] = []

    for case in cases:
        trial_outputs = []
        trial_passes = []
        trial_reasons = []
        elapsed_list = []

        for _ in range(trials):
            start = time.time()

            if case.metamorphic:
                a_prompt = case.metamorphic["a_prompt"]
                b_prompt = case.metamorphic["b_prompt"]
                out_a = provider.generate(a_prompt)
                out_b = provider.generate(b_prompt)
                score = score_metamorphic_pair(out_a, out_b, case.metamorphic.get("expectation", {}))
                output = {"a": out_a, "b": out_b}
            else:
                out = provider.generate(case.prompt or "")
                score = score_case(out, case.expected or {})
                output = out

            elapsed = time.time() - start
            trial_outputs.append(output)
            trial_passes.append(bool(score.passed))
            trial_reasons.append(score.reasons)
            elapsed_list.append(round(elapsed, 4))

        pass_count = sum(1 for p in trial_passes if p)
        pass_rate = pass_count / trials if trials else 0.0
        flaky = (flaky_low < pass_rate < flaky_high)
        stable_failure = (pass_rate == 0.0)
        stable_pass = (pass_rate == 1.0)

        failed_reasons = [
            {"trial": i, "reasons": trial_reasons[i], "output": trial_outputs[i]}
            for i, p in enumerate(trial_passes)
            if not p
        ]

        results.append({
            "id": case.id,
            "category": case.category,
            "severity": case.severity,
            "trials": trials,
            "pass_count": pass_count,
            "pass_rate": round(pass_rate, 3),
            "reproducibility": round(pass_rate, 3),
            "flaky": flaky,
            "stable_pass": stable_pass,
            "stable_failure": stable_failure,
            "elapsed_s": elapsed_list,
            "notes": case.notes,
            "failed_trials": failed_reasons[:3],
        })

    summary = summarize(results)
    return {"summary": summary, "results": results}

def save_results(payload: Dict[str, Any], out_dir: str = "results") -> str:
    os.makedirs(out_dir, exist_ok=True)
    ts = time.strftime("%Y%m%d-%H%M%S")
    out_path = os.path.join(out_dir, f"run-{ts}.jsonl")

    with open(out_path, "w", encoding="utf-8") as f:
        for r in payload["results"]:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    with open(os.path.join(out_dir, f"summary-{ts}.json"), "w", encoding="utf-8") as f:
        json.dump(payload["summary"], f, indent=2)

    return out_path

if __name__ == "__main__":
    provider = MockProvider()
    payload = run_suite("testsuites/mini_suite.yaml", provider, trials=5)
    path = save_results(payload)
    print("Saved:", path)
    print(json.dumps(payload["summary"], indent=2))
