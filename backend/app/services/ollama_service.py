
import ollama


def generate_email(
    company_name,
    job_title,
    company_info
):

    prompt = f"""
You are the official Placement Coordination Team of IIIT Bhubaneswar writing a real placement outreach email to a company recruiter or hiring team.

Your goal is to professionally approach the company for internship, placement, and campus hiring opportunities for the 2026 graduating batch.

========================
COMPANY DETAILS
========================

Company Name:
{company_name}

Relevant Job Role:
{job_title}

Company Background:
{company_info}

========================
COLLEGE DETAILS
========================

Institute:
International Institute of Information Technology (IIIT) Bhubaneswar

Graduating Batch:
2026

Eligible Branches:
- Computer Engineering (CE)
- Computer Science Engineering (CSE)
- Information Technology (IT)
- Electronics & Telecommunication (ETC)
- Electrical & Electronics Engineering (EEE)

========================
EMAIL OBJECTIVE
========================

Write a professional placement outreach email requesting the company to consider IIIT Bhubaneswar students for:
- internships
- full-time roles
- campus recruitment opportunities

========================
WRITING STYLE
========================

The email MUST:
- sound natural and human-written
- sound professional and confident
- feel personalized to the company
- reference the company domain/work naturally
- mention the relevant role naturally
- avoid sounding overly sales-like
- avoid robotic AI wording
- avoid generic template language
- avoid repetition
- avoid bullet points
- avoid placeholders
- avoid exaggerated claims

========================
IMPORTANT INSTRUCTIONS
========================

- Keep the email concise but impactful
- Keep tone formal and respectful
- Maximum length: 220 words
- Write in proper paragraphs
- Mention why IIIT Bhubaneswar students are suitable
- End with a polite call for further discussion or collaboration

========================
OUTPUT RULES
========================

Return ONLY the email body.

Do NOT generate:
- subject line
- greetings like "Dear Sir/Madam" repeatedly
- explanations
- notes
- markdown
- bullet points
"""

    response = ollama.chat(

        model="llama3.2:3b",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


def generate_custom_email(

    company_name,

    hr_name,

    position,

    company_info,

    custom_prompt
):

    final_prompt = f"""
{custom_prompt}

========================
COMPANY DETAILS
========================

Company Name:
{company_name}

HR Name:
{hr_name}

Position:
{position}

Company Information:
{company_info}

========================
IMPORTANT INSTRUCTIONS
========================

- Personalize the email according to the company
- Mention company work/domain naturally
- Mention the role naturally
- Keep the tone professional
- Sound human-written
- Avoid robotic AI wording
- Keep it concise
- Write proper paragraphs
- No bullet points
- No placeholders
- Do not add any company facts unless they are present in Company Information.
- Do not praise the company using general statements.
- Do not mention hiring process, culture, values, products, or achievements without evidence.
- Use only the student's resume information and provided company context.

Generate ONLY the email body.
"""

    response = ollama.chat(

        model="llama3.2:3b",

        messages=[
            {
                "role": "user",
                "content": final_prompt
            }
        ]
    )

    return response["message"]["content"]
