import discord
from discord.ext import commands
import json
from .commands import button_callback
from .commands import start_nudes, start_videos

def on_ready(bot):
    @bot.event
    async def on_ready():
        print(f'Connecté en tant que {bot.user}!')


### BOUTONS
########### NUDES 

async def start_nudes(interaction):
    embed = discord.Embed(
        title="Accès au menu", 
        description="Veuillez rentrer une clé pour accéder au menu.", 
        color=0xE4022C
        
        )
    embed.set_author(name="Lili Rigel BOT", url="https://aizufans-agency.fr", icon_url="https://cdn.discordapp.com/attachments/1287722220499505207/1287722403882860564/433422822_7357960910946904_3542919409976340496_n.jpg?ex=67065af1&is=67050971&hm=9c2e679fabd80c174888783c9151df79a8c699d8d0e923c3e71d2159186af868&")
    embed.set_footer(text="Powered by Alex Blond & Raphael Porras")
    embed.add_field(name="Exemple", value="*LILIRGL-KEY-NUDES-12345678*", inline=False)
    embed.add_field(name="Clé", value="Rentrer votre clé dessous", inline=False)
    await interaction.response.send_message(embed=embed)

########### VIDEOS

async def start_videos(interaction):
    embed = discord.Embed(
        title="Accès au menu", 
        description="Veuillez rentrer une clé pour accéder au menu.", 
        color=0xE4022C
        )
    embed.set_author(name="Lili Rigel BOT", url="https://aizufans-agency.fr", icon_url="https://cdn.discordapp.com/attachments/1287722220499505207/1287722403882860564/433422822_7357960910946904_3542919409976340496_n.jpg?ex=67065af1&is=67050971&hm=9c2e679fabd80c174888783c9151df79a8c699d8d0e923c3e71d2159186af868&")
    embed.set_footer(text="Powered by Alex Blond & Raphael Porras")
    embed.add_field(name="Exemple", value="*LILIRGL-KEY-VIDEOS-12345678*", inline=False)
    embed.add_field(name="Clé", value="Rentrer votre clé dessous", inline=False)
    await interaction.response.send_message(embed=embed)

########### VIDEOS X5

async def start_videos_x5(interaction):
    embed = discord.Embed(
        title="Accès au menu", 
        description="Veuillez rentrer une clé pour accéder au menu.", 
        color=0xE4022C
        )
    embed.set_author(name="Lili Rigel BOT", url="https://aizufans-agency.fr", icon_url="https://cdn.discordapp.com/attachments/1287722220499505207/1287722403882860564/433422822_7357960910946904_3542919409976340496_n.jpg?ex=67065af1&is=67050971&hm=9c2e679fabd80c174888783c9151df79a8c699d8d0e923c3e71d2159186af868&")
    embed.set_footer(text="Powered by Alex Blond & Raphael Porras")
    embed.add_field(name="Exemple", value="*LILIRGL-KEY-VIDEOSx5-12345678*", inline=False)
    embed.add_field(name="Clé", value="Rentrer votre clé dessous", inline=False)
    await interaction.response.send_message(embed=embed)

########### NUDES X5
async def start_nudes_x5(interaction):
    embed = discord.Embed(
        title="Accès au menu", 
        description="Veuillez rentrer une clé pour accéder au menu.", 
        color=0xE4022C
        )
    embed.set_author(name="Lili Rigel BOT", url="https://aizufans-agency.fr", icon_url="https://cdn.discordapp.com/attachments/1287722220499505207/1287722403882860564/433422822_7357960910946904_3542919409976340496_n.jpg?ex=67065af1&is=67050971&hm=9c2e679fabd80c174888783c9151df79a8c699d8d0e923c3e71d2159186af868&")
    embed.set_footer(text="Powered by Alex Blond & Raphael Porras")
    embed.add_field(name="Exemple", value="*LILIRGL-KEY-NUDESx5-12345678*", inline=False)
    embed.add_field(name="Clé", value="Rentrer votre clé dessous", inline=False)
    await interaction.response.send_message(embed=embed)

