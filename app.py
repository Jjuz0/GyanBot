import disnake
import os
from disnake.ext import commands
from config import token


intents = disnake.Intents.default()
intents.members = True
bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
      print(f'Бот: {bot.user.name} с ID: {bot.user.id} готов.')

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"cogs.{filename[:-3]} загружен.")


bot.run(token)

