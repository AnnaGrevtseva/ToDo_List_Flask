"""Module for settings"""
from pydantic import BaseSettings


# pylint: disable=too-few-public-methods
class Settings(BaseSettings):
    """Save settings parameters"""

    host_url: str = 'http://127.0.0.1:5000'
    database_path: str = 'sqlite:///todo.db'
    track_modifications: bool = False


settings = Settings()
