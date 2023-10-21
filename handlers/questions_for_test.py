from aiogram import types, Dispatcher
from config import bot
from keyboards import answers_inline_buttons


async def question1(call: types.CallbackQuery):
    await call.answer("LET'S GO!!")
    await bot.send_message(chat_id=call.message.chat.id,
                           text='1)Do you work here?',
                           reply_markup=await answers_inline_buttons.answer_1())


async def question2(call: types.CallbackQuery):
    await call.answer('The next question!')
    await bot.send_message(chat_id=call.message.chat.id,
                           text='2) Who do you ____ with?',
                           reply_markup=await answers_inline_buttons.answer_2())


async def question3(call: types.CallbackQuery):
    await call.answer('The 3 question!')
    await bot.send_message(chat_id=call.message.chat.id,
                           text='3) ___ any shops near here?',
                           reply_markup=await answers_inline_buttons.answer_3())


async def question4(call: types.CallbackQuery):
    await call.answer('The 4 question!')
    await bot.send_message(chat_id=call.message.chat.id,
                           text='4)We live in ___ USA ',
                           reply_markup=await answers_inline_buttons.answer_4())


def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(question1,
                                       lambda call: call.data == "start_yes")
    dp.register_callback_query_handler(question2,
                                       lambda call: call.data == 'd1_button'
                                                    or call.data == "c1_button"
                                                    or call.data == "b1_button"
                                                    or call.data == "a1_button")
    dp.register_callback_query_handler(question3,
                                       lambda call: call.data == "a3_button"
                                                    or call.data == "b3_button"
                                                    or call.data == "c3_button"
                                                    or call.data == "d3_button")
    dp.register_callback_query_handler(question4,
                                       lambda call: call.data == "a4_button"
                                                    or call.data == "b4_button"
                                                    or call.data == "c4_button"
                                                    or call.data == "d4_button")
