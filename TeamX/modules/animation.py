import time
from typing import List

from telegram import Update
from telegram.ext import run_async, CallbackContext

from TeamX import dispatcher
from TeamX.modules.disable import DisableAbleCommandHandler
from TeamX.modules.helper_funcs.chat_status import user_admin

# sleep how many times after each edit in 'love'
EDIT_SLEEP = 1
# edit how many times in 'love'
EDIT_TIMES = 10


# sleep how many times after each edit in 'bombs'
EDIT_SLEEP = 1
# edit how many times in 'bombs'
EDIT_TIMES = 9


# sleep how many times after each edit in 'hack'
EDIT_SLEEP = 1
# edit how many times in 'hack'
EDIT_TIMES = 10


# sleep how many times after each edit in 'earthanimation'
EDIT_SLEEP = 1
# edit how many times in 'earthanimation'
EDIT_TIMES = 18


# sleep how many times after each edit in 'moonanimation'
EDIT_SLEEP = 1
# edit how many times in 'moonanimation'
EDIT_TIMES = 32


# sleep how many times after each edit in 'clockanimation'
EDIT_SLEEP = 1
# edit how many times in 'clockanimation'
EDIT_TIMES = 11


# sleep how many times after each edit in 'blockanimation'
EDIT_SLEEP = 1
# edit how many times in 'blockanimation'
EDIT_TIMES = 18


# sleep how many times after each edit in 'kill'
EDIT_SLEEP = 1
# edit how many times in 'kill'
EDIT_TIMES = 12


kill_you = [
    "Ｆｉｉｉｉｉｒｅ",
    "(　･ิω･ิ)︻デ═一-->",






    "------------------>",
    "------>;(^。^)ノ",
    "(￣ー￣) DED",
    "**Target killed successfully",
]


block_chain = [
    "🟥",
    "🟧",
    "🟨",
    "🟩",
    "🟦",
    "🟪",
    "🟫",
    "⬛",
    "⬜",
    "🟥",
    "🟧",
    "🟨",
    "🟩",
    "🟦",
    "🟪",
    "🟫",
    "⬛",
    "⬜",
]


love_siren = [
    "❤️❤️❤️🧡🧡🧡💚💚💚\n💙💙💙💜💜💜🖤🖤🖤",
    "🖤🖤🖤💜💜💜💙💙💙\n❤️❤️❤️🧡🧡🧡💚💚💚",
    "💛💛💛💙💙💙❤️❤️❤️\n💜💜💜❤️❤️❤️🧡🧡🧡",
    "❤️❤️❤️🧡🧡🧡💚💚💚\n💙💙💙💜💜💜🖤🖤🖤",
    "🖤🖤🖤💜💜💜💙💙💙\n❤️❤️❤️🧡🧡🧡💚💚💚",
    "💛💛💛💙💙💙❤️❤️❤️\n💜💜💜❤️❤️❤️🧡🧡🧡",
    "❤️❤️❤️🧡🧡🧡💚💚💚\n💙💙💙💜💜💜🖤🖤🖤",
    "🖤🖤🖤💜💜💜💙💙💙\n❤️❤️❤️🧡🧡🧡💚💚💚",
    "💛💛💛💙💙💙❤️❤️❤️\n💜💜💜❤️❤️❤️🧡🧡🧡",
]


hack_you = [
    "Looking for WhatsApp databases in targeted person...",
    " User online: True\nTelegram access: True\nRead Storage: True ",
    "Hacking... 20.63%\n[███░░░░░░░░░░░░░░░░░]",
    "Hacking... 86.21%\n[███████████████░░░░░]",
    "Hacking... 93.50%\n[█████████████████░░░]",
    "hacking....  100%\n[████████████████████]",
]


bomb_ettu = [
    "▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️",
    "💣💣💣💣\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️",
    "▪️▪️▪️▪️\n💣💣💣💣\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️",
    "▪️▪️▪️▪️\n▪️▪️▪️▪️\n💣💣💣💣\n▪️▪️▪️▪️\n▪️▪️▪️▪️",
    "▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n💣💣💣💣\n▪️▪️▪️▪️",
    "▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n💣💣💣💣",
    "▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n💥💥💥💥",
    "▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n💥💥💥💥\n💥💥💥💥",
    "▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n😵😵😵😵",
]


moon_ani = [
    "🌗",
    "🌘",
    "🌑",
    "🌒",
    "🌓",
    "🌔",
    "🌕",
    "🌖",
    "🌗",
    "🌘",
    "🌑",
    "🌒",
    "🌓",
    "🌔",
    "🌕",
    "🌖",
    "🌗",
    "🌘",
    "🌑",
    "🌒",
    "🌓",
    "🌔",
    "🌕",
    "🌖",
    "🌗",
    "🌘",
    "🌑",
    "🌒",
    "🌓",
    "🌔",
    "🌕",
    "🌖",
]


