import pandas as pd
import matplotlib.pyplot as plt


# Load the scraped jobs data
df = pd.read_csv("data/jobs.csv")


# ============================================================
# BASIC DATA VALIDATION
# ============================================================

print("Total rows:", len(df))
print("Total columns:", len(df.columns))


print("\nColumns:")
print(df.columns.tolist())


print("\nMissing values:")
print(df.isnull().sum())


print("\nDuplicate rows:", df.duplicated().sum())


# ============================================================
# JOB ANALYSIS
# ============================================================

print("\nTop 10 job titles:")
print(
    df["title"]
    .value_counts()
    .head(10)
)


print("\nTop 10 companies:")
print(
    df["company"]
    .value_counts()
    .head(10)
)


print("\nTop 10 locations:")
print(
    df["location"]
    .value_counts()
    .head(10)
)


# ============================================================
# PYTHON JOB ANALYSIS
# ============================================================

print("\nPython-related jobs:")


python_jobs = df[
    df["title"].str.contains(
        "Python",
        case=False,
        na=False
    )
]


print(
    "Number of Python-related jobs:",
    len(python_jobs)
)


print("\nPython-related job titles:")

print(
    python_jobs["title"]
    .value_counts()
)


python_percentage = (
    len(python_jobs) / len(df)
) * 100


print(
    "\nPercentage of Python-related jobs:",
    python_percentage,
    "%"
)


# ============================================================
# POSTED DATE ANALYSIS
# ============================================================

df["posted_date"] = pd.to_datetime(
    df["posted_date"]
)


print("\nJobs by posted date:")

print(
    df["posted_date"]
    .value_counts()
    .sort_index()
)


# ============================================================
# TECHNOLOGY / SKILL ANALYSIS
# ============================================================

print("\nTechnology mentions:")


skills = [
    "Python",
    "Django",
    "Flask",
    "Java",
    "JavaScript",
    "HTML",
    "CSS",
    "SQL",
    "AWS",
    "Git"
]


for skill in skills:

    count = df["description"].str.contains(
        skill,
        case=False,
        na=False
    ).sum()

    print(
        f"{skill}: {count}"
    )


# ============================================================
# CHART 1: TOP JOB TITLES
# ============================================================

top_titles = (
    df["title"]
    .value_counts()
    .head(10)
)


plt.figure(figsize=(10, 6))

top_titles.plot(
    kind="bar"
)

plt.title(
    "Top 10 Job Titles"
)

plt.xlabel(
    "Job Title"
)

plt.ylabel(
    "Number of Jobs"
)

plt.xticks(
    rotation=45,
    ha="right"
)

plt.tight_layout()

plt.show()


# ============================================================
# CHART 2: PYTHON VS NON-PYTHON JOBS
# ============================================================

python_count = df["title"].str.contains(
    "Python",
    case=False,
    na=False
).sum()


non_python_count = (
    len(df) - python_count
)


labels = [
    "Python Jobs",
    "Non-Python Jobs"
]


values = [
    python_count,
    non_python_count
]


plt.figure(figsize=(7, 5))

plt.bar(
    labels,
    values
)

plt.title(
    "Python vs Non-Python Jobs"
)

plt.xlabel(
    "Job Type"
)

plt.ylabel(
    "Number of Jobs"
)

plt.tight_layout()

plt.show()


# ============================================================
# CHART 3: TOP LOCATIONS
# ============================================================

top_locations = (
    df["location"]
    .value_counts()
    .head(10)
)


plt.figure(figsize=(10, 6))

top_locations.plot(
    kind="bar"
)

plt.title(
    "Top 10 Job Locations"
)

plt.xlabel(
    "Location"
)

plt.ylabel(
    "Number of Jobs"
)

plt.xticks(
    rotation=45,
    ha="right"
)

plt.tight_layout()

plt.show()


# ============================================================
# CHART 4: JOBS BY POSTED DATE
# ============================================================

jobs_by_date = (
    df["posted_date"]
    .value_counts()
    .sort_index()
)


plt.figure(figsize=(10, 6))

jobs_by_date.plot(
    kind="line",
    marker="o"
)

plt.title(
    "Jobs by Posted Date"
)

plt.xlabel(
    "Posted Date"
)

plt.ylabel(
    "Number of Jobs"
)

plt.xticks(
    rotation=45
)

plt.tight_layout()

plt.show()


# ============================================================
# CHART 5: TOP COMPANIES
# ============================================================

top_companies = (
    df["company"]
    .value_counts()
    .head(10)
)


plt.figure(figsize=(10, 6))

top_companies.plot(
    kind="bar"
)

plt.title(
    "Top 10 Companies by Number of Jobs"
)

plt.xlabel(
    "Company"
)

plt.ylabel(
    "Number of Jobs"
)

plt.xticks(
    rotation=45,
    ha="right"
)

plt.tight_layout()

plt.show()


# ============================================================
# SAVE ANALYSIS SUMMARY
# ============================================================

summary = {

    "total_jobs": len(df),

    "total_companies":
        df["company"].nunique(),

    "total_locations":
        df["location"].nunique(),

    "python_jobs":
        python_count,

    "python_job_percentage":
        (python_count / len(df)) * 100

}


summary_df = pd.DataFrame(
    [summary]
)


summary_df.to_csv(
    "data/analysis_summary.csv",
    index=False
)


print(
    "\nAnalysis summary saved to "
    "data/analysis_summary.csv"
)