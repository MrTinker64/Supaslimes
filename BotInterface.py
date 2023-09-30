import discord
import os
from secretkey import TOKEN

intents = discord.Intents(messages=True, guilds=True)
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.content.startswith('$bridge'):
        channel = message.channel
        await channel.send("hey dirtbag")

def handle_response(msg) -> str:
    message = message.lower()

client.run(TOKEN)
