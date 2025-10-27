from aiogram import types, Router
from aiogram.filters import CommandStart, Command

from app.services.parser_service import ParserService
from app.utils.formatter import format_ad_message


user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer('start')


@user_private_router.message(Command('latest'))
async def latest(message: types.Message):
    ad = ParserService.get_last_ad()
    text = format_ad_message(ad)
    await message.answer(text)


@user_private_router.message()
async def echo(message: types.Message):
    text = message.text
    if text:
        await message.answer(message.text)
    else:
        await message.answer("I only work with text")