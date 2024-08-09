import discord
from responses import get_response
from dotenv import load_dotenv
import os

#Getting discord token
load_dotenv()
TOKEN = os.getenv('TOKEN')

#Setting intents(permissions)
intents = discord.Intents.default()
intents.message_content = True


#Creating instance of bot
client = discord.Client(intents = intents)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
@client.event
async def on_message(message):
    #Ignoring messages from the bot
    if message.author == client.user:
        return
    
    #Response to user input
    if message.content.startswith('!'):
        response = get_response(message.content)
        await message.channel.send(response)

#start the bot
client.run(TOKEN)
