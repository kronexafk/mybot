import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, LabeledPrice

API_TOKEN = "7924263054:AAG-i7aWwu1ivhJfLW-CPVS7-71q6LHtJ4g"  # вставь токен от BotFather

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(F.text == "/start")
async def start(message: Message):
    await message.answer("Привет! Напиши /buy чтобы оплатить ⭐️")

@dp.message(F.text == "/buy")
async def buy(message: Message):
    prices = [LabeledPrice(label="Поддержка проекта", amount=20)]
    await message.answer_invoice(
        title="Поддержка проекта",
        description="Оплата 20 ⭐️",
        prices=prices,
        provider_token="",
        payload="support-20",
        currency="XTR",
    )

@dp.message(F.successful_payment)
async def success_payment(message: Message):
    total = message.successful_payment.total_amount
    await message.answer(f"Спасибо за оплату {total} ⭐️!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
