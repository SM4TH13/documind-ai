from fastapi import FastAPI

app = FastAPI()


app = FastAPI(
    title="DocuMind AI API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Bienvenue sur DocuMind AI"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }