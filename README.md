[![CI/CD](https://github.com/Licheng1004/Spark-Flight-Delay-Pipeline/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/Licheng1004/Spark-Flight-Delay-Pipeline/actions/workflows/ci.yml)

# Spark Flight-Delay Data Preparation

A PySpark DataFrame pipeline that cleans flight and weather records, joins weather observations around departure and arrival times, and builds a monthly flight-level joint table. The final workflow also includes the report's simple downstream Spark ML baseline.

## Pipeline

1. `notebooks/project_clean.ipynb` cleans flight and weather inputs and writes partitioned Parquet data under `data/clean/`.
2. `notebooks/project_join_test.ipynb` joins weather observations for the configured flight months and writes the joint table under `data/jt/`. The checked-in settings cover the months documented in the report.
3. `notebooks/JOIN_TOTAL_ML.ipynb` trains and evaluates the simple downstream delay classifier on the generated joint-table partitions.
4. `notebooks/figures.ipynb` regenerates the final report figures into the ignored `outputs/report_figures/` directory.

The report notes that only selected months were demonstrated and that wide weather matching and output materialization are the main runtime costs. The baseline model is a pipeline check; it is not presented as a reproduction of the reference paper.

## Data download and layout

Raw course data are not included. Download the original dataset bundle from the [Dropbox share referenced by the course project brief](https://www.dropbox.com/sh/iasq7frk6f58ptq/AAAzSmk6cusSNfqYNYsnLGIXa), subject to its access and use terms. The shared bundle includes the flight and weather CSV/TXT files used by the project. Arrange them as follows:

```text
data/raw/
├── wban_airport_timezone.csv
├── Flights/
│   ├── 201201.csv
│   └── ...
└── Weather/
    ├── 201201hourly.txt
    └── ...
```

The notebooks expect the original headers and monthly filenames. Do not add downloaded data or generated Parquet outputs to Git; `data/` is ignored.

## Requirements and run

Install a Spark-compatible Java runtime, then:

```bash
python -m pip install -r requirements.txt
jupyter lab
```

Start Jupyter from the repository root. Run the three notebooks in pipeline order. The join notebook builds only the report's selected months unless `RUN_YEAR` and `RUN_MONTHS` are changed.

## Report

- [Final report (Markdown)](report/final_report.md)
- [Final report (PDF)](report/final_report.pdf)

## CI/CD

The GitHub Actions workflow runs on pushes to `main`, pull requests, and manual dispatch. It validates all project notebooks and starts local Spark for a tiny DataFrame smoke check; it does not need the course data bundle. On a `v*` tag, it also publishes a GitHub Release with the source snapshot and the final report deliverables.
