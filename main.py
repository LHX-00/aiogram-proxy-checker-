
import logging

from aiogram import Bot, Dispatcher, executor, types










import requests









API_TOKEN = '5565070958:AAGxqag-qTn-KeWp8-xITCDAgAoA0C_5nQ0'

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

    row1 = (
        "📩Ottieni proxy",
        "",
    )
    row2 = (
        "➕Controlla i tuoi proxy",
        "❌Elimina Email",
    )
    row3 = (
      "👤Fai una donazione",
      "🏵Gestisci Bot",
    )
    
    keyboard_markup.row(*(types.KeyboardButton(str) for str in row1))
    # adds buttons as a new row to the existing keyboard
    # the behaviour doesn't depend on row_width attribute

    keyboard_markup.row(*(types.KeyboardButton(text) for text in row2))
    # adds buttons. New rows are formed according to row_width parameter
    keyboard_markup.add(*(types.KeyboardButton(str) for str in row3))
  
    await message.reply("Hi!\nDo you like aiogram?", reply_markup=keyboard_markup)

@dp.message_handler()
async def check_proxy(message: types.Message):
    headers = {
    'Accept': 'application/json',
    }

    params = {
    'host': 'check-host.net',
    'max_nodes': '3',
    }

    response = requests.get('https://check-host.net/check-ping', params=params, headers=headers)
    await message.reply(response, reply_markup=keyboard_markup)



@dp.message_handler()
async def all_msg_handler(message: types.Message):
    button_text = message.text
    logger.debug('The answer is %r', button_text)  

    if button_text == '📩Apri Casella':
        reply_text = "apro la casella"
    elif button_text == '➕Crea Nuovamil':
        reply_text = "Creo una nuova mail"
    else:
        reply_text = "Keep calm...Everything is fine"

    await message.reply(reply_text, reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler()
async def nuova_casella(message: types.Message)
    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
