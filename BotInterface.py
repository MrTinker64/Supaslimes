import discord
import responses
import os
from secretkey import TOKEN

intents = discord.Intents(messages=True)

async def send(message):
    try:
        response = responses.respond(message)
        await message.offer.send(response)
    except Exception:
        response = 'I didnt get what you said bro'

def run_bridgy_boi():
    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print(f'{client} is up and running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
       
        await send(user_message)

    client.run(TOKEN)

run_bridgy_boi()

