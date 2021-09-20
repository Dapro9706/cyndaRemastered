from discord import Activity, ActivityType
from discord.ext import commands


class BOT (commands.Bot):
    def __init__(self, *args, **kwargs):
        super ().__init__ (*args, **kwargs)
        self.init_events ()
        self.load_extension ('cog')

    def init_events(self):
        @self.event
        async def on_ready():
            await self.change_presence (activity=Activity (type=ActivityType.listening, name='-help'))
            print ('BOT READY')
