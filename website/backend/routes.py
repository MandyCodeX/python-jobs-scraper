from flask import (
    Blueprint,
    render_template,
    request
)

from backend.services.job_service import (
    load_jobs,
    search_jobs,
    filter_python_jobs,
    sort_jobs,
    get_job_by_id,
    get_job_skills,
    get_job_statistics
)

from backend.services.analytics_service import (
    get_analytics
)


main = Blueprint(
    "main",
    __name__
)


@main.route("/")
def home():

    df = load_jobs()

    search = request.args.get(
        "search",
        ""
    ).strip()

    python_only = request.args.get(
        "python_only"
    )

    sort = request.args.get(
        "sort",
        "title"
    )

    # Search
    df = search_jobs(
        df,
        search
    )

    # Python filter
    df = filter_python_jobs(
        df,
        python_only
    )

    # Sorting
    df = sort_jobs(
        df,
        sort
    )

    jobs = df.to_dict(
        orient="records"
    )

    statistics = get_job_statistics(
        df
    )

    return render_template(
        "index.html",
        jobs=jobs,
        search=search,
        python_only=python_only,
        sort=sort,
        **statistics
    )


@main.route("/job/<int:job_id>")
def job_detail(job_id):

    job = get_job_by_id(
        job_id
    )

    if job is None:

        return "Job not found", 404

    skills = get_job_skills(
        job["description"]
    )

    return render_template(
        "job_detail.html",
        job=job,
        skills=skills
    )


@main.route("/analytics")
def analytics():

    df = load_jobs()

    analytics_data = get_analytics(
        df
    )

    return render_template(
        "analytics.html",
        **analytics_data
    )