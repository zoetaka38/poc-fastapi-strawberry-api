import logging

import strawberry
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from mangum import Mangum
from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig
from strawberry.subscriptions import GRAPHQL_TRANSPORT_WS_PROTOCOL, GRAPHQL_WS_PROTOCOL

from app.api.v1.main import router as api_router
from app.graphql.schemas.mutation_schema import Mutation
from app.graphql.schemas.query_schema import Query
from app.settings import settings

graphql_schema = strawberry.Schema(query=Query, mutation=Mutation, config=StrawberryConfig(auto_camel_case=True))

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router, prefix="/api/v1")

graphql_app = GraphQLRouter(
    graphql_schema,
    subscription_protocols=[
        GRAPHQL_TRANSPORT_WS_PROTOCOL,
        GRAPHQL_WS_PROTOCOL,
    ],
    graphiql=settings.RACK_ENV == "local",
)
app.include_router(graphql_app, prefix="/graphql")


@app.get("/api", include_in_schema=False)
@app.get("/api/v1/health", include_in_schema=False)
def health() -> JSONResponse:
    """ヘルスチェック"""
    return JSONResponse({"message": "It worked!!"})


handler = Mangum(app, "off")  # FastAPIのインスタンスをMangumのコンストラクタに渡して、handlerとして読めるようにしておく

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000, reload=True)
