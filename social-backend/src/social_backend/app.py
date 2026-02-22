from fastapi import FastAPI


app = FastAPI(
    title="Social Backend",
)


@app.get("")
def hello_world() -> dict[str, str]:
    return {"message": "Hello World"}
