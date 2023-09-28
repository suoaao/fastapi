from fastapi import Cookie, Depends, FastAPI

app = FastAPI()


def query_extractor(q: str = None):
    return q


def query_or_cookie_extractor(
    q: str = Depends(query_extractor), last_query: str = Cookie(None)
):
    return last_query if not q else q


@app.get("/items/")
async def read_query(query_or_default: str = Depends(query_or_cookie_extractor)):
    return {"q_or_cookie": query_or_default}
