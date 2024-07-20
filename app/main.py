from fastapi import fastAPI

app = fastAPI

@app.get("/")
def index():
    return {"message": "Hello World"}