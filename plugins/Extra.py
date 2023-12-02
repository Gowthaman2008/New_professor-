import time
import random
import asyncio
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters, enums
from Script import script

CMD = ["/", "."]


@Client.on_message(filters.command("donate", CMD))
async def extra(_, message):
    buttons = [[
            InlineKeyboardButton('✘ ᴄʟᴏsᴇ ✘', callback_data='close_data')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(
            text=(script.DONATE_TXT),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
