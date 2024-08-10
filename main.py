import discord
from responses import get_response
from dotenv import load_dotenv
import os

# #Getting discord token
# load_dotenv()
# TOKEN = os.getenv('TOKEN')

# #Setting intents(permissions)
# intents = discord.Intents.default()
# intents.message_content = True


# #Creating instance of bot
# client = discord.Client(intents = intents)


# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')
    
# @client.event
# async def on_message(message):
#     #Ignoring messages from the bot
#     if message.author == client.user:
#         return
    
#     #Response to user input
#     if message.content.startswith('!'):
#         response = get_response(message.content)
#         await message.channel.send(response)

# #start the bot
# client.run(TOKEN)

#Creating the main class for the bot
class WorkoutBud(discord.Client):
    def __init__(self, **options):
        #Initialize the parent class with **options
        super().__init__(**options)

        #Getting discord token
        load_dotenv()
        self.token = os.getenv('TOKEN')

    #Functions to run when bot is ready
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    #Functions to run when a message is sent
    async def on_message(self, message):
        #Ignoring messages from the bot
        if message.author == self.user:
            return
        
        #Response to user input
        if message.content.startswith('!'):
            response = get_response(message.content)
            await message.channel.send(response)
    
    #Function to start the bot
    def run(self):
        super().run(self.token)

#main loop to keep bot running
if __name__ == "__main__":
    #Using **options to set intents and status here
    bot = WorkoutBud(intents = discord.Intents.default(), status = discord.Status.idle)
    bot.run()