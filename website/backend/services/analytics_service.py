import pandas as pd


def get_analytics(df):
    """
    Generate analytics data for the dashboard.
    """

    python_jobs = df[
        df["title"].str.contains(
            "Python",
            case=False,
            na=False
        )
    ]

    python_count = len(
        python_jobs
    )

    non_python_count = (
        len(df) - python_count
    )

    company_data = (
        df["company"]
        .value_counts()
        .head(10)
        .to_dict()
    )

    location_data = (
        df["location"]
        .value_counts()
        .head(10)
        .to_dict()
    )

    date_data = (
        df["posted_date"]
        .value_counts()
        .sort_index()
        .to_dict()
    )

    total_jobs = len(df)

    total_companies = df[
        "company"
    ].nunique()

    total_locations = df[
        "location"
    ].nunique()

    python_percentage = round(
        (python_count / total_jobs) * 100,
        1
    ) if total_jobs else 0

    return {
        "total_jobs": total_jobs,
        "total_companies": total_companies,
        "total_locations": total_locations,
        "python_count": python_count,
        "non_python_count": non_python_count,
        "python_percentage": python_percentage,
        "company_data": company_data,
        "location_data": location_data,
        "date_data": date_data
    }