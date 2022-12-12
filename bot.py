import asyncio

import discord
from settings import config
from handler import handler
import time
import datetime

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Ready!")
    asyncio.get_event_loop().create_task(main())


async def main():
    channel = client.get_channel(int(config.dc_channel))  # channel id should be an int

    if not channel:
        print("False")
        return
    while True:
        for mint in config.MINTS:
            query = handler(mint)

            try:
                if query is not None and query[0]:
                    print(query)
                    embed = discord.Embed(title=query[0], description=query[1])
                    embed.set_footer(text="\n\nAegis Royalty Shield by Thor Labs",
                                     icon_url="https://imgur.com/hX4eLTa.png")  # if you like to
                    embed.timestamp = datetime.datetime.utcnow()
                    await channel.send(embed=embed)
                    print("POST", query)
                await asyncio.sleep(2)
                print('******************************')
            except Exception as e:
                print(e)
        print("****************************** LOOP ENDS ******************************")
        await asyncio.sleep(14400)


client.run(config.bot_token)
