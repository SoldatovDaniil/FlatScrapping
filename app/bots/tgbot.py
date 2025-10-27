import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from app.bots.routers.user_private import user_private_router


ALLOWED_UPDATES = ["message, edited_message"]
ROUTERS = [user_private_router]


class TGBot():
    def __init__(self, routers=ROUTERS):
        self.bot = Bot(token=os.getenv("TOKEN"), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
        self.dp = Dispatcher()
        self.setup_routers(routers)


    def setup_routers(self, routers):
        self.dp.include_router(*routers)
    

    async def send_ad_notification(self, ad):
        message = self.format_ad_message(ad)
        user = 123 #добавить поиск usera
        success_count = 0
        try:
            await self.bot.send_message(
                chat_id=user.user_id,
                text=message,
                parse_mode='HTML',
                disable_web_page_preview=True
            )
            success_count += 1
        except Exception as e:
                print(f"Ошибка отправки уведомления пользователю {user.user_id}: {e}")
        
        return success_count


    async def run(self):
        await self.bot.delete_webhook(drop_pending_updates=True)
        await self.dp.start_polling(self.bot, allowed_updates=ALLOWED_UPDATES)
    

    async def stop(self):
        await self.bot.session.close()


if __name__ == '__main__':
    bot = TGBot()
    asyncio.run(bot.run())