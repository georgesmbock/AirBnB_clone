#!/usr/bin/python3
"""Initializes the package"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

storage = FileStorage()

storage.reload()
