import discord
import os
import dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('MTE1NzcyNDY2NzMyNzU1MzY4Ng.GpAVLD.sKXn_29n700ELWV9tcVmTUOIdR6Jz-S0E-1Wdo')

intents = discord.Intents(messages=True, guilds=True)



bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_message(message):
    if message.content == "$bridge":
        await message.channel.send("hey dirtbag")

bot.run(TOKEN)
