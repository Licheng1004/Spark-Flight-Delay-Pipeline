# Reproducibility record

Reviewed on **2026-10-14** in a separate Windows x86-64 working copy with **CPython 3.12.14 / uv 0.12.17**. This is a fresh environment check on the review machine, not a claim that every OS and hardware combination has been exercised.

## Environment

The repository has a committed `pyproject.toml`, `.python-version` and `uv.lock`. Direct and transitive dependencies are locked. The public quick start uses `uv sync --locked`; caches, environments and generated `.reproduction/` outputs are ignored by Git. First sync requires package-index access.


The local execution sandbox blocked Windows source-archive canonicalization. A wheel was built from the official PyPI 3.5.9 source (SHA-256 `ea27adc39ddac9413b8951e45aa748cbed6c785971b81386efc41938f6243d93`) and installed at the locked version. A subsequent ordinary `uv sync --locked` succeeded. This helper wheel is not a repository dependency or an uploaded artifact; other machines install from the committed PyPI lock.


## Checks actually performed

Four notebooks validated. PySpark 3.5.9 with Temurin Java 17 started locally and the synthetic DataFrame operation passed.

| Command | Local result |
| --- | --- |
| `uv run --locked python scripts/verify.py` | Passed |
| `uv run --locked python scripts/ci_smoke.py` | Passed |

## Scope and prerequisites

The course flight/weather inputs are external, so the complete cleaning/join/model pipeline was not rerun. Windows emitted Hadoop-native/winutils warnings; Linux/WSL2 remains the reference for full Parquet execution.

The current CI workflow runs the documented locked checks on its configured platform(s). The workflow file itself is not evidence that a remote run passed; use the linked GitHub Actions run for that result. Numerical floating-point differences and external Java/model/data prerequisites are not solved by a Python lock alone.

Notebook changes preserve prior saved outputs. Schema checks compile code without executing all analysis cells. Archived metrics are labeled as historical in the README unless checked directly here.
