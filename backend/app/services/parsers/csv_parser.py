import csv
from io import StringIO


def parse_csv_jobs(csv_content: str):
    jobs = []

    reader = csv.DictReader(StringIO(csv_content))

    for row in reader:
        company = row.get("company_name", "").strip()
        title = row.get("position", "").strip()
        email = row.get("email", "").strip()
        hr_name = row.get("hr_name", "").strip()

        if company and title:
            jobs.append({
                "company_name": company,
                "job_title": title,
                "company_email": email,
                "hr_name": hr_name
            })

    print(f"CSV Parser extracted {len(jobs)} jobs")
    print(jobs[:3])

    return jobs