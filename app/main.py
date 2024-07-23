from fastapi import fastAPI

app = fastAPI

@app.get("/")
def index():
    return {"message": "Hello World"}


@app.get("/about")
def index():
    return {"message": "Hello World"}