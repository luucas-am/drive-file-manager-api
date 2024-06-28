from src.errors.exceptions import BadRequestException, NotFoundException

class FolderService:
    def get_all(service):
        results = service.files().list(q="mimeType='application/vnd.google-apps.folder'", pageSize=20, fields="nextPageToken, files(id, name)").execute()
        folders = results.get('files', [])

        return folders
    
    def get_one(service, folder_id):
        folder = service.files().get(fileId=folder_id).execute()

        if not folder:
            raise NotFoundException("Folder not found")

        return folder
    
    def get_files(service, folder_id):
        results = service.files().list(q=f"'{folder_id}' in parents", pageSize=20, fields="nextPageToken, files(id, name)").execute()
        files = results.get('files', [])

        return files
    
    def create_one(service, foldername):
        file_metadata = {
            'name': foldername,
            'mimeType': 'application/vnd.google-apps.folder'
        }

        folder = service.files().create(body=file_metadata, fields='id').execute()
        
        return folder
    
    def create_one_in_folder(service, foldername, parent_id):
        file_metadata = {
            'name': foldername,
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': [parent_id]
        }

        folder = service.files().create(body=file_metadata, fields='id').execute()
        
        return folder
        
    def delete_one(service, folder_id):
        folder = service.files().delete(fileId=folder_id).execute()
        return folder