from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def my_endpoint():
    return {"message": "Hello World"}