from aiogram import types, Dispatcher
from config import bot
from keyboards.inline_buttons import start_test_keyboard


async def start_questionnaire(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="Are you ready?",
        reply_markup=await start_test_keyboard()
    )


# async def start_yes(call: types.CallbackQuery):
#     await bot.send_message(
#         chat_id=call.message.chat.id,
#         text="LET'S GO!👏"
#     )


async def start_no(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="BYE👋"
    )


def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionnaire,
                                       lambda call: call.data == "start_questionnaire")
    # dp.register_callback_query_handler(start_yes,
    #                                    lambda call: call.data == "start_yes")
    dp.register_callback_query_handler(start_no,
                                       lambda call: call.data == "start_no")
