import re

from app.services.company_search_service import search_google


EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"


def get_company_emails(company_name):

    queries = [

        f"{company_name} HR email",

        f"{company_name} careers email",

        f"{company_name} recruiter email"

    ]

    found = set()

    for query in queries:

        results = search_google(query)

        for result in results:

            snippet = result.get("snippet", "")

            emails = re.findall(EMAIL_REGEX, snippet)

            for email in emails:

                found.add(email)

    return list(found)