########### NUDES X10
async def start_nudes_x10(interaction):
    embed = discord.Embed(
        title="Accès au menu", 
        description="Veuillez rentrer une clé pour accéder au menu.", 
        color=0xE4022C
        )
    embed.set_author(name="Lili Rigel BOT", url="https://aizufans-agency.fr", icon_url="https://cdn.discordapp.com/attachments/1287722220499505207/1287722403882860564/433422822_7357960910946904_3542919409976340496_n.jpg?ex=67065af1&is=67050971&hm=9c2e679fabd80c174888783c9151df79a8c699d8d0e923c3e71d2159186af868&")
    embed.set_footer(text="Powered by Alex Blond & Raphael Porras")
    embed.add_field(name="Exemple", value="*LILIRGL-KEY-NUDESx10-12345678*", inline=False)
    embed.add_field(name="Clé", value="Rentrer votre clé dessous", inline=False)
    await interaction.response.send_message(embed=embed)

########### VIDEOS X6

async def start_videos_x6(interaction):
    embed = discord.Embed(
        title="Accès au menu", 
        description="Veuillez rentrer une clé pour accéder au menu.", 
        color=0xE4022C
        )
    embed.set_author(name="Lili Rigel BOT", url="https://aizufans-agency.fr", icon_url="https://cdn.discordapp.com/attachments/1287722220499505207/1287722403882860564/433422822_7357960910946904_3542919409976340496_n.jpg?ex=67065af1&is=67050971&hm=9c2e679fabd80c174888783c9151df79a8c699d8d0e923c3e71d2159186af868&")
    embed.set_footer(text="Powered by Alex Blond & Raphael Porras")
    embed.add_field(name="Exemple", value="*LILIRGL-KEY-VIDEOSx6-12345678*", inline=False)
    embed.add_field(name="Clé", value="Rentrer votre clé dessous", inline=False)
    await interaction.response.send_message(embed=embed)

### BOUTONS

async def button_callback(interaction, button_number, category):
    global valid_key
    if valid_key is None:
        await interaction.response.send_message("Veuillez rentrer une clé valide")
    else:
        with open("json/message.json", "r") as f:
            messages = json.load(f)
        await interaction.response.send_message(f"**ICI** ➡: {messages['categories'][category][button_number]['description']} \n ❤**MERCI POUR TON ACHAT** \n *Si besoin d'aide contacte @lili_rgl* \n ✨ **[BOUTIQUE](https://lilirgl.mysellix.io/fr/)**")
        valid_key = None  # Réinitialiser la clé valide après un clic
        await interaction.message.delete()  # Supprimer le message du menu

