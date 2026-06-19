from fastapi import FastAPI

app = FastAPI()

customer_risk_profiles = {
    101: {"name": "sagar", "risk": "low", "score": 0.12},
    101: {"name": "Test", "risk": "medium", "score": 0.42},
    101: {"name": "abc", "risk": "high", "score": 0.72},
}


@app.get("/customer/{customer_id}")
def get_customer_risk(customer_id : int):
    if customer_id not in customer_risk_profiles:
        return {"error": "customer {customer_id} not found!"}
    profile = customer_risk_profiles[customer_id]

    return {
        "customer_id": customer_id,
        "name": profile["name"],
        "risk_level": profile["risk"],
        "score": profile["score"],
    }
    
@app.get("/model/{model_name}/customer/{customer_id}")
def get_model_prediction(model_name: str, customer_id: int):
    return {
        "model" : model_name,
        "customer_id": customer_id,
        "prediction":"high risk"
        
    }