from pyrogram import Client
from datetime import datetime
a = 2719576
b = "ab88e6ee1be33f53db445baf874e1c74"
c = "AQA4rcw5LQvVi1nKPrFAYgko589S2vhRs9s5F0dno1oGYLJ93pbVEzNhEf-M5ZGtRwQme0N-0JsK88_3JyTTwm3GyeMCQ81JW9gzR-6TY_gNOdWDosL8AcTfKI4gU7z6BaYiKO8x8BRlotUVZu4SxQZixaGLnr3IFqvK6AQyl9ASNDTqAVaYWHfZsohSSKkMgcFrB5SYqBxTJPUyTbOAlUQVztKu4d9U2srUAQdwCz509RfAzvsk46ilduOstz4BcoUnMgKj67yaPuTY9j3DZrsbr3GEgYP7WFrYikCe9A97u0rfui244vp6CxQ5NiSIK3Wil32rT4nM68D0-IgHMit7ZXjosgA"
d = "AQCGHPU5cf0yPtOB5t9XBQde4fjFRhQyGCnY3jW0siyY4p1bVVFyidtFejGDKR-NDlHRseQq3ReCfU6Bcag9hhagRPHpi9PKSbsjYZHH5ohJN-YTsEaywvb_vJFAGz3Kw8cCMFZU-OVI5m4q_FA-5KR4QBMik73M1XCFqlh_b2C10CyXBXxoUDRSW0Q925KW-EsPOUKI2BchLjoaEfOj-0VVy-HSRomgBai8NALwuZAthSKFhao5pX8PKutnU2xycRR6ZW2AaFE579oegfKwF9zZBpc9Bj15ml6HsxXP5gu9QhNBRZ2ihioqbZcxd_zZW-H9rsf1BBV_JrX2L0HVks5hZhFiCgA"
e = "AQB8pHQIKG1loSuQKAo8srcpDm_YUbH9P6YCChitY3M85kWBJmG74fXGA8wnQx-g8qNKmaOiW8fD4VwUb6D4B5h-pctUyRhTaHqrx3M19z8WL3QZ5H1lM4DoVbbEBtyn12wX_tFMs43SthQA37H99T9HURBcycItANcqQrje2LqYTcteD8otSTkuAsO80NdohgSys9BD2eDcHHDKeo5i-3ZPw_2K2B8XqrsVDFSgYpl-sQtkWsg3m8V6-q8UNwnfDY5TvXTsftLwio4lWrxW5q8iQd5iBSpvwsnVHpUlTH2fCkglWKgSk5KcudXWD9tY89RbaiMKiruHjWHeVlju93JpR6qU0QA"
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



app.run()
xd.run()
pepe.run()
