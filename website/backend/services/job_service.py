import pandas as pd

from config import JOBS_FILE


def load_jobs():
    """
    Load job data from the CSV file.
    """

    df = pd.read_csv(JOBS_FILE)

    # Give every job a permanent ID
    df["job_id"] = df.index

    return df


def search_jobs(df, search):
    """
    Search jobs by title, company, or location.
    """

    if not search:
        return df

    search = search.strip()

    if not search:
        return df

    return df[
        df["title"].str.contains(
            search,
            case=False,
            na=False
        )
        |
        df["company"].str.contains(
            search,
            case=False,
            na=False
        )
        |
        df["location"].str.contains(
            search,
            case=False,
            na=False
        )
    ]


def filter_python_jobs(df, python_only):
    """
    Filter jobs whose title contains Python.
    """

    if python_only != "on":
        return df

    return df[
        df["title"].str.contains(
            "Python",
            case=False,
            na=False
        )
    ]


def sort_jobs(df, sort):
    """
    Sort jobs according to the selected option.
    """

    if sort == "company":

        return df.sort_values(
            "company"
        )

    if sort == "date":

        return df.sort_values(
            "posted_date"
        )

    return df.sort_values(
        "title"
    )


def get_job_by_id(job_id):
    """
    Return a single job by its ID.
    """

    df = load_jobs()

    job = df[
        df["job_id"] == job_id
    ]

    if job.empty:
        return None

    return job.iloc[0].to_dict()


def get_job_skills(description):
    """
    Extract known technology skills
    mentioned in a job description.
    """

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
        "Git",
        "PostgreSQL",
        "MySQL",
        "Docker",
        "Linux"
    ]

    found_skills = []

    description = str(description)

    for skill in skills:

        if skill.lower() in description.lower():

            found_skills.append(skill)

    return found_skills


def get_job_statistics(df):
    """
    Calculate statistics for the jobs page.
    """

    total_jobs = len(df)

    total_companies = df[
        "company"
    ].nunique()

    total_locations = df[
        "location"
    ].nunique()

    python_jobs = df[
        "title"
    ].str.contains(
        "Python",
        case=False,
        na=False
    ).sum()

    python_percentage = round(
        (python_jobs / total_jobs) * 100,
        1
    ) if total_jobs else 0

    return {
        "total_jobs": total_jobs,
        "total_companies": total_companies,
        "total_locations": total_locations,
        "python_jobs": python_jobs,
        "python_percentage": python_percentage
    }