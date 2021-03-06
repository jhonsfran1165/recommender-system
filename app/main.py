from fastapi import Depends, FastAPI
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from supertokens_python import get_all_cors_headers
from supertokens_python.framework.fastapi import get_middleware

from .api.api_v1.api import api_router
from .core.config import settings
from .core.json_config import ORJSONResponse

from supertokens_python import init, InputAppInfo, SupertokensConfig
from supertokens_python.recipe import emailpassword, session

from supertokens_python.recipe.session import SessionContainer
from supertokens_python.recipe.session.framework.fastapi import verify_session


app = FastAPI(
    default_response_class=ORJSONResponse,
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.add_middleware(get_middleware())

init(
    app_info=InputAppInfo(
        app_name="Recommender System",
        api_domain="http://localhost:8000",
        website_domain="http://localhost:3000",
        api_base_path=f"{settings.API_V1_STR}/auth/",
        website_base_path="/auth/"
    ),
    supertokens_config=SupertokensConfig(
        connection_uri="http://recommender-login:3567",
        # api_key="IF YOU HAVE AN API KEY FOR THE CORE, ADD IT HERE"
    ),
    framework='fastapi',
    recipe_list=[
        session.init(),  # initializes session features
        emailpassword.init()
    ],
    mode='wsgi',  # use asgi - wsgi,
    telemetry=False
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            str(origin) for origin in settings.BACKEND_CORS_ORIGINS
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["Content-Type"] + get_all_cors_headers(),
    )

app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/sessioninfo")
async def get_session_info(
    session_: SessionContainer = Depends(verify_session())
):
    return JSONResponse(
        {
            "sessionHandle": session_.get_handle(),
            "userId": session_.get_user_id(),
            "accessTokenPayload": session_.get_access_token_payload(),
            "sessionData": await session_.get_session_data()
        }
    )
