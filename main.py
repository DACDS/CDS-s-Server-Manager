#IMPORTS
import re
import os
import discord
from discord import app_commands
import sys
import asyncio
from pydactyl import PterodactylClient
import json

#FILE_SETUP
os.makedirs("/usr/src/app/data/server", exist_ok=True) #Makes server directory
def FILE_SETUP(path,purpose):#Checks if file (path) exists if not creates it and writes (purpose) inside it
    isExist = os.path.isfile(path)
    if isExist == False:
        file1 = open(path, "w")
        file1.write(purpose)
        file1.close()

FILE_SETUP("/usr/src/app/data/token.txt","Insert discord token here")
FILE_SETUP("/usr/src/app/data/api.txt","Insert petrodacly api here")
FILE_SETUP("/usr/src/app/data/link.txt","Insert petrodacly link here")

#KEY-GET
file1 = os.open("/usr/src/app/data/token.txt",os.O_RDONLY)
token = os.read(file1,100)
token = token.decode("utf-8")
os.close(file1)
file1 = os.open("/usr/src/app/data/api.txt",os.O_RDONLY)
api = os.read(file1,100)
api = api.decode("utf-8")
os.close(file1)
file1 = os.open("/usr/src/app/data/link.txt",os.O_RDONLY)
link = os.read(file1,100)
link = link.decode("utf-8")
os.close(file1)
api = PterodactylClient(link, api)

#SETTINGS_MAKE
if os.path.isfile("/usr/src/app/data/config.json"):
    pass
else:
    print("No prexisting config file found attemping to create")
    deft_config = {
        "README": "config file (delete this file reset)",
        "force_run": (False)
    }
    with open("/usr/src/app/data/config.json", "w", encoding="utf-8") as file:
        json.dump(deft_config, file, indent=4)
#SETTINGS_GET
with open("/usr/src/app/data/config.json", "r", encoding="utf-8") as file:
    jsondata = json.load(file)
forcerun = (jsondata["force_run"])
#DEBUG
if forcerun == False:
    async def token_debug():
        async with discord.Client(intents=discord.Intents.default()) as client:
            try:
                await client.login(token)
                print("Token is valid.")
            except Exception as e:
                print(e)
                sys.exit()
    asyncio.run(token_debug())
    print("Discord login sucess")
    try:
        servers = api.client.servers.list_servers()
        print("Petro login sucess")
    except Exception as e:
                print(e)
                sys.exit()
else:
    print("Force run enabled, skiping debug step")
#COMMAND SETUP
# class MyClient(discord.Client):
#     def __init__(self):
#         super().__init__(intents=discord.Intents.default())
#         self.tree = app_commands.CommandTree(self)
