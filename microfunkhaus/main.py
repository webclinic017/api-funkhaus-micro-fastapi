import json
from fastapi import (
    FastAPI,
    Response,
    HTTPException,
    status,
    Path,
    Header,
    Depends,
)
from API import (
    PerformanceRequest,
    LabelingRequest,
    AmendmentRequest,
    GenericRequest,
    PerformanceResponse,
)
from aiohttp import ClientResponseError
from actions import generate_progression, send_labels, amend_progression, create_user


with open("config.json", "r") as config_file:
    config = json.load(config_file)
    TITLE = config["title"]
    PORT = config["port"]
    HOST = config["host"]
    RELOAD = config["reload"]

with open(".tokens.json", "r") as token_file:
    TOKENS = set(json.load(token_file))

async def check_token(x_token: str = Header()):
    if x_token not in TOKENS:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")


app = FastAPI(
    title="microfunkhaus",
    docs_url='/',
    dependencies=[Depends(check_token)],
    )


generation_description = """You can specify the optional key and mode (graph) parameters,
or even supply the otherwise verbatim progression with a changed key to transpose it."""
@app.post(
    "/generate",
    summary="Generates a new progression",
    description=generation_description,
    response_description="A generated progression",
    response_model=PerformanceResponse,
    status_code=status.HTTP_200_OK,
    )
async def gen_progression(
    performance: PerformanceRequest
    ):
    try:
        responses = await generate_progression(performance)
    except ClientResponseError as e:
        raise HTTPException(status_code=e.status, detail=e.message)
    return responses


amendment_description = """It is crucially important to provide a valid performance object,
copied verbatim from the response of the '/generate' endpoint.
Can return a 204 'No Content' if the chord change is impossible."""
@app.post(
    "/amend/{index}",
    summary="Changes a specified chord in a progression",
    description=amendment_description,
    response_description="An amended progression",
    response_model=PerformanceResponse,
    status_code=status.HTTP_200_OK,
    )
async def amend_performance(
    full_request: AmendmentRequest,
    index: int = Path(
        ...,
        title="Index",
        description="The chord under this index will be substituted",
        example=1,
        )
    ):
    try:
        responses = await amend_progression(full_request, index)
    except ClientResponseError as e:
        raise HTTPException(status_code=e.status, detail=e.message)
    return responses


@app.post("/label")
async def label_progression(labeling_request: LabelingRequest):
    try:
        await send_labels(labeling_request)
    except ClientResponseError as e:
        raise HTTPException(status_code=e.status, detail=e.message)
    return Response(status_code=201)

@app.post("/create_user_id")
async def initialize_user(request: GenericRequest):
    try:
        user_obj = await create_user(request)
    except ClientResponseError as e:
        raise HTTPException(status_code=e.status, detail=e.message)
    return Response(content=user_obj.json(), status_code=201, media_type="application/json")


if __name__=="__main__":
    import uvicorn
    uvicorn.run("main:app", host=HOST, port=PORT, reload=RELOAD)