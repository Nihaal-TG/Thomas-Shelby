#code by @MS_OFFICIALS


from pyrogram import filters, Client as Ms_officials 
from time import time

@Ms_officials.on_message(filters.command("ban"))
async def ban_users(bot, msg):
    user_id = msg.reply_to_message.from_user.id
    chat_id = msg.chat.id
    try:
        await bot.ban_chat_member(chat_id, user_id)
    except:
        pass
    await msg.reply_text("ᴀɴᴏᴛʜᴇʀ ᴏɴᴇ ʙɪᴛᴇs ᴛʜᴇ ᴅᴜsᴛ...!")

@Ms_officials.on_message(filters.command("unban"))
async def unban_users(bot, msg):
    user_id = msg.reply_to_message.from_user.id
    chat_id = msg.chat.id
    try:
        await bot.unban_chat_member(chat_id, user_id)
    except:
        pass
    await msg.reply_text("ഒരു തവണ ഷമിച്ചു ഇനി മേലാ ഇത് ആവർത്തിക്കരുത്")
