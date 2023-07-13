import random
from datetime import datetime
from TeamX import pbot as pgram
from pyrogram import filters
from TeamX.ex_plugins.dbfunctions import get_couple,save_couple

def dt():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    dt_list = dt_string.split(" ")
    return dt_list


def dt_tom():
    a = (
        str(int(dt()[0].split("/")[0]) + 1)
        + "/"
        + dt()[0].split("/")[1]
        + "/"
        + dt()[0].split("/")[2]
    )
    return a

tomorrow = str(dt_tom())
today = str(dt()[0])


CAP = """
**💌 ᴄᴏᴜᴘʟᴇs ᴏғ ᴛʜᴇ ᴅᴀʏ :**\n
{0} + {1} = 💘\n
`ɴᴇᴡ ᴄᴏᴜᴘʟᴇ ᴏғ ᴛʜᴇ ᴅᴀʏ ᴄᴀɴ ʙᴇ ᴄʜᴏsᴇɴ ᴀᴛ 12AM {2}`
"""
COUPLES_PIC = "https://te.legra.ph/file/1a51f3b709f83df326c75.jpg"


@pgram.on_message(filters.command(["couple","couples","shipping"]) & ~filters.private)
async def nibba_nibbi(_, message):    
    try:
        chat_id = message.chat.id
        is_selected = await get_couple(chat_id, today)
        if not is_selected:
            list_of_users = []
            async for i in _.get_chat_members(message.chat.id, limit=50):
                if not i.user.is_bot:
                    list_of_users.append(i.user.id)
            if len(list_of_users) < 2:
                return await message.reply_text("ɴᴏᴛ ᴇɴᴏᴜɢʜ ᴜsᴇʀs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ.")
            c1_id = random.choice(list_of_users)
            c2_id = random.choice(list_of_users)
            while c1_id == c2_id:
                c1_id = random.choice(list_of_users)
            c1_mention = (await _.get_users(c1_id)).mention
            c2_mention = (await _.get_users(c2_id)).mention
            await _.send_photo(message.chat.id,photo=COUPLES_PIC, caption=CAP.format(c1_mention,c2_mention,tomorrow))    
            couple = {"c1_id": c1_id, "c2_id": c2_id}
            await save_couple(chat_id, today, couple)

        elif is_selected:
            c1_id = int(is_selected["c1_id"])
            c2_id = int(is_selected["c2_id"])
            try:              
                c1_mention = (await _.get_users(c1_id)).mention 
                c2_mention = (await _.get_users(c2_id)).mention

                couple_selection_message = f"""**💌 Couple Of The Day :**
{c1_mention} + {c2_mention} = 💘
`ɴᴇᴡ ᴄᴏᴜᴘʟᴇ ᴏf ᴛʜᴇ ᴅᴀʏ ᴄᴀɴ ʙᴇ ᴄʜᴏsᴇɴ ᴀᴛ 12AM {tomorrow}`"""
                await _.send_photo(message.chat.id,photo=COUPLES_PIC,caption=couple_selection_message)
            except :
                couple_selection_message = f"""**💌 Couple Of The Day :**
{c1_id} + {c1_id} = 💘
`New Couple Of The Day Can Be Chosen At 12AM {tomorrow}`"""
                await _.send_photo(message.chat.id,photo=COUPLES_PIC,caption=couple_selection_message)
    except Exception as e:
        print(e)
        await message.reply_text(e)


__help__ = """
Choose couples in your chat

 ❍ /couple *:* Choose 2 users and send their name as couples in your chat.
"""

__mod_name__ = "Cᴏᴜᴘʟᴇ"
