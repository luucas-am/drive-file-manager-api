from fastapi import APIRouter, Depends

from src.constants import get_authenticated_service
from src.api.files.service import FileService

files_router = APIRouter(
    prefix='/api/files',
    tags=['Files'],
    dependencies=[Depends(get_authenticated_service)]
)

@files_router.get('/', status_code=200)
async def get_all(service=files_router.dependencies[0]):
    return FileService.get_all(service=service)

@files_router.get('/{file_id}', status_code=200)
async def get_one(file_id: str, service=files_router.dependencies[0]):
    return FileService.get_one(service=service, file_id=file_id)

@files_router.get('/{file_id}/download', status_code=200)
async def download_one(file_id: str, local_filepath: str, service=files_router.dependencies[0]):
    return FileService.download_one(service=service, file_id=file_id, local_filepath=local_filepath)

@files_router.post('/', status_code=201)
async def create_one(filename: str, filepath: str, service=files_router.dependencies[0]):
    return FileService.create_one(service=service, filename=filename, filepath=filepath)

@files_router.post('/{folder_id}', status_code=201)
async def create_one_in_folder(filename: str, filepath: str, folder_id: str, service=files_router.dependencies[0]):
    return FileService.create_one_in_folder(service=service, filename=filename, filepath=filepath, parent_id=folder_id)


@files_router.post('/{file_id}/shared', status_code=201)
async def create_one_in_folder_shared(filename: str, filepath: str, folder_id: str, service=files_router.dependencies[0]):
    return FileService.create_one_in_folder_shared(service=service, filename=filename, filepath=filepath, parent_id=folder_id)

@files_router.delete('/{file_id}', status_code=200)
async def delete_one(file_id: str, service=files_router.dependencies[0]):
    return FileService.delete_one(service=service, file_id=file_id)