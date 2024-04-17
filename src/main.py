from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from src.api.files.controller import files_router


server = FastAPI(title="Google Drive Manipulation API", version="0.1.0")

cors_origin = ["http://localhost:3000"]

server.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@server.get("/", tags=["Home"], status_code=200, response_model=None)
async def redirect_to_docs():
    return RedirectResponse(url="/docs")

server.include_router(files_router)
