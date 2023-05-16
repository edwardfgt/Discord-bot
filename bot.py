import os
import discord
import responses
from config.config_files import APIkeys


async def send_message(message, user_message):
    try:
        response = response.handle_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    client = discord.CLIENT()

    @client.event
    async def on_ready():
        print(f"{client.user} is now running")
    
    client.run(APIkeys.TOKEN)