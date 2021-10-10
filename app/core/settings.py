from typing import Tuple
from pydantic import BaseSettings


class Settings(BaseSettings):
    telegram_api_key: str
    admin_ids: Tuple[int, ...]
    sheet_title: str = 'Курсы по Питону'

    class Config:
        case_sensitive = False
        env_file = 'creds/.env'
        env_file_encoding = 'utf-8'
