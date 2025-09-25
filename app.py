#!/usr/bin/env python3
import argparse
import os
import sys
import subprocess
import tempfile
import json
from datetime import datetime, UTC


# ---------------------------
# Clone repo if a GitHub URL is passed
# ---------------------------
def clone_if_url(src: str):
    looks_like_url = src.startswith(("http://", "https://")) or src.endswith(".git")
    if not looks_like_url:
        return os.path.abspath(src), False
    tmpdir = tempfile.mkdtemp(prefix="repo_")
    try:
        subprocess.run(
            ["git", "clone", "--depth", "1", src, tmpdir],
            check=True,
            capture_output=True,
        )
        return tmpdir, True
    except subprocess.CalledProcessError as e:
        sys.stderr.write(
            "Error cloning repository:\n" + e.stderr.decode("utf-8", errors="ignore")
        )
        sys.exit(1)


# ---------------------------
# Simple detectors for packaging + deps + tests
# ---------------------------
def detect_packaging(root: str):
    return {
        "has_pyproject_toml": os.path.exists(os.path.join(root, "pyproject.toml")),
        "has_setup_py": os.path.exists(os.path.join(root, "setup.py")),
        "has_setup_cfg": os.path.exists(os.path.join(root, "setup.cfg")),
    }


def detect_dependencies(root: str):
    candidates = [
        "requirements.txt",
        "requirements-dev.txt",
        "Pipfile",
        "Pipfile.lock",
        "poetry.lock",
        "pyproject.toml",
        "uv.lock",
    ]
    found = [f for f in candidates if os.path.exists(os.path.join(root, f))]
    return {"dependency_files": found}


def detect_tests(root: str):
    test_dirs = [
        name for name in ("tests", "test") if os.path.isdir(os.path.join(root, name))
    ]
    has_pytest_cfg = any(
        os.path.exists(os.path.join(root, f)) for f in ("pytest.ini", "tox.ini")
    )
    try:
        if os.path.exists(os.path.join(root, "pyproject.toml")):
            with open(os.path.join(root, "pyproject.toml"), encoding="utf-8") as f:
                content = f.read()
            if "[tool.pytest.ini_options]" in content or "[tool.pytest]" in content:
                has_pytest_cfg = True
    except Exception:
        pass
    return {"test_dirs": test_dirs, "has_pytest_cfg": has_pytest_cfg}


