import time 
import asyncio
from TeamX import pbot as app , DEV_USERS , SUPPORT_CHAT
from pyrogram import filters
from io import BytesIO
from pyrogram.enums import MessageEntityType
from TeamX.modules.sql.users_sql import get_user_com_chats
from pyrogram.errors import Unauthorized, FloodWait 
from TeamX.gbans_db import *

async def get_id_reason_or_rank(message,sender_chat=False):
    args = message.text.strip().split()
    text = message.text
    user = None
    reason = None
    replied = message.reply_to_message
    if replied:
                
        if not replied.from_user:
            if (
                    replied.sender_chat
                    and replied.sender_chat != message.chat.id
                    and sender_chat
            ):
                id_ = replied.sender_chat.id
            else:
                return None, None
        else:
            id_ = replied.from_user.id

        if len(args) < 2:
            reason = None
        else:
            reason = text.split(None, 1)[1]
        return id_, reason
    
    if len(args) == 2:
        user = text.split(None, 1)[1]
        return await get_user_id(message, user), None

    if len(args) > 2:
        user, reason = text.split(None, 2)[1:]
        return await get_user_id(message, user), reason

    return user, reason

async def extract_user_id(message):    
    return (await get_id_reason_or_rank(message))[0]


@app.on_message(filters.command("gban"))
async def _gban(_, message):
    if message.from_user.id not in DEV_USERS:
        return await message.reply_text("**You Don't Have Access To This Command.**")
    user_id,reason = await get_id_reason_or_rank(message)
    from_user = message.from_user
    if not user_id:
        return await message.reply_text("**Specify An User.**")    
    if not reason:
        return await message.reply_text("**Provide A Reason.**")
    if user_id in DEV_USERS:
        return await message.reply_text("**This Is A Developer**")
    user = await _.get_users(user_id)
    start_time = time.time()
    chats = get_user_num_chats(user_id)
    msg = await message.reply(f"**Initialising Gban On User ID :** `{user_id}`\n**Kicking Out From {chats} Chats**")
    await add_gban_user(user_id,reason)
    number_of_chats = 0
    for chat in chats:
        try:
            await _.ban_chat_member(chat, user_id)
            number_of_chats += 1
            await asyncio.sleep(1)
        except FloodWait as e:
            await asyncio.sleep(e.value)
        except Exception:
            pass
    try:
        await _.send_message(user_id,f"**You Have been Gbanned By {from_user.mention}\nYou Can Appeal This Gban From @{SUPPORT_CHAT}**")            
    except Unauthorized:
        pass
    gban_time = get_readable_time((time.time() - start_time))
    await msg.edit(f"**♠ Global Ban ♠\n• Banned : {user.mention}\n• Chats :** `{number_of_chats}`")
    
    
@app.on_message(filters.command("ungban"))
async def _ungban(_, message):
    if message.from_user.id not in DEV_USERS:
        return await message.reply_text("**You Don't Have Access To This Command.**")
    user_id = await extract_user_id(message)
    if not user_id:
        return await message.reply_text("**Specify An User.**")    
    is_gbanned = await is_gbanned_user(user_id)
    if not is_gbanned:
        return await message.reply_text("**This User Isn't Gbanned.**")    
    await remove_gban_user(user_id)
    start_time = time.time()
    chats = get_user_num_chats(user_id)
    number_of_chats = 0
    for chat in chats:
        try:
            await _.unban_chat_member(chat, user_id)
            number_of_chats += 1
            await asyncio.sleep(1)
        except FloodWait as e:
            await asyncio.sleep(e.value)
        except Exception:
            pass   
    ungban_time = get_readable_time((time.time() - start_time))
    await message.reply_text(f"**Removed Global Ban From User ID :** `{user_id}`")
    
@app.on_message(filters.command("gbanlist"))
async def _gbanlist(_, message):
    if message.from_user.id not in DEV_USERS:
        return await message.reply_text("**You Don't Have Access To This Command.**")
    gbanlist = await get_gbans_list()
    if not gbanlist:
        return await message.reply_text("**There Is No Gbannned Users.**")
    msg = "**♠ Global Ban List ♠\n**"
    for i in gbanlist:
        user = await _.get_users(int(i))
        msg += f"• {user.mention} - {user.id}\n"
    with BytesIO(str.encode(msg)) as output:
        output.name = "gbanlist.txt"
        await message.reply_document(            
            document = output,
            caption="**Gban List.**")
