import discord
from discord.ext import commands
import json

def start_nudes(bot):
    @bot.command(name="start_nudes")
    async def start_nudes(ctx):
        embed = discord.Embed(title="Accès au menu", description="Veuillez rentrer une clé pour accéder au menu.", color=0xE4022C)
        embed.add_field(name="Clé", value="Rentrer votre clé dessous", inline=False)
        await ctx.send(embed=embed)

def start_videos(bot):
    @bot.command(name="start_videos")
    async def start_videos(ctx):
        embed = discord.Embed(title="Accès au menu", description="Veuillez rentrer une clé pour accéder au menu.", color=0xE4022C)
        embed.add_field(name="Clé", value="Rentrer votre clé dessous", inline=False)
        await ctx.send(embed=embed)

def button_callback(bot):
    @bot.command(name="button_callback")
    async def button_callback(ctx, button_number, category):
        global valid_key
        if valid_key is None:
            await ctx.send("Veuillez rentrer une clé valide")
        else:
            with open("json/message.json", "r") as f:
                messages = json.load(f)
            await ctx.send(f"Message {button_number}: {messages['categories'][category][button_number]['description']}")
            valid_key = None  # Réinitialiser la clé valide après un clic
            await ctx.message.delete()  # Supprimer le message du menu