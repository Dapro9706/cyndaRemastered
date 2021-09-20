from misc import Misc


def setup(bot):
    cogs = [Misc]
    for i in cogs:
        bot.add_cog (i (bot))
