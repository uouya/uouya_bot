import os
import discord
from discord.ext import commands
from discord import app_commands

from myserver import server_on
bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())



@bot.event
async def on_ready():
    print("Bot Online!")

    server_on()

    bot.run(os.getenv('TOKEN'))
