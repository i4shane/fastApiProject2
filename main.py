from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello AI"}


@app.get("/", tags=["test"])
async def say_hello(name: str):
    return {"message": f"Hello World"}
