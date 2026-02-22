from fastapi import FastAPI


app = FastAPI(
    title="Social Backend",
)

@app.get("")
def hello_world():
    return {"message": "Hello World"}

