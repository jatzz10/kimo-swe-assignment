from pydantic import BaseSettings


class Settings(BaseSettings):
    mongo_uri: str = 'mongodb://mongo:27017'
    mongo_db: str = 'courses'

    class Config:
        env_prefix = 'COURSES_'