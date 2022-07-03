import os

from discord.ext import commands
from mongoengine import *

from mastermode.settings import *

connect(
    MONGODB_DATABASE,
    host=MONGODB_HOST,
    username=MONGODB_USER,
    password=MONGODB_PASSWORD,
    authentication_source="admin",
)

bot = commands.Bot(command_prefix="$")
for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(DISCORD_BOT_TOKEN)
