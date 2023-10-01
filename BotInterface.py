import discord
from responses import respond
from secretkey import TOKEN

intents = discord.Intents(messages=True, message_content=True)
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user.name} is up and running!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Ignore messages from the bot itself

    print(message.content)

    if message.content.startswith('$bridge'):
        # Send a response message
        response = await respond(message.content)
        await message.channel.send(response)

if __name__ == "__main__":
    client.run(TOKEN)