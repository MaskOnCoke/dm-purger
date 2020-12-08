import asyncio # ignore all the imports
import datetime
import functools
import io
import json
import os
import random
import re
import string
import time
import ctypes
from os import system
import aiohttp
import colorama
import discord
import requests
from colorama import Fore
from discord.ext import commands
from discord.utils import get

from colorama import Fore
from discord.ext import commands
from discord.utils import get


os.system('cls')

token = "TOKEN-HERE"

client = discord.Client()
client = commands.Bot(command_prefix="$", self_bot=True)
client.remove_command('help')
ctypes.windll.kernel32.SetConsoleTitleW(f'Message purger')


@client.event
async def on_connect():
    print("ready")
                                                 
@client.command()
async def purge(ctx, limit: int=None):
    async for message in ctx.message.channel.history(limit=None).filter(lambda m: m.author == client.user):
            try:
                await message.delete()
            except:
                pass 




try:
    client.run(token, reconnect=True, bot=False)
except Exception:
    pass
