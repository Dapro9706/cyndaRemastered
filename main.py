from bot import BOT
from keep_alive import keep_alive
import os

bot = BOT (command_prefix="-")

keep_alive ()
bot.run (os.getenv ('TOKEN'))
