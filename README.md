#Compliance Content Copilot

**Compliance Content Copilot** is an AI-powered backend service that generates tailored compliance policies and checklists using OpenAI's GPT-4 Turbo. It supports popular frameworks like **SOC 2**, **ISO 27001**, and **NIST CSF**, helping security teams, consultants, and startups generate audit-ready documents in minutes.

---

## Features

- Generate markdown-formatted policies in seconds
- Powered by OpenAI GPT-4.1 (`gpt-4-0125-preview`)
- Built with FastAPI for speed and flexibility
-  Environment-secured API key integration

---

## 🧪 Example Use Case

**POST** `/generate-policy/`

### Request Body:

```json
{
  "company_name": "Acme Inc.",
  "industry": "SaaS",
  "employee_count": 50,
  "cloud_provider": "AWS",
  "framework": "NIST CSF",
  "control_category": "Access Control Policy"
}
