#!/usr/bin/python3
"""Import FileStorage and read existing data into `storage` variable"""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
