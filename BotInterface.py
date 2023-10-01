import discord
import responses
import os
from secretkey import TOKEN

intents = discord.Intents(messages=True)
client = discord.Client(intents=intents)

@client.event
async def discordPrint(message):
    # send message to user
    await message.channel.send(f"{await react_to(message.content)}")

async def react_to(message):
    return(responses.respond(message))

def run_bridgy_boi():
    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print(f'{client} is up and running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return  # Ignore messages from the bot itself
        print(message.content)

        if message.content.startswith('$bridge'):
            # Send a response message
            await message.channel.send(f"{await react_to(message.content)}")


    client.run(TOKEN)

run_bridgy_boi()

