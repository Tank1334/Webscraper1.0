from check import tof
import discord
from discord.ext import tasks
from discord.ext.commands import Bot
from time import sleep


client = Bot(command_prefix = '!')


@tasks.loop(hours=1.0)
async def timed_check():
  channel = client.get_channel(790412745911828490)
  #await channel.send(tof())
  if tof() == "In stock.":
    await channel.send("@everyone")
  await channel.send(tof())
    

@client.event
async def on_ready():
  print('bot is up ayyyyyyyyyyyyyyyyyyyy')
  timed_check.start()

@client.command()
async def check(ctx):
  if ctx.message.author == client.user:
    return
  await ctx.send(tof())


client.run('DISCORDID')

#ping either @everyone or <@437622065932140546>
#
#make it send every like 3600 seconds
#
