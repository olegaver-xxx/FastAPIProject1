from aiogram.types import (
    ReplyKeyboardRemove,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message,
)
from aiogram import Router, F
from aiogram.filters import Command
from poetry.core.masonry.builders import builder

from bot.my_requests import get_res_list

router = Router()

from aiogram.utils.keyboard import InlineKeyboardBuilder

resources_list = ["res1", "res2", "res3", "res4", "res5", "res6"]


def get_keyboard_builder():
    get_res_list()
    builder = InlineKeyboardBuilder()

    for index, resource in enumerate(resources_list):
        builder.button(text=resource, callback_data=("res_num_" + str(index)))
        print("res_num_" + str(index))
    builder.adjust(2, 2)

    return builder.as_markup()


@router.message(Command("select"))
async def menu_handler(message: Message):
    keyboard = get_keyboard_builder()
    await message.answer("choise", reply_markup=keyboard)
