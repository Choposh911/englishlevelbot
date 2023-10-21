from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "START TEST ",
        callback_data="start_questionnaire"
    )
    markup.add(questionnaire_button)
    return markup

async def start_test_keyboard():
    markup = InlineKeyboardMarkup()
    yes_button = InlineKeyboardButton(
        "YES ",
        callback_data="start_yes"
    )
    no_button = InlineKeyboardButton(
        "NO",
        callback_data="start_no"
    )
    markup.add(yes_button)
    markup.add(no_button)
    return markup
