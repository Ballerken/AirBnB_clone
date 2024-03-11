#!/usr/bin/python3

"""Creates a unique instance of the FileData model."""

from models.engine.file_data import FileData

storage = FileData()
storage.reload()
