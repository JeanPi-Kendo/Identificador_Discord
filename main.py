import discord
from discord.ext import commands
from model import get_class
import requests
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='#', intents=intents)


@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')


# ----------- PATO RANDOM -----------

def get_duck_image_url():
    url = "https://random-d.uk/api/random"
    res = requests.get(url)
    data = res.json()
    return data["url"]


@bot.command()
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)


# ----------- BARRA DE CONFIANZA -----------

def confidence_bar(confidence):

    total_blocks = 10
    filled_blocks = int(confidence / 10)

    bar = "▰" * filled_blocks + "▱" * (total_blocks - filled_blocks)

    return bar


# ----------- ESTADO DE CONFIANZA -----------

def confidence_status(confidence):

    if confidence >= 80:
        return "🟢", "Estoy muy seguro de esta predicción."

    elif confidence >= 50:
        return "🟡", "Podría ser este personaje, pero no estoy completamente seguro."

    else:
        return "🔴", "No estoy muy seguro del resultado."


# ----------- COMANDO ANIME -----------

@bot.command()
async def check(ctx):

    if ctx.message.attachments:

        for attachment in ctx.message.attachments:

            file_name = attachment.filename

            # guardar imagen
            await attachment.save(f"./{file_name}")

            # analizar imagen
            character, confidence = get_class(
                model_path="./keras_model.h5",
                labels_path="./labels.txt",
                image_path=f"./{file_name}"
            )

            bar = confidence_bar(confidence)

            emoji, message = confidence_status(confidence)

            await ctx.send(
                f"{emoji} **Personaje detectado:** {character}\n"
                f"📊 **Confianza:** {confidence}%\n\n"
                f"{bar}\n\n"
                f"{message}"
            )

            # borrar imagen
            os.remove(f"./{file_name}")

    else:
        await ctx.send("⚠️ Debes subir una imagen.")


# ----------- TOKEN -----------

bot.run("TOKEN")
