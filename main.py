import discord
from discord.ext import commands
import music

client = commands.Bot(command_prefix = '?', intents=discord.Intetns.all())

cogs = [music]
for i in range(len(cogs)):
  cogs[i].setup(client)

client.run("OTkyNDkxNDkxMTY1NDg3MTY0.GiJESI._rK-JpOSW4uCQM-7tM9u2c5-v7e-_wmtsdFo7c")