def create_storage():
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
    return storage

storage = create_storage()

