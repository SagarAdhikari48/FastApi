### -> Pydantic is the python library  which defines the shape of data the comes through incomming request. entire validation occurs. reads the json and compare with the validation
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class LoanApplication(BaseModel):
    name: str
    age: int
    income: float
    loan_amount: float
    employment_years: int


@app.post("/prediction")
def predict_loadn(application: LoanApplication):
    approved = (
        application.income > 500000
        and application.employment_years > 2
        and application.age >= 21
    )

    return {
        "applicant name": application.name,
        "loan_amount": application.loan_amount,
        "decision": "approved" if approved else "rejected",
        "reviewed_incoome": application.income,
    }
