import os
import shutil
from pyrogram import Client, filters
from telegraph import upload_file
from info import TMP_DOWNLOAD_DIRECTORY
from NL_BOTZ.helper_functions.cust_p_filters import f_onw_fliter
from NL_BOTZ.helper_functions.get_file_id import get_file_id


@Client.on_message(
    filters.command("telegraph") &
    f_onw_fliter
)
async def telegraph(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply_text("𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝙿𝙷𝙾𝚃𝙾 𝙾𝚁 𝚅𝙸𝙳𝙴𝙾 𝚄𝙽𝙳𝙴𝚁 𝟻𝙼𝙱.")
        return
    file_info = get_file_id(replied)
    if not file_info:
        await message.reply_text("⚠️ 𝚂𝙾𝚁𝚁𝚈 ! 𝙽𝙾𝚃 𝚂𝚄𝙿𝙿𝙾𝚁𝚃𝙸𝙽𝙶 ⚠️")
        return
    _t = os.path.join(
        TMP_DOWNLOAD_DIRECTORY,
        str(replied.message_id)
    )
    if not os.path.isdir(_t):
        os.makedirs(_t)
    _t += "/"
    download_location = await replied.download(
        _t
    )
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply_text(message, text=document)
    else:
        await message.reply(
            f"Link :- <code>https://telegra.ph{response[0]}</code>",
            disable_web_page_preview=True
        )
    finally:
        shutil.rmtree(
            _t,
            ignore_errors=True
        )
