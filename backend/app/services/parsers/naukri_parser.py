from bs4 import BeautifulSoup


def parse_naukri_jobs(html):
    soup = BeautifulSoup(html, "html.parser")

    jobs = []

    job_cards = soup.select("div.srp-jobtuple-wrapper")

    print("FOUND JOB CARDS:", len(job_cards))

    for card in job_cards[:20]:
        try:
            title_tag = card.select_one("a.title")
            company_tag = card.select_one("a.comp-name")
            location_tag = card.select_one(".locWdth")

            if not title_tag or not company_tag:
                continue

            title = title_tag.get_text(strip=True)
            company = company_tag.get_text(strip=True)

            location = ""
            if location_tag:
                location = location_tag.get_text(strip=True)

            link = title_tag.get("href", "")

            jobs.append({
                "company_name": company,
                "job_title": title,
            })

        except Exception as e:
            print("PARSER ERROR:", e)

    print("PARSED JOBS:", len(jobs))

    return jobs