# ---------------------------
# Step-2B: Run repo tests (pytest → unittest)
# ---------------------------
def run_tests(repo_path: str):
    result = {"framework": None, "exit_code": None, "output": ""}
    try:
        completed = subprocess.run(
            ["pytest", "-q", "--maxfail=1"],
            cwd=repo_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        result["framework"] = "pytest"
        result["exit_code"] = completed.returncode
        result["output"] = completed.stdout.strip() or "No pytest output."
        return result
    except FileNotFoundError:
        try:
            completed = subprocess.run(
                [sys.executable, "-m", "unittest", "discover"],
                cwd=repo_path,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
            )
            result["framework"] = "unittest"
            result["exit_code"] = completed.returncode
            if "Ran 0 tests" in completed.stdout:
                result["output"] = (
                    "No tests discovered. Repo may require extra dependencies."
                )
            else:
                result["output"] = completed.stdout.strip()
            return result
        except Exception as e:
            result["framework"] = "none"
            result["output"] = f"Could not run tests: {e}"
            return result


# ---------------------------
# Step-3: Ruff integration
# ---------------------------
def run_ruff(repo_path: str, apply: bool = False):
    result = {"available": False, "applied": False, "output": ""}
    try:
        subprocess.run(
            ["ruff", "--version"],
            check=True,
            capture_output=True,
        )
        if apply:
            completed = subprocess.run(
                ["ruff", "check", "--fix", "."],
                cwd=repo_path,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
            )
            result["applied"] = True
            result["output"] = completed.stdout.strip() or "✅ Applied Ruff fixes."
        else:
            completed = subprocess.run(
                ["ruff", "check", "."],
                cwd=repo_path,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
            )
            result["output"] = completed.stdout.strip() or "No lint issues found."
        result["available"] = True
    except FileNotFoundError:
        result["output"] = "ruff not installed."
    return result


# ---------------------------
# Step-3: Pyupgrade integration
# ---------------------------
def run_pyupgrade(repo_path: str, apply: bool = False, check: bool = False):
    result = {"available": False, "applied": False, "output": ""}
    try:
        subprocess.run(["pyupgrade"], capture_output=True)
        result["available"] = True

        pyfiles = _collect_py_files(repo_path)

        if check:
            subprocess.run(
                ["git", "init"],
                cwd=repo_path,
                capture_output=True,
            )
            subprocess.run(
                ["git", "add", "."],
                cwd=repo_path,
                capture_output=True,
            )
            subprocess.run(
                ["git", "commit", "-m", "baseline"],
                cwd=repo_path,
                capture_output=True,
            )

            subprocess.run(
                ["pyupgrade", "--py311-plus"] + pyfiles,
                cwd=repo_path,
                capture_output=True,
            )

            diff = subprocess.run(
                ["git", "diff"],
                cwd=repo_path,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
            )
            result["output"] = diff.stdout.strip() or "No changes suggested."
            return result

        if apply:
            completed = subprocess.run(
                ["pyupgrade", "--py311-plus"] + pyfiles,
                cwd=repo_path,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
            )
            result["applied"] = True
            result["output"] = (
                completed.stdout.strip() or "✅ Applied pyupgrade changes."
            )
        else:
            result["output"] = (
                "pyupgrade available but not applied (use --check-fixes or --apply-fixes)."
            )
    except FileNotFoundError:
        result["output"] = "pyupgrade not installed."
    return result


def _collect_py_files(root: str):
    pyfiles = []
    for dirpath, _, filenames in os.walk(root):
        for f in filenames:
            if f.endswith(".py"):
                pyfiles.append(os.path.join(dirpath, f))
    return pyfiles


# ---------------------------
# Step-4: Security Audit (pip-audit)
# ---------------------------
def run_pip_audit(repo_path: str):
    result = {"available": False, "vulnerabilities": [], "output": ""}
    try:
        subprocess.run(
            ["pip-audit", "--version"],
            check=True,
            capture_output=True,
        )
        result["available"] = True

        req_path = os.path.join(repo_path, "requirements.txt")
        if not os.path.exists(req_path):
            result["output"] = "No requirements.txt found, skipping pip-audit."
            return result

        completed = subprocess.run(
            ["pip-audit", "-r", "requirements.txt"],
            cwd=repo_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        output = completed.stdout.strip()
        result["output"] = output

        if "No known vulnerabilities found" in output:
            result["vulnerabilities"] = []
        else:
            result["vulnerabilities"] = output.splitlines()

    except FileNotFoundError:
        result["output"] = "pip-audit not installed."
    except Exception as e:
        result["output"] = f"pip-audit error: {e}"
    return result


def _yn(flag: bool) -> str:
    return "Yes ✅" if flag else "No ❌"


# ---------------------------
# Step-5: Black integration
# ---------------------------
def run_black(repo_path: str, apply: bool = False):
    result = {"available": False, "applied": False, "output": ""}
    try:
        subprocess.run(
            ["black", "--version"],
            check=True,
            capture_output=True,
        )
        result["available"] = True

        if apply:
            completed = subprocess.run(
                ["black", "."],
                cwd=repo_path,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
            )
            result["applied"] = True
            result["output"] = (
                completed.stdout.strip() or "✅ Applied Black formatting."
            )
        else:
            completed = subprocess.run(
                ["black", "--check", "."],
                cwd=repo_path,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
            )
            if completed.returncode == 0:
                result["output"] = "✅ Code is properly formatted."
            else:
                result["output"] = (
                    completed.stdout.strip() or "❌ Code needs reformatting."
                )
    except FileNotFoundError:
        result["output"] = "black not installed."
    return result


# ---------------------------
# Write Markdown Report
# ---------------------------
def write_markdown_report(summary: dict, md_path: str):
    lines = []
    lines.append("# Python Project Audit Report")
    lines.append("")
    lines.append(f"- **Generated:** {datetime.now(UTC).isoformat(timespec='seconds')}")
    lines.append(f"- **Repo Path:** `{summary.get('repo_path','')}`")
    lines.append("")

    pkg = summary.get("packaging", {})
    dep = summary.get("dependencies", {})
    tst = summary.get("tests", {})
    testrun = summary.get("test_run", {})
    ruffrun = summary.get("ruff", {})
    blackrun = summary.get("black", {})
    pyup = summary.get("pyupgrade", {})
    sec = summary.get("security", {})

    lines.append("## Packaging")
    lines.append(f"- `pyproject.toml`: {_yn(pkg.get('has_pyproject_toml', False))}")
    lines.append(f"- `setup.py`: {_yn(pkg.get('has_setup_py', False))}")
    lines.append(f"- `setup.cfg`: {_yn(pkg.get('has_setup_cfg', False))}")
    lines.append("")

    lines.append("## Dependencies")
    files = dep.get("dependency_files", [])
    if files:
        lines.append("- Found dependency files:")
        for f in files:
            lines.append(f"  - `{f}`")
    else:
        lines.append("- No dependency files detected.")
    lines.append("")

    lines.append("## Tests")
    test_dirs = tst.get("test_dirs", [])
    if test_dirs:
        lines.append("- Test directories:")
        for d in test_dirs:
            lines.append(f"  - `{d}`")
    else:
        lines.append("- No `tests/` or `test/` directory found.")
    lines.append(f"- Pytest config present: {_yn(tst.get('has_pytest_cfg', False))}")
    lines.append("")

    lines.append("## Test Run Results")
    if testrun.get("framework"):
        lines.append(f"- Framework: {testrun['framework']}")
        lines.append(f"- Exit Code: {testrun['exit_code']}")
        lines.append("```")
        lines.append(testrun.get("output", ""))
        lines.append("```")
    else:
        lines.append("- Test run skipped.")
    lines.append("")

    lines.append("## Ruff Linting")
    lines.append("```")
    lines.append(ruffrun.get("output", ""))
    lines.append("```")
    lines.append("")

    lines.append("## Code Formatting (Black)")
    lines.append("```")
    lines.append(blackrun.get("output", ""))
    lines.append("```")
    lines.append("")

    lines.append("## Pyupgrade")
    lines.append("```")
    lines.append(pyup.get("output", ""))
    lines.append("```")
    lines.append("")

    lines.append("## Security Audit")
    if sec.get("available"):
        if sec.get("vulnerabilities"):
            lines.append("Known vulnerabilities:")
            lines.append("```")
            lines.extend(sec.get("vulnerabilities", []))
            lines.append("```")
        else:
            lines.append("- ✅ No known vulnerabilities found.")
    else:
        lines.append(f"- {sec.get('output','pip-audit not installed.')}")
    lines.append("")

    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


# ---------------------------
# Main CLI
# ---------------------------
def main():
    ap = argparse.ArgumentParser(
        description="Step-5: Auditor with Ruff + Black + Pyupgrade + Security Audit."
    )
    ap.add_argument("source", help="Local path OR GitHub URL (https://... or ... .git)")
    ap.add_argument(
        "--report", default="audit_report.json", help="Path to write the audit JSON"
    )
    ap.add_argument(
        "--md-report",
        default="audit_report.md",
        help="Path to write the Markdown report",
    )
    ap.add_argument("--skip-tests", action="store_true", help="Skip running tests")
    ap.add_argument(
        "--apply-format",
        action="store_true",
        help="Apply Black and Ruff formatting fixes",
    )

    group = ap.add_mutually_exclusive_group()
    group.add_argument(
        "--check-fixes",
        action="store_true",
        help="Preview pyupgrade changes without applying",
    )
    group.add_argument(
        "--apply-fixes", action="store_true", help="Apply pyupgrade fixes directly"
    )

    args = ap.parse_args()
    repo_path, is_temp = clone_if_url(args.source)

    summary = {
        "repo_path": repo_path,
        "packaging": detect_packaging(repo_path),
        "dependencies": detect_dependencies(repo_path),
        "tests": detect_tests(repo_path),
    }

    if not args.skip_tests:
        summary["test_run"] = run_tests(repo_path)
    else:
        summary["test_run"] = {"framework": None, "output": "Test run skipped."}

    summary["ruff"] = run_ruff(repo_path, apply=args.apply_format)
    summary["black"] = run_black(repo_path, apply=args.apply_format)
    summary["pyupgrade"] = run_pyupgrade(
        repo_path, apply=args.apply_fixes, check=args.check_fixes
    )
    summary["security"] = run_pip_audit(repo_path)

    with open(args.report, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    write_markdown_report(summary, args.md_report)

    print("✅ Audit complete.")
    print(f"- Wrote JSON: {args.report}")
    print(f"- Wrote Markdown: {args.md_report}")
    if is_temp:
        print(f"(Temporary clone at: {repo_path})")


if __name__ == "__main__":
    main()
