from app.services.parsers.naukri_parser import parse_naukri_jobs
from app.services.parsers.foundit_parser import parse_foundit
from app.services.parsers.internshala_parser import parse_internshala


def parse_jobs(html):

    html_lower = html.lower()

    if "naukri" in html_lower:
        print("USING NAUKRI PARSER")
        return parse_naukri_jobs(html)

    elif "foundit" in html_lower:
        print("USING FOUNDIT PARSER")
        return parse_foundit_jobs(html)

    elif "internshala" in html_lower:
        print("USING INTERNSHALA PARSER")
        return parse_internshala_jobs(html)

    else:
        print("NO PARSER MATCHED")
        return []