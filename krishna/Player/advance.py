import os
import asyncio
import sys
import git
import heroku3
from krishna.main import BOT
from config import OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, ALIVE_IMG as krishna_PIC
from telethon.tl.functions.users import GetFullUserRequest
# alive Pic By Default It's Will Show Our
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
hl = '/'
deadlyversion = 'Spambot0.10'

  

DEADLY = "โฏ ๐๐ฎ๐ฌ๐ข๐+๐๐๐ข๐ ๐๐ฉ๐๐ฆ ๐๐จ๐ญ โฏ\n\n"
DEADLY += f"โโโโโโโโโโโโโโโโโโโ\n"
DEADLY += f"โข **แดสแดสแดษด แด แดสsษชแดษด** : `3.10.1`\n"
DEADLY += f"โข **แดแดสแดแดสแดษด แด แดสsษชแดษด** : `{version.__version__}`\n"
DEADLY += f"โข **vแดสsษชแดษด**  : `{deadlyversion}`\n"
DEADLY += f"โโโโโโโโโโโโโโโโโโโ\n\n"   

                                  
@BOT.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event):
     await BOT.send_file(event.chat_id,
                                  krishna_PIC,
                                  caption=DEADLY,
                                  buttons=[
        [
        Button.url("แดสแดษดษดแดส", "https://t.me/DC_LOGS"),
        Button.url("sแดแดแดแดสแด", "https://t.me/DC_Kurukshethra")
        ],
        ]
        )
    
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@BOT.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"๐ ๐ตโ๐ดโ๐ณโ๐ฌโ!\n\nโก๏ธ `{ms}` ๐บ๐ โก๏ธ")
        
        

