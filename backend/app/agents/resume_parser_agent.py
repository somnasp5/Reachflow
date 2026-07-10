"""
Simple Resume Parser Agent
"""

import logging
import re

logger = logging.getLogger(__name__)


def extract_contact_info(lines, text):
    data = {
        "name": "",
        "email": "",
        "github": "",
        "linkedin": "",
        "college": "",
        "branch": "",
        "graduation_year": ""
    }

    # Name
    if lines:
        first = lines[0]
        if "@" not in first and len(first.split()) <= 4:
            data["name"] = first

    # Email
    match = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    if match:
        data["email"] = match.group()

    # Github
    match = re.search(r"github\.com/\S+", text, re.I)
    if match:
        data["github"] = match.group()

    # LinkedIn
    match = re.search(r"linkedin\.com/in/\S+", text, re.I)
    if match:
        data["linkedin"] = match.group()

    # Education details
    education_text = text.lower()

    if "iiit bhubaneswar" in education_text:
        data["college"] = "IIIT Bhubaneswar"

    elif "iit" in education_text:
        data["college"] = "IIT"

    year = re.search(r"20\d{2}", text)
    if year:
        data["graduation_year"] = year.group()

    if "electronics" in education_text or "etc" in education_text:
        data["branch"] = "Electronics & Telecommunication Engineering"

    elif "computer science" in education_text or "cse" in education_text:
        data["branch"] = "Computer Science Engineering"

    return data


def extract_sections(lines):
    result = {
        "skills": [],
        "projects": [],
        "experience": [],
        "education": "",
        "certifications": []
    }

    current = ""

    headers = {
        "skills": ["skills"],
        "projects": ["projects"],
        "experience": ["experience"],
        "education": ["education"],
        "certifications": ["certifications", "certificates"]
    }

    for line in lines:

        lower = line.lower()

        found = False

        for section, words in headers.items():

            if any(word == lower.rstrip(":") for word in words):
                current = section
                found = True
                break

        if found:
            continue

        if current == "skills":

            skills = re.split(r"[,|;/•]", line)

            for skill in skills:
                skill = skill.strip()
                if skill:
                    result["skills"].append(skill)

        elif current == "projects":
            result["projects"].append(line)

        elif current == "experience":
            result["experience"].append(line)

        elif current == "education":
            result["education"] += line + " "

        elif current == "certifications":
            result["certifications"].append(line)

    # Remove duplicates
    result["skills"] = list(dict.fromkeys(result["skills"]))

    return result


def resume_parser_agent(state):

    print("\n--- RESUME PARSER AGENT RUNNING ---")

    resume_text = state.get("resume_text", "")

    if not resume_text:
        return {"resume_context": {}}

    try:

        lines = [line.strip() for line in resume_text.split("\n") if line.strip()]

        contact = extract_contact_info(lines, resume_text)

        sections = extract_sections(lines)

        resume_context = {**contact, **sections}

        logger.info("Resume parsed successfully.")

        return {
            "resume_context": resume_context
        }

    except Exception as e:

        logger.error(e)

        return {
            "resume_context": {}
        }