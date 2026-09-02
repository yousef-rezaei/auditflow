from fastapi import FastAPI

app = FastAPI(
    title="AuditFlow API",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "service": "auditflow",
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
    }
