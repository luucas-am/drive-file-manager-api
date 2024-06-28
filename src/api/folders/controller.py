from fastapi import APIRouter, Depends

from src.constants import get_authenticated_service
from src.api.folders.service import FolderService

folders_router = APIRouter(
    prefix='/api/folders',
    tags=['Folders'],
    dependencies=[Depends(get_authenticated_service)]
)

@folders_router.get('/', status_code=200)
async def get_all(service=folders_router.dependencies[0]):
    return FolderService.get_all(service=service)

@folders_router.get('/{folder_id}', status_code=200)
async def get_one(folder_id: str, service=folders_router.dependencies[0]):
    return FolderService.get_one(service=service, folder_id=folder_id)

@folders_router.get('/{folder_id}/files', status_code=200)
async def get_files(folder_id: str, service=folders_router.dependencies[0]):
    return FolderService.get_files(service=service, folder_id=folder_id)

@folders_router.post('/', status_code=201)
async def create_one(foldername: str, service=folders_router.dependencies[0]):
    return FolderService.create_one(service=service, foldername=foldername)

@folders_router.post('/{folder_id}', status_code=201)
async def create_one_in_folder(foldername: str, folder_id: str, service=folders_router.dependencies[0]):
    return FolderService.create_one_in_folder(service=service, foldername=foldername, parent_id=folder_id)

@folders_router.delete('/{folder_id}', status_code=200)
async def delete_one(folder_id: str, service=folders_router.dependencies[0]):
    return FolderService.delete_one(service=service, folder_id=folder_id)