import discord
from discord.ext import commands
import json
import os
from dotenv import load_dotenv
from fonctions.init_bot import init_bot
from fonctions.events import on_ready, on_message
from fonctions.commands import start_nudes, start_videos, button_callback
from keep_alive import keep_alive

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

valid_key = None

bot = init_bot()

on_ready(bot)
on_message(bot)

keep_alive()
bot.run(token=token)