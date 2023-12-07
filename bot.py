# from aiogram import Bot, Dispatcher, types, filters
# import asyncio
#
# token = '6980903450:AAFaB7nf27cfLLZsZ5ULlBiTzsxlc_e-aIE'
# bot = Bot(token)
# dp = Dispatcher()
#
# main_channel_id = -1001645112994
# forward_channel_ids = ['-1001970786759', '-1001957087469', '-1001859188029', '-1001731290697', '-1001883118075', '-1001560203968', '-1001807942156', '-1001515515473', '-1002092804390', '-1001906584657']
#
# @dp.channel_post()
# async def handle_channel_post(message: types.Message):
#     if message.chat.id == main_channel_id:
#         for channel_id in forward_channel_ids:
#             await message.forward(chat_id=channel_id)
#
#
# async def main():
#     await dp.start_polling(bot)
#
# asyncio.run(main())


from aiogram import Bot, Dispatcher, types, filters
import asyncio

token = '6980903450:AAFaB7nf27cfLLZsZ5ULlBiTzsxlc_e-aIE'
bot = Bot(token)
dp = Dispatcher()


# main_channel_id = -1001645112994
# forward_channel_ids = ['-1001970786759', '-1001957087469', '-1001859188029', '-1001731290697', '-1001883118075', '-1001560203968', '-1001807942156', '-1001515515473', '-1002092804390', '-1001906584657']

main_channel_id = -1001981393451
forward_channel_ids = ['-1001839188139', '-1001510405331']

@dp.channel_post()
async def handle_channel_post(message: types.Message):
    if message.chat.id == main_channel_id:
        for channel_id in forward_channel_ids:
            await message.forward(chat_id=channel_id)

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