clock_ani = ["🕙", "🕘", "🕗", "🕖", "🕕", "🕔", "🕓", "🕒", "🕑", "🕐", "🕛"]


earth_ani = [
    "🌍",
    "🌎",
    "🌏",
    "🌍",
    "🌎",
    "🌏",
    "🌍",
    "🌎",
    "🌏",
    "🌍",
    "🌎",
    "🌏",
    "🌍",
    "🌎",
    "🌏",
    "🌍",
    "🌎",
    "🌏",
]


def blockanimation(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    msg = update.effective_message.reply_text("⬜")
    for x in range(EDIT_TIMES):
        msg.edit_text(block_chain[x % 18])
        time.sleep(EDIT_SLEEP)
    msg.edit_text("🟥")

@user_admin
def clockanimation(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    msg = update.effective_message.reply_text("🕙")
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    for x in range(EDIT_TIMES):
        msg.edit_text(clock_ani[x % 11])
        time.sleep(EDIT_SLEEP)
    msg.edit_text("🕚")

@user_admin
def earthanimation(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    msg = update.effective_message.reply_text("🌍")
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    for x in range(EDIT_TIMES):
        msg.edit_text(earth_ani[x % 18])
        time.sleep(EDIT_SLEEP)
    msg.edit_text("🌍")


def moonanimation(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    msg = update.effective_message.reply_text("🌚")
    for x in range(EDIT_TIMES):
        msg.edit_text(moon_ani[x % 32])
        time.sleep(EDIT_SLEEP)
    msg.edit_text("🌙")


def bombs(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    msg = update.effective_message.reply_text("💣")
    for x in range(EDIT_TIMES):
        msg.edit_text(bomb_ettu[x % 9])
        time.sleep(EDIT_SLEEP)
    msg.edit_text("DUAR ...")


def hack(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    msg = update.effective_message.reply_text("Target selected")
    for x in range(EDIT_TIMES):
        msg.edit_text(hack_you[x % 5])
        time.sleep(EDIT_SLEEP)
    msg.edit_text("successful hacked all data send on my Database")


def love(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    msg = update.effective_message.reply_text("❣️")
    for x in range(EDIT_TIMES):
        msg.edit_text(love_siren[x % 5])
        time.sleep(EDIT_SLEEP)
    msg.edit_text("True Love💞")


def kill(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    msg = update.effective_message.reply_text("🔫")
    for x in range(EDIT_TIMES):
        msg.edit_text(kill_you[x % 12])
        time.sleep(EDIT_SLEEP)
    msg.edit_text("⚰")



KILL_HANDLER = DisableAbleCommandHandler("kill", kill, run_async=True)
LOVE_HANDLER = DisableAbleCommandHandler("love", love, run_async=True)
HACK_HANDLER = DisableAbleCommandHandler("hack", hack, run_async=True)
BOMBS_HANDLER = DisableAbleCommandHandler("bombs", bombs, run_async=True)
MOONANIMATION_HANDLER = DisableAbleCommandHandler("moon", moonanimation, run_async=True)
CLOCKANIMATION_HANDLER = DisableAbleCommandHandler(
    "clock", clockanimation, run_async=True
)
BLOCKANIMATION_HANDLER = DisableAbleCommandHandler(
    "block", blockanimation, run_async=True
)
EARTHANIMATION_HANDLER = DisableAbleCommandHandler(
    "earth", earthanimation, run_async=True
)
dispatcher.add_handler(KILL_HANDLER)
dispatcher.add_handler(LOVE_HANDLER)
dispatcher.add_handler(HACK_HANDLER)
dispatcher.add_handler(BOMBS_HANDLER)
dispatcher.add_handler(EARTHANIMATION_HANDLER)
dispatcher.add_handler(MOONANIMATION_HANDLER)
dispatcher.add_handler(CLOCKANIMATION_HANDLER)
dispatcher.add_handler(BLOCKANIMATION_HANDLER)

__mod_name__ = "Animation"
__command_list__ = [
    "love",
    "hack",
    "bombs",
    "moonanimation",
    "clockanimation",
    "earthanimation",
    "blockanimation",
    "kill",
]
__handlers__ = [
    LOVE_HANDLER,
    HACK_HANDLER,
    BOMBS_HANDLER,
    MOONANIMATION_HANDLER,
    CLOCKANIMATION_HANDLER,
    EARTHANIMATION_HANDLER,
    BLOCKANIMATION_HANDLER,
    KILL_HANDLER,
]
