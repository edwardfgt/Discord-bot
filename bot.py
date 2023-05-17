import os
import discord
from discord import Intents
import responses
from config.config_files import APIkeys

intents = Intents.default()
intents.message_content = True

async def send_message(message, user_message):
    try:
        response = responses.get_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)

        print(f"{username} said: {user_message}")
        await send_message(message, user_message)
    
    client.run(APIkeys.TOKEN)