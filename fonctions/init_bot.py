import discord
from discord.ext import commands

def init_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.dm_messages = True

    bot = commands.Bot(command_prefix="!", intents=intents)
    return bot