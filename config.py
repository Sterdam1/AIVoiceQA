from pydantic import Field, BaseModel
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    tg_token: str = Field('tg_token', env="TG_TOKEN")

settings = Settings(_env_file='.env', _env_file_encoding='utf-8')