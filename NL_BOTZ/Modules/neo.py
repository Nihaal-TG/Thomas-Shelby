#@Aadhi000 #AVR #neo

import asyncio
import os
import math
import time
import requests
from pyrogram import Client, filters

#=====================================================
BOT_START_TIME = time.time()
#=====================================================

@Client.on_message(filters.command("ping"))
async def ping(_, message):
    start_t = time.time()  
    avr = await message.reply_text("•••")  
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    uptime = time.strftime("%Hh | %Mm | %Ss", time.gmtime(time.time() - BOT_START_TIME))   
    await avr.edit(f"ᴄᴜʀʀᴇɴᴛ ʙᴏᴛ sᴛᴀᴛᴜs\n\n‹› ᴘᴏɴɢ! : {time_taken_s:.3f} ms\n‹› ʙᴏᴛ ᴜᴘᴛɪɴᴇ : {uptime}")
    await asyncio.sleep(10)
    await avr.delete()
