from bs4 import BeautifulSoup


def parse_foundit(html):

    soup = BeautifulSoup(html, "lxml")

    jobs = []

    cards = soup.find_all(
        "div",
        class_="flex flex-col gap-4 rounded-2xl"
    )

    print("\nTOTAL FOUNDIT CARDS:")
    print(len(cards))

    for card in cards:

        try:

            title_tag = card.find(
                "h2",
                class_="jobCardTitle"
            )

            company_tag = card.find(
                "span",
                class_="jobCardCompany"
            )

            location_tag = card.find(
                "div",
                class_="jobCardLocation"
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

            link_tag = title_tag.find("a")

            link = ""

            if link_tag:

                link = link_tag.get("href", "")

            jobs.append({
                "company_name": company,
                "job_title":role,
            })

        except Exception as e:

            print("FOUNDIT PARSER ERROR:", e)

    return jobs