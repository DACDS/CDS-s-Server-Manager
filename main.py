#IMPORTS
import os
import discord
import sys



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
FILE_SETUP("/usr/src/app/data/settings.json","[Settings File]")

#DEBUG
file1 = os.open("/usr/src/app/data/token.json","os.O_RDONLY")
token = os.read(file1,100)
file1.close()
with discord.Client(intents=discord.Intents.none()) as client:
    try:
        client.login(token)
    except discord.LoginFailure:
        print("Invalid bot token.")
        sys.exit()
    except discord.HTTPException as exc:
        print(f"Discord request failed: {exc}")
        sys.exit()



