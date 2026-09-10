import requests
from bs4 import BeautifulSoup
import csv


URL = "https://realpython.github.io/fake-jobs/"


def get_page():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(
            URL,
            headers=headers,
            timeout=5
        )

        response.raise_for_status()

        return response.text

    except requests.RequestException as e:
        print("Error accessing the website:", e)

        return None


def get_job_details(url):

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    for attempt in range(3):

        try:

            response = requests.get(
                url,
                headers=headers,
                timeout=5
            )

            response.raise_for_status()

            break

        except requests.RequestException as e:

            print(f"Attempt {attempt + 1}/3 failed")

            if attempt == 2:

                print("Giving up on this job")

                return {
                    "description": "Description not available",
                    "location": "Location not available",
                    "posted_date": "Date not available"
                }

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    content = soup.find(
        "div",
        class_="content"
    )

    description_parts = []

    location = "Location not found"

    posted_date = "Date not found"

    if content:

        paragraphs = content.find_all("p")

        for paragraph in paragraphs:

            text = paragraph.get_text(
                " ",
                strip=True
            )

            if text.startswith("Location:"):

                location = text.replace(
                    "Location:",
                    ""
                ).strip()

            elif text.startswith("Posted:"):

                posted_date = text.replace(
                    "Posted:",
                    ""
                ).strip()

            else:

                description_parts.append(text)

    description = " ".join(
        description_parts
    )

    return {
        "description": description,
        "location": location,
        "posted_date": posted_date
    }


def scrape_jobs(html):

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    job_cards = soup.find_all(
        "div",
        class_="card-content"
    )

    jobs = []

    for index, card in enumerate(
        job_cards,
        start=1
    ):

        print(
            f"Scraping job {index}/{len(job_cards)}..."
        )

        title = card.find(
            "h2",
            class_="title"
        )

        company = card.find(
            "h3",
            class_="company"
        )

        location = card.find(
            "p",
            class_="location"
        )

        link_container = card.find(
            "a",
            string="Apply"
        )

        if (
            title
            and company
            and location
            and link_container
        ):

            job_url = link_container.get(
                "href"
            )

            details = get_job_details(
                job_url
            )

            job = {

                "title": title.get_text(
                    strip=True
                ),

                "company": company.get_text(
                    strip=True
                ),

                "location": location.get_text(
                    strip=True
                ),

                "description": details[
                    "description"
                ],

                "posted_date": details[
                    "posted_date"
                ],

                "link": job_url
            }

            jobs.append(job)

    return jobs


def save_to_csv(jobs):

    with open(
        "data/jobs.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        fieldnames = [

            "title",
            "company",
            "location",
            "description",
            "posted_date",
            "link"

        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        writer.writerows(jobs)


def main():

    html = get_page()

    if html is None:
        return

    jobs = scrape_jobs(html)

    print(
        f"Total jobs found: {len(jobs)}"
    )

    for job in jobs:

        print("-----------------------------")

        print(
            "Title:",
            job["title"]
        )

        print(
            "Company:",
            job["company"]
        )

        print(
            "Location:",
            job["location"]
        )

        print(
            "Description:",
            job["description"][:100],
            "..."
        )

        print(
            "Posted Date:",
            job["posted_date"]
        )

        print(
            "Link:",
            job["link"]
        )

    save_to_csv(jobs)

    print(
        "\nJobs saved to data/jobs.csv"
    )


if __name__ == "__main__":
    main()