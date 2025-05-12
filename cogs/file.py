import os
from datetime import datetime
import disnake
from disnake.ext import commands

class BuildInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Показать информацию о сборке")
    async def buildinfo(self, ctx: disnake.ApplicationCommandInteraction):
        # Получаем данные из переменных окружения
        commit_hash = os.getenv("COMMIT_HASH", "unknown")
        commit_date_str = os.getenv("COMMIT_DATE", "unknown")
        
        time_ago = "unknown"

        # Создаем Embed
        embed = disnake.Embed(
            title="Информация о сборке",
            color=disnake.Color.green()
        )
        embed.add_field(name="Версия", value="1.0.0", inline=False)
        embed.add_field(name="Хэш коммита", value=f"`{commit_hash}`", inline=False)
        embed.add_field(name="Дата сборки", value=f"{commit_date_str} ({time_ago})", inline=False)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(BuildInfo(bot))