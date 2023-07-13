from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from TeamX import pbot
from TeamX.utils.errors import capture_err
from TeamX.utils.functions import make_carbon


@pbot.on_message(filters.command("carbon"))
@capture_err
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    if not message.reply_to_message.text:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    m = await message.reply_text("`Preparing Carbon`")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("`Uploading`")
    await pbot.send_photo(message.chat.id, carbon)
    await m.delete()
    carbon.close()


MEMEK = "https://telegra.ph/file/57d58f92003ae6a82e2b0.jpg"

@pbot.on_message(filters.command("repo"))
async def repo(_, message):
    await message.reply_photo(
        photo=MEMEK,
        caption=f"""✨ **Hey I'm Kaguya** ✨ 

**Oᴡɴᴇʀ ʀᴇᴘᴏ : [Zoro](https://t.me/Aceladi)**
╔═══════════════╗
┣× ʀᴇᴘᴏ ɪs ᴘʀɪᴠᴀᴛᴇ
┣× ᴏᴡɴᴇʀ ɪs ʜᴀʀᴀᴍɪ 
┣× ʏᴏᴜ ᴄᴀɴ'ᴛ ɢᴇᴛ ɪᴛ 
┣× sᴏ ᴋɪɴᴅʟʏ ғᴜᴄᴋ ᴏғғ
╚═══════════════╝

**Create your own with click button bellow.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Repo", url="https://t.me/Aceladi"), 
                    InlineKeyboardButton(
                        "Support", url="https://t.me/NexusXSupport")
                ]
            ]
        )
    )
