from os import getenv
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter
from ..auth.middleware import authentication_middleware, graphql_api_path
from services.financial.schema.advisor import schema

app = FastAPI()

# origins = [
#     "https://studio.apollographql.com",
# ]


@app.middleware("http")
async def cors_handler(request: Request, call_next):
    response: Response = await call_next(request)
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response


@app.middleware('http')
async def authenticate(request: Request, call_next):
    return await authentication_middleware(request, call_next, 'financial')

graphql_app = GraphQLRouter(schema, path=graphql_api_path,
                            graphiql=bool(int(getenv("NWM_DEBUG_MODE", default="1"))))

app.include_router(graphql_app)

# @app.middleware("http")
# async def check_router_security(
#     request: Request, call_next: Callable[[Request], Awaitable[Response]]
# ) -> Response:
#     router_secret = environ.get("ROUTER_SECRET")
#     if router_secret is None:
#         return await call_next(request)
#     if request.headers.get("Router-Authorization") != router_secret:
#         return Response(status_code=HTTPStatus.UNAUTHORIZED)
#     return await call_next(request)
