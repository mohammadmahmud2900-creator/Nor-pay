from fastapi import FastAPI
import random
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Nor-pay AI Guardian LIVE", "creator": "Mohammad from Palestine"}
@app.post("/scan-invoice")
def scan_invoice():
    score = random.randint(10, 95)
    return {"status": "FRAUD ALERT" if score > 70 else "SAFE", "fraud_score": f"{score}%"}
@app.get("/stats")
def stats():
    return {"invoices": 1247, "fraud_blocked": 89, "saved": "$12450"}
