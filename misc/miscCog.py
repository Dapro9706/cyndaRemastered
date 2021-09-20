from discord.ext import commands
from .miscWrapper import MiscWrapper


class Misc (commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.API = MiscWrapper ()

    @commands.command (name='test', hidden=True)
    async def test(self, ctx):
        await ctx.send ('test')

    @commands.command (name='joke')
    async def joke(self, ctx):
        await ctx.send (self.API.get ('joke'))

    @commands.command (name='billboard')
    async def joke(self, ctx):
        await ctx.send (self.API.get ('bb'))

    @commands.command (name='insult')
    async def insult(self, ctx, name: str):
        await ctx.send (name + ',\n' + self.API.get ('insult'))
