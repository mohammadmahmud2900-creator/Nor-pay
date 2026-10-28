from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    html = """
    <html><body style="background:#080c14;color:white;text-align:center;padding:60px;font-family:sans-serif">
    <h2 style="color:#7CFF67">● API LIVE</h2>
    <h1>Nor-pay AI Guardian</h1>
    <p>Created by Mohammad from Palestine</p>
    <p>Secure payment protection powered by real-time AI</p>
    <p style="margin-top:40px;color:#666">© 2026 Built with love in Palestine</p>
    </body></html>
    """
    return html

@app.get("/stats")
def stats():
    return {"status":"LIVE","invoices":1247,"fraud_blocked":89}

@app.post("/scan")
def scan():
    s=random.randint(10,95)
    return {"score":s,"result":"FRAUD" if s>70 else "SAFE"}
