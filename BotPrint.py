import discord
import os
from secretkey import TOKEN

intents = discord.Intents(messages=True)
client = discord.Client(intents=intents)

intents.message_content = True

@client.event
async def discordPrint(message):
    # send message to user
    await message.channel.send(message.content)