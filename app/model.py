import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_policy_prompt(company, industry, size, cloud, framework, control):
    return f"""
You are a compliance consultant generating documentation for a {industry} company named {company}.

Company Details:
- Name: {company}
- Industry: {industry}
- Employee Count: {size}
- Cloud Provider: {cloud}
- Compliance Framework: {framework}

Task:
Generate a {control} that aligns with the {framework} framework. Use markdown format with:
- Purpose
- Scope
- Roles and Responsibilities
- Policy Statements
- Review and Maintenance
"""

def generate_policy(company, industry, size, cloud, framework, control):
    prompt = generate_policy_prompt(company, industry, size, cloud, framework, control)
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": "You generate professional compliance policies."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )
    return response.choices[0].message.content

