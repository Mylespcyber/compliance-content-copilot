from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.model import generate_policy

app = FastAPI()

class PolicyRequest(BaseModel):
    company_name: str
    industry: str
    employee_count: int
    cloud_provider: str
    framework: str
    control_category: str

@app.post("/generate-policy/")
async def create_policy(request: PolicyRequest):
    try:
        content = generate_policy(
            request.company_name,
            request.industry,
            request.employee_count,
            request.cloud_provider,
            request.framework,
            request.control_category
        )
        return {"policy_markdown": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

