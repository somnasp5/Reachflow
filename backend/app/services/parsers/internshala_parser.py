from bs4 import BeautifulSoup


def parse_internshala(html):

    soup = BeautifulSoup(html, "lxml")

    jobs = []

    cards = soup.find_all(
        "div",
        class_="individual_internship"
    )

    print("\nTOTAL INTERNSHALA CARDS:")
    print(len(cards))

    for card in cards:

        try:

            title_tag = card.find(
                "a",
                class_="job-title-href"
            )

            company_tag = card.find(
                "p",
                class_="company-name"
            )

            location_tag = card.find(
                "p",
                class_="locations"
            )

            skill_tags = card.find_all(
                "div",
                class_="job_skill"
            )

            if not title_tag or not company_tag:
                continue

            role = title_tag.get_text(
                strip=True
            )

            company = company_tag.get_text(
                strip=True
            )

            location = ""

            if location_tag:

                location = location_tag.get_text(
                    strip=True
                )

            skills = []

            for skill in skill_tags:

                text = skill.get_text(
                    strip=True
                )

                if text:
                    skills.append(text)

            link = title_tag.get(
                "href",
                ""
            )

            if link.startswith("/"):

                link = (
                    "https://internshala.com"
                    + link
                )

            jobs.append({
                "company_name": company,
                "job_title": role,
            })

        except Exception as e:

            print(
                "INTERNSHALA PARSER ERROR:",
                e
            )

    return jobs