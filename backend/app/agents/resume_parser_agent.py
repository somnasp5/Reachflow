"""
Resume Parser Agent for extracting key information from resume text.
"""

import logging
import re
from typing import Dict, List, Any

logger = logging.getLogger(__name__)

# Define section headers we're looking for (case-insensitive)
SECTION_HEADERS = {
    "skills": [
        "skills", "technical skills", "technologies", "programming languages",
        "tools", "languages", "technical expertise", "competencies"
    ],
    "projects": [
        "projects", "personal projects", "academic projects", "project experience",
        "key projects", "selected projects", "project work"
    ],
    "experience": [
        "experience", "work experience", "professional experience", "employment",
        "work history", "professional background", "career history"
    ],
    "education": [
        "education", "academic background", "academic education", "educational background",
        "academic qualifications", "qualifications"
    ],
    "certifications": [
        "certifications", "certificates", "licenses", "accreditations",
        "professional certifications", "coursework"
    ]
}

# Sections to ignore (we won't capture content under these)
IGNORE_SECTIONS = [
    "summary", "profile", "personal", "personal information", "contact",
    "contact information", "address", "phone", "email", "linkedin", "github",
    "hobbies", "interests", "references", "objective", "objectives"
]

def _is_header_line(line: str, headers: List[str]) -> bool:
    """Check if a line matches any of the given headers (case-insensitive)."""
    line_lower = line.strip().lower()
    for header in headers:
        # Match exact header or header followed by colon
        if line_lower == header.lower() or line_lower.startswith(header.lower() + ":"):
            return True
        # Also match common variations like "Skills:" or "SKILLS"
        if re.match(rf"^{re.escape(header)}[\s:-]*$", line_lower, re.IGNORECASE):
            return True
    return False

def _get_section_content(lines: List[str], start_idx: int, stop_headers: List[str]) -> List[str]:
    """
    Extract content lines starting from start_idx until we hit a stop header or end of lines.
    """
    content = []
    for i in range(start_idx, len(lines)):
        line = lines[i].strip()
        if not line:
            # Skip empty lines but continue in case there's more content
            continue

        # Check if this line is a header we should stop at (either target or ignore)
        if _is_header_line(line, stop_headers):
            break

        content.append(line)
    return content

def _extract_skills(text_lines: List[str]) -> List[str]:
    """Extract and clean skills from the skills section."""
    skills = []
    # Find skills section
    in_skills = False
    skills_lines = []

    for line in text_lines:
        stripped = line.strip()
        if not stripped:
            continue

        if _is_header_line(stripped, SECTION_HEADERS["skills"]):
            in_skills = True
            continue

        # Stop if we hit another section header (target or ignore)
        if in_skills and (_is_header_line(stripped,
                           [h for sect in SECTION_HEADERS.values() for h in sect] +
                           IGNORE_SECTIONS)):
            in_skills = False
            continue

        if in_skills:
            skills_lines.append(stripped)

    # Process skills lines: split by common delimiters
    for line in skills_lines:
        # Split by commas, semicolons, newlines, and bullet points
        parts = re.split(r'[,;\n\-•\*]', line)
        for part in parts:
            cleaned = part.strip()
            if cleaned and len(cleaned) > 1:  # Avoid single characters
                skills.append(cleaned)

    # Remove duplicates while preserving order
    seen = set()
    unique_skills = []
    for skill in skills:
        if skill.lower() not in seen:
            seen.add(skill.lower())
            unique_skills.append(skill)

    return unique_skills

def _extract_section_as_list(text_lines: List[str], section_key: str) -> List[str]:
    """Extract a section (projects, experience, certifications) as a list of entries."""
    entries = []
    in_section = False
    section_lines = []

    for line in text_lines:
        stripped = line.strip()
        if not stripped:
            continue

        if _is_header_line(stripped, SECTION_HEADERS[section_key]):
            in_section = True
            # Save previous section content if any
            if section_lines:
                entries.append(" ".join(section_lines))
                section_lines = []
            continue

        # Stop if we hit another section header (target or ignore)
        if in_section and (_is_header_line(stripped,
                           [h for sect in SECTION_HEADERS.values() for h in sect] +
                           IGNORE_SECTIONS)):
            in_section = False
            if section_lines:
                entries.append(" ".join(section_lines))
                section_lines = []
            continue

        if in_section:
            section_lines.append(stripped)

    # Don't forget the last section
    if in_section and section_lines:
        entries.append(" ".join(section_lines))

    # Clean up entries: remove empty and very short ones
    cleaned_entries = []
    for entry in entries:
        entry = entry.strip()
        if entry and len(entry) > 3:  # Avoid meaningless entries
            cleaned_entries.append(entry)

    return cleaned_entries

def _extract_section_as_string(text_lines: List[str], section_key: str) -> str:
    """Extract a section (education) as a single string."""
    in_section = False
    section_lines = []

    for line in text_lines:
        stripped = line.strip()
        if not stripped:
            continue

        if _is_header_line(stripped, SECTION_HEADERS[section_key]):
            in_section = True
            # Save previous section content if any
            if section_lines:
                section_lines = []  # Reset for new section
            continue

        # Stop if we hit another section header (target or ignore)
        if in_section and (_is_header_line(stripped,
                           [h for sect in SECTION_HEADERS.values() for h in sect] +
                           IGNORE_SECTIONS)):
            in_section = False
            break

        if in_section:
            section_lines.append(stripped)

    # Join lines with spaces for education
    return " ".join(section_lines).strip()

def resume_parser_agent(state):
    """
    Parse resume text to extract skills, projects, experience, education, and certifications.
    """
    print("\n--- RESUME PARSER AGENT RUNNING ---")

    resume_text = state.get("resume_text", "")
    if not resume_text:
        logger.warning("No resume text provided")
        return {
            "resume_context": {
                "skills": [],
                "projects": [],
                "experience": [],
                "education": "",
                "certifications": []
            }
        }

    try:
        # Split text into lines
        lines = resume_text.split('\n')

        # Extract each section
        skills = _extract_skills(lines)
        projects = _extract_section_as_list(lines, "projects")
        experience = _extract_section_as_list(lines, "experience")
        education = _extract_section_as_string(lines, "education")
        certifications = _extract_section_as_list(lines, "certifications")

        logger.info(f"Parsed resume: {len(skills)} skills, {len(projects)} projects, "
                   f"{len(experience)} experience entries, {len(certifications)} certifications")

        return {
            "resume_context": {
                "skills": skills,
                "projects": projects,
                "experience": experience,
                "education": education,
                "certifications": certifications
            }
        }

    except Exception as e:
        logger.error(f"Error parsing resume: {e}")
        # Return empty structure on error to avoid breaking the pipeline
        return {
            "resume_context": {
                "skills": [],
                "projects": [],
                "experience": [],
                "education": "",
                "certifications": []
            }
        }