from bot import BOT
import os

bot = BOT (command_prefix="-")
bot.run (os.getenv ('TOKEN'))
