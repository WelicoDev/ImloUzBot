import logging
from checkword import CheckWords

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6133846999:AAH9m0XxeiP8h813eWU8XIDEAKheJ4cQlEE'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.reply("Assalom aleykum !\nMen ImloUzBot !\nSizga so'zlarni bexato yozishda yordam beraman")
    await message.reply("Uzbek tilida  yozmoqchi bo'lgan so'zingizni kiriting :>> 👉 ")
    
@dp.message_handler(commands='help')
async def send_help(message: types.Message):
    await message.reply("Sizga nima yordam kerak ? :>> ")
    await message.answer("Botdagi kamchiliklar yoki takliflar uchun murojaat qiling @welicodev 👨🏻‍💻")
    await message.answer("Kamchiliklar uchun uzr so'raymiz!")
    
@dp.message_handler()
async def send_imlouz(message: types.Message):
    word = message.text
    result = CheckWords(word)
    
    if result['available']:
        response = f"✅ {word.capitalize()}"
    else:
        response = f"❌ {word.capitalize()}\n"
        for text in result['matches']:
            response+= f"✅ {text.capitalize()}\n"
            
    await message.answer(response)
        
        
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)