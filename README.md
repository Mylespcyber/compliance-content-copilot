# Compliance Content Copilot

**Compliance Content Copilot** is an AI-powered backend service that generates tailored compliance policies and checklists using OpenAI's GPT-4 Turbo. It supports popular frameworks like **SOC 2**, **ISO 27001**, and **NIST CSF**, helping security teams, consultants, and startups generate audit-ready documents in minutes.

---

## Features

- Generate markdown-formatted policies in seconds
- Powered by OpenAI GPT-4.1 (`gpt-4-0125-preview`)
- Built with FastAPI for speed and flexibility
-  Environment-secured API key integration

---

## Example Use Case

**POST** `/generate-policy/`

### Request Body:

 - "company_name": "Acme Inc."
 - "industry": "SaaS"
 - "employee_count": 50
 - "cloud_provider": "AWS"
 - "framework": "NIST CSF"
 - "control_category": "Access Control Policy"

## Example Respons
### Access Control Policy

**Company:** Acme Inc.  
**Framework:** SOC 2  

### Purpose
The purpose of this Access Control Policy is to...

### Scope
This policy applies to...

### Roles and Responsibilities
- CISO
- IT Admins
- Department Managers


### Policy Statements
1. Least privilege
2. MFA required
3. Role-based access control

## Tech Stack

Python 3.12

FastAPI

OpenAI SDK v1.x

dotenv (for local API key security)

Uvicorn (dev server)

## Getting Started
# Clone the repo
git clone https://github.com/Mylespcyber/compliance-content-copilot.git
cd compliance-content-copilot

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Add your OpenAI key to a .env file
echo "OPENAI_API_KEY=your-key-here" > .env

# Run the app
uvicorn app.main:app --reload
Open your browser to http://localhost:8000/docs to test the API using Swagger UI.

## 📈 Roadmap
 Add frontend UI with framework picker

 Generate full policy packs (multi-control export)

 PDF export

 User authentication + saved history

 Deploy backend to Render