def on_message(bot):
    @bot.event
    async def on_message(message):
        global valid_key
        # Vérifier si le message est un DM (message privé)
        if isinstance(message.channel, discord.DMChannel):
            if message.author == bot.user:  # Ignore messages sent by the bot itself
                return
            if message.content.lower() == "start":
                ## EMBED
                embed = discord.Embed(
                    title="🤖 MENU", 
                    description="Sélectionnez une option par rapport a votre 🔑 **clé** \n 👀 Pas de **clé** ? vient en acheter **[LIEN BOUTIQUE](https://lilirgl.mysellix.io/fr/)**", 
                    color=0xE4022C)
                embed.set_author(name="Lili Rigel BOT", url="https://aizufans-agency.fr", icon_url="https://cdn.discordapp.com/attachments/1287722220499505207/1287722403882860564/433422822_7357960910946904_3542919409976340496_n.jpg?ex=67065af1&is=67050971&hm=9c2e679fabd80c174888783c9151df79a8c699d8d0e923c3e71d2159186af868&")
                embed.set_image(url="https://media.discordapp.net/attachments/565218193581277209/1291481207196090499/BANNER.png?ex=67062fda&is=6704de5a&hm=f7404bd31b66470e97cbb41f916790f72a6bf7c0bc7705b3cfdf89414badbcf7&=&format=webp&quality=lossless")
                embed.set_footer(text="Powered by Alex Blond & Raphael Porras")
                ## EMBED
                view = discord.ui.View()
                button_nudes = discord.ui.Button(label="📷 Nudes x1", custom_id="nudes_button")
                button_nudes_x5 = discord.ui.Button(label="📷 Nudes x5", custom_id="nudes_button_x5")
                button_nudes_x10 = discord.ui.Button(label="📷 Nudes x10", custom_id="nudes_button_x10") # add
                button_videos = discord.ui.Button(label="🎥 Videos x1", custom_id="videos_button")
                button_videos_x5 = discord.ui.Button(label="🎥 Videox x5", custom_id="videos_button_x5")
                button_videos_x6 = discord.ui.Button(label="🎥 Videox x6", custom_id="videos_button_x6") # add
                button_nudes.callback = lambda interaction: start_nudes(interaction)
                button_nudes_x5.callback = lambda interaction: start_nudes_x5(interaction)
                button_nudes_x10.callback = lambda interaction: start_nudes_x10(interaction)
                button_videos.callback = lambda interaction: start_videos(interaction)
                button_videos_x5.callback = lambda interaction: start_videos_x5(interaction)
                button_videos_x6.callback = lambda interaction: start_videos_x6(interaction)
                view.add_item(button_nudes)
                view.add_item(button_nudes_x5)
                view.add_item(button_nudes_x10)
                view.add_item(button_videos)
                view.add_item(button_videos_x5)
                view.add_item(button_videos_x6)
                await message.channel.send(embed=embed, view=view)
            elif message.content.startswith("LILIRGL-KEY-NUDES-") or message.content.startswith("LILIRGL-KEY-VIDEOS-") or message.content.startswith("LILIRGL-KEY-NUDESx5-") or message.content.startswith("LILIRGL-KEY-VIDEOSx5-") or message.content.startswith("LILIRGL-KEY-VIDEOSx6-") or message.content.startswith("LILIRGL-KEY-NUDESx10-"):
                with open("json/message.json", "r") as f:
                    messages = json.load(f)

                if message.content.startswith("LILIRGL-KEY-NUDES-"):
                    category = "photos"
                    json_file = "main_json/key_img.json"
                elif message.content.startswith("LILIRGL-KEY-VIDEOS-"):
                    category = "videos"
                    json_file = "main_json/key_vid.json"
                elif message.content.startswith("LILIRGL-KEY-VIDEOSx5-"):
                    category = "videosx5"
                    json_file = "main_json/key_vid_x5.json"
                elif message.content.startswith("LILIRGL-KEY-NUDESx5-"):
                    category = "photosx5"
                    json_file = "main_json/key_img_x5.json"
                elif message.content.startswith("LILIRGL-KEY-NUDESx10-"):
                    category = "photosx10"
                    json_file = "main_json/key_img_x10.json"
                elif message.content.startswith("LILIRGL-KEY-VIDEOSx6-"):
                    category = "videosx6"
                    json_file = "main_json/key_vid_x6.json"

                with open(json_file, "r") as f:
                    keys = json.load(f)
                if any(k["key"] == message.content for k in keys):
                    with open(json_file, "w") as f:
                        keys = [k for k in keys if k["key"] != message.content]
                        json.dump(keys, f, indent=4)
                    valid_key = message.content

                    embed = discord.Embed(
                        title="✨ Choix", 
                        description="Cliquez sur un bouton pour recuperer votre produit!", 
                        color=0xE4022C
                        )
                    embed.set_author(name="Lili Rigel BOT", url="https://aizufans-agency.fr", icon_url="https://cdn.discordapp.com/attachments/1287722220499505207/1287722403882860564/433422822_7357960910946904_3542919409976340496_n.jpg?ex=67065af1&is=67050971&hm=9c2e679fabd80c174888783c9151df79a8c699d8d0e923c3e71d2159186af868&")
                    embed.set_footer(text="Powered by Alex Blond & Raphael Porras")
                    view = discord.ui.View()
                    for i, msg in enumerate(messages["categories"][category]):
                        button = discord.ui.Button(label=msg["label"], custom_id=f"button_{i}")
                        button.callback = lambda interaction, i=i, category=category: button_callback(interaction, i, category)
                        view.add_item(button)
                    msg = await message.channel.send(embed=embed, view=view)
                else:
                    await message.channel.send("Clé pas valide")
            else:
                await message.channel.send("Clé pas valide")