from pyrogram import Client
from datetime import datetime
a = 2719576
b = "ab88e6ee1be33f53db445baf874e1c74"
c = 
d =
e = 
PRO = 1678331806
pepe = Client(c, api_id=a, api_hash=b)
app = Client(d, api_id=a, api_hash=b)
xd = Client(e, api_id=a, api_hash=b)
@pepe.on_message(filters.command("ping") & filters.user(PRO))
@bot.on_message(filters.command("ping") & filters.user(PRO))
@xd.on_message(filters.command("ping") & filters.user(PRO))
async def ping_(_, message):
    start = datetime.now()
    response = await message.reply("`>> Pong!`")
    end = datetime.now()
    resp = (end - start).microseconds / 1000
    await message.reply(f"**>> Pong!**\n`⚡{resp} ms`")



