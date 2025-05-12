import disnake
import os
from disnake.ext import commands
from config import token
import os

intents = disnake.Intents.default()
intents.members = True
bot = commands.Bot(intents=intents)

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")

@bot.event
async def on_ready():
      print(f'Бот: {bot.name} с ID: {bot.id} готов.')

      
bot.run(token)

