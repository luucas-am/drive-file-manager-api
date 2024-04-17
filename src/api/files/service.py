import json

from googleapiclient.http import MediaFileUpload

from src.errors.exceptions import BadRequestException, NotFoundException

class FileService:
    def get_all(service):
        results = service.files().list(pageSize=20, fields="nextPageToken, files(id, name)").execute()
        files = results.get('files', [])

        return files
    
    def get_one(service, file_id):
        file = service.files().get(fileId=file_id).execute()

        if not file:
            raise NotFoundException("File not found")

        return file
    
    def create_one(service, filename, filepath):
        file_extension = filepath.split('.')[-1]
        mimetypes = json.loads(open("mimetypes.json").read())

        try:
            mimetype = mimetypes[f".{file_extension}"]

            file_metadata = {'name': filename}
            media = MediaFileUpload(filepath, mimetype=mimetype)

            file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        except:
            raise BadRequestException("Failed to upload file. Check path and file extension.")
        
        return file
        
    def delete_one(service, file_id):
        file = service.files().delete(fileId=file_id).execute()
        return file