from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/", response_class=Response)
async def root(name: str, message: str):
    return Response(content=f"Hello {name}! {message}!", media_type="text/plain")