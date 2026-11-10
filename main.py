#IMPORTS
import os
import discord
import sys
import asyncio
from pydactyl import PterodactylClient

#FILE_SETUP
os.makedirs("/usr/src/app/data/server", exist_ok=True) #Makes server directory
def FILE_SETUP(path,purpose):#Checks if file (path) exists if not creates it and writes (purpose) inside it
    isExist = os.path.isfile(path)
    if isExist == False:
        file1 = open(path, "w")
        file1.write(purpose)
        file1.close()

FILE_SETUP("/usr/src/app/data/token.json","Insert discord token here")
FILE_SETUP("/usr/src/app/data/api.json","Insert petrodacly api here")
FILE_SETUP("/usr/src/app/data/link.json","Insert petrodacly link here")
FILE_SETUP("/usr/src/app/data/settings.json","[Settings File]")

#FILE-GET
file1 = os.open("/usr/src/app/data/token.json",os.O_RDONLY)
token = os.read(file1,100)
token = token.decode("utf-8")
os.close(file1)
file1 = os.open("/usr/src/app/data/api.json",os.O_RDONLY)
api = os.read(file1,100)
api = api.decode("utf-8")
os.close(file1)
file1 = os.open("/usr/src/app/data/link.json",os.O_RDONLY)
link = os.read(file1,100)
link = link.decode("utf-8")
os.close(file1)
api = PterodactylClient(link, api)

#DEBUG
async def token_debug():
    async with discord.Client(intents=discord.Intents.default()) as client:
        try:
            await client.login(token)
            print("Token is valid.")
        except discord.LoginFailure:
            print("Invalid bot token.")
            sys.exit(1)
        except discord.HTTPException as exc:
            print(f"Discord request failed: {exc}")
            sys.exit(1)
        except Exception as exc:
            print(f"Unknown Discord error: {type(exc).__name__}: {exc}")
            sys.exit(1)
            
asyncio.run(token_debug())
print("Discord login sucess")