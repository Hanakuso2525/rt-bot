# RT

from ujson import load
import rtutil


print("Now loading...")


bot = rtutil.RTShardFrameWork()


with open("data.json", "r") as f:
    bot.data = load(f)


@bot.event
async def on_ready():
    print("Connected")


print("Connecting...")
bot.run(bot.data["token"])
