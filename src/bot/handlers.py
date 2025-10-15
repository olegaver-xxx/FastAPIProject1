from aiogram import types
from main import bot, dp
from my_requests import make_post_request
from bot.my_requests import make_post_request, get_user_if_exist
import keyboards as kb


@dp.message()
async def send_user_data(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text=message.text,
    )
    user_id = int(message.from_user.id)
    username = message.from_user.username
    a = await get_user_if_exist(user_id)
    print(a, "<<<<<<<<<<")
    if a:
        print(f"{username} already exists")
    else:
        await make_post_request(username, user_id)
