from collections import defaultdict
from typing import Any, Dict, List

def summarize(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    total_cases = len(results)
    total_trials = sum(r.get("trials", 1) for r in results)
    total_passes = sum(r.get("pass_count", 1 if r.get("passed") else 0) for r in results)

    pass_rate = (total_passes / total_trials) if total_trials else 0.0

    by_cat = defaultdict(lambda: {"cases": 0, "trials": 0, "passes": 0, "pass_rate": 0.0})
    cases_not_perfect_by_severity = defaultdict(int)
    flaky_cases = 0

    for r in results:
        cat = r["category"]
        trials = r.get("trials", 1)
        passes = r.get("pass_count", 1 if r.get("passed") else 0)

        by_cat[cat]["cases"] += 1
        by_cat[cat]["trials"] += trials
        by_cat[cat]["passes"] += passes

        if r.get("flaky"):
            flaky_cases += 1

        if r.get("pass_rate", 1.0) < 1.0:
            cases_not_perfect_by_severity[str(r["severity"])] += 1

    for cat, v in by_cat.items():
        v["pass_rate"] = round((v["passes"] / v["trials"]) if v["trials"] else 0.0, 3)

    return {
        "total_cases": total_cases,
        "total_trials": total_trials,
        "total_passes": total_passes,
        "overall_pass_rate": round(pass_rate, 3),
        "flaky_cases": flaky_cases,
        "by_category": dict(by_cat),
        "cases_not_perfect_by_severity": dict(cases_not_perfect_by_severity),
    }
