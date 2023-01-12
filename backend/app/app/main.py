from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse

from app.api.api_v1.api import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.get("/", response_class=HTMLResponse)
def main_page_welcome():
    return """
    <html>
        <head>
            <title>Title BE page</title>
        </head>
        <body>
            <h1>Hello. This is main page of back-end</h1>
            <p><a href="./docs">See interactive documentation here</a></p>
            <p>API to play with is /items: 
            
            You can list, create and delete items:
            <ul>
            <li><a href="./api/items/">List all items</a> with  GET /items
            <li>Create item with POST /items (pass name and description in body in JSON format) 
            <li>And delete item with DELETE item/{id}
            </ul>
            </p>
        </body>
    </html>
    """


app.include_router(api_router, prefix=settings.API_V1_STR)
