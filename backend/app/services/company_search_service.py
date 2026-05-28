import re

from app.services.google_search_service import search_google


EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"


BAD_EMAIL_WORDS = [
    "noreply",
    "no-reply",
    "support",
    "help",
    "privacy",
    "legal",
    "abuse",
    "security",
    "feedback",
    "notification",
    "donotreply",
    "example.com"
]


GOOD_EMAIL_WORDS = [
    "hr",
    "career",
    "careers",
    "recruit",
    "recruitment",
    "hiring",
    "jobs",
    "talent",
    "campus"
]


def clean_email(email):

    email = email.strip().lower()

    if len(email) < 5:
        return None

    for bad in BAD_EMAIL_WORDS:
        if bad in email:
            return None

    return email


def extract_emails(text):

    raw_emails = re.findall(EMAIL_REGEX, text)

    cleaned = []

    for email in raw_emails:

        email = clean_email(email)

        if email:
            cleaned.append(email)

    return cleaned


def score_email(email):

    score = 0

    for word in GOOD_EMAIL_WORDS:
        if word in email:
            score += 10

    return score


def get_company_emails(company_name):

    queries = [

        f"{company_name} HR email",

        f"{company_name} careers email",

        f"{company_name} recruitment email",

        f"{company_name} talent acquisition email",

        f"{company_name} campus hiring email",

        f"{company_name} recruiter email",

        f"{company_name} contact email"
    ]

    found_emails = set()

    for query in queries:

        try:

            results = search_google(query)

            for result in results:

                title = result.get("title", "")

                snippet = result.get("snippet", "")

                link = result.get("link", "")

                combined_text = f"""
                {title}
                {snippet}
                {link}
                """

                emails = extract_emails(combined_text)

                for email in emails:
                    found_emails.add(email)

        except Exception as e:

            print("EMAIL SEARCH ERROR:", e)

    ranked = sorted(
        list(found_emails),
        key=score_email,
        reverse=True
    )

    return ranked[:5]


def get_company_info(company_name):

    query = f"{company_name} company overview"

    try:

        results = search_google(query)

        info = []

        for result in results[:3]:

            snippet = result.get("snippet", "")

            if snippet:
                info.append(snippet)

        return "\n".join(info)

    except Exception as e:

        print("COMPANY INFO ERROR:", e)

        return ""