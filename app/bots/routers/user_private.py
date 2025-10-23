from aiogram import types, Router
from aiogram.filters import CommandStart, Command


user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer('start')


@user_private_router.message(Command('latest'))
async def echo(message: types.Message):
    await message.answer('latest ad')


@user_private_router.message()
async def echo(message: types.Message):
    text = message.text
    if text:
        await message.answer(message.text)
    else:
        await message.answer("I only work with text")