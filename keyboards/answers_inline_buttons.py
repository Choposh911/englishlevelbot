from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def answer_1():
    markup = InlineKeyboardMarkup()
    a1_button = InlineKeyboardButton(
        "a)YES, I am  ",
        callback_data="a1_button"
    )
    b1_button = InlineKeyboardButton(
        "b)NO, I'm not ",
        callback_data="b1_button"
    )
    c1_button = InlineKeyboardButton(
        "c)NO, I don't ",
        callback_data="c1_button"
    )
    d1_button = InlineKeyboardButton(
        "d)Yes, they do ",
        callback_data="d1_button"
    )
    markup.add(a1_button)
    markup.add(b1_button)
    markup.add(c1_button)
    markup.add(d1_button)

    return markup


async def answer_2():
    markup = InlineKeyboardMarkup()
    a2_button = InlineKeyboardButton(
        "a) working   ",
        callback_data="a2_button"
    )
    b2_button = InlineKeyboardButton(
        "b) worked ",
        callback_data="b2_button"
    )
    c2_button = InlineKeyboardButton(
        "c) will work",
        callback_data="c2_button"
    )
    d2_button = InlineKeyboardButton(
        "d) work ",
        callback_data="d2_button"
    )
    markup.add(a2_button)
    markup.add(b2_button)
    markup.add(c2_button)
    markup.add(d2_button)

    return markup


async def answer_3():
    markup = InlineKeyboardMarkup()
    a3_button = InlineKeyboardButton(
        "a)Is there  ",
        callback_data="a3_button"
    )
    b3_button = InlineKeyboardButton(
        "b)Are there ",
        callback_data="b3_button"
    )
    c3_button = InlineKeyboardButton(
        "c)Is here ",
        callback_data="c3_button"
    )
    d3_button = InlineKeyboardButton(
        "d)Are here",
        callback_data="d3_button"
    )
    markup.add(a3_button)
    markup.add(b3_button)
    markup.add(c3_button)
    markup.add(d3_button)

    return markup


async def answer_4():
    markup = InlineKeyboardMarkup()
    a4_button = InlineKeyboardButton(
        "a)The  ",
        callback_data="a4_button"
    )
    b4_button = InlineKeyboardButton(
        "b)A ",
        callback_data="b4_button"
    )
    c4_button = InlineKeyboardButton(
        "c) At ",
        callback_data="c4_button"
    )
    d4_button = InlineKeyboardButton(
        "d)-",
        callback_data="d4_button"
    )
    markup.add(a4_button)
    markup.add(b4_button)
    markup.add(c4_button)
    markup.add(d4_button)

    return markup

