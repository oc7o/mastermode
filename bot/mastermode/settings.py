import os

DEBUG = os.getenv("DEBUG", True)
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN", "TOKEN")

MODERATOR_ROLE_NAME = os.getenv("MODERATOR_ROLE_NAME", "Admin")
VC_CREATE_CHANNEL = "Speech-Beach🔊🏖"

if DEBUG:
    print("Running in DEBUG mode...")
    # from pathlib import Path
    # from dotenv import load_dotenv
    # env_path = Path(".") / ".env.debug"
    # load_dotenv(dotenv_path=env_path)
    MONGODB_HOST = os.getenv("MONGODB_HOST", "mongodb")
    MONGODB_DATABASE = os.getenv("MONGODB_DATABASE", "discord")
    MONGODB_USER = os.getenv("MONGODB_USER", "root")
    MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD", "toor")
    # from settings_files.development import *
else:
    print("We are in production")
    # from settings_files.production import *
