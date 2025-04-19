import discord
from discord.ext import commands
from discord import app_commands

from myserver import server_on
bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

TOKEN = 'MTM2Mjg1OTU1NTMxODUzNDE1NA.GSRTtN.TMQmkp99zV9L5xl3lr5PrXJwthuxmIQaLO1jTI'

@bot.event
async def on_ready():
    print("Bot Online!")

    server_on()

    bot.run(TOKEN)