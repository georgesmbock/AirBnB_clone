#!/usr/bin/python3
from models.engine.file_storage import FileStorage

"""
create a unique filestorage instance
"""
storage = FileStorage()
"""
call relaod() method on this variable to load date from JSON file
"""
storage.reload()
