import discord
from discord.ext import commands
import json
import logging
import asyncio

cogs = [
    "Cogs.EightBall",
    "Cogs.Owner"
]

def log_info(message):
    logging.info(message)
    print(message)

intents = discord.Intents.all()
bot = commands.AutoShardedBot(command_prefix=';', intents=intents)
logging.basicConfig(
    filename="bot.log",
    filemode="w",
    format="$(asctime)s %(message)s",
    level=logging.ERROR,
    datefmt="%d.%b %Y %H:%M:%S")
logging.getLogger().addHandler(logging.StreamHandler())

@bot.event
async def on_ready():
    log_info(f"Logged in as: {bot.user.name} : {str(bot.user.id)}")
    game = discord.Game(name=f"on {str(len(bot.guilds))} guilds!")
    await bot.change_presence(activity=game)

@bot.event
async def on_guild_join(guild):
    log_info(f"Joined server `{guild.name}`!")
    log_info(f"Connected to: {str(len(bot.guilds))} guilds.")
    log_info(f"Connected to: {str(len(bot.users))} users.")
    game = discord.Game(name=f"on {str(len(bot.guilds))} guilds!")
    await bot.change_presence(activity=game)


@bot.event
async def on_guild_remove(guild):
    log_info(f"Left server `{guild.name}`.")
    log_info(f"Connected to: {str(len(bot.guilds))} guilds.")
    log_info(f"Connected to: {str(len(bot.users))} users.")
    game = discord.Game(name=f"on {str(len(bot.guilds))} guilds!")
    await bot.change_presence(activity=game)

async def main():
    for cog in cogs:
        try:
            await bot.load_extension(cog)
            log_info(f"Loaded {cog}")
        except Exception as e:
            log_info("Failed to load " + cog + ": " + str(e))
    await bot.start(json.load(open("json/config.json"))["token"])

if __name__ == "__main__":
    asyncio.run(main())
