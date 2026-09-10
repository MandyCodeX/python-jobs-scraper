from pathlib import Path


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent


# Data directory
DATA_DIR = BASE_DIR / "data"


# Jobs CSV file
JOBS_FILE = DATA_DIR / "jobs.csv"


# Analysis summary file
ANALYSIS_FILE = DATA_DIR / "analysis_summary.csv"