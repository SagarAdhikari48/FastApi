# Query Parameters - > value attached at the end of the path parameter
from fastapi import FastAPI

app = FastAPI()

all_customers = [
    {"id": 101, "name": "Sagar", "city": "Kathmandu", "risk": "low"},
    {"id": 102, "name": "Ram", "city": "Banepa", "risk": "low"},
    {"id": 103, "name": "Hari", "city": "Dhulikhel", "risk": "high"},
    {"id": 104, "name": "Shyam", "city": "Kathmandu", "risk": "low"},
    {"id": 105, "name": "Raju", "city": "Hetauda", "risk": "high"},
]


@app.get("/customers")
def get_customer(city: str, risk: str):
    filtered = [c for c in all_customers if (c["city"] == city and c["risk"] == risk)] 
    return {"city": city, "risk": risk, "count": len(filtered), "results": filtered}
