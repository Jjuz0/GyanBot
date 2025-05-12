import disnake
from disnake.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def ping(self, inter):
        await inter.send(f'Задержка бота: {round(self.bot.latency * 1000)} мс')


def setup(bot):
    bot.add_cog(Ping(bot))