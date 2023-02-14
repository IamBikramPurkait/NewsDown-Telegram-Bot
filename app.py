# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from scrapper import *

file_name = ""


load_dotenv()
api_id_env = os.getenv('api_id')
api_hash_env = os.getenv('api_hash')
bot_token_env = os.getenv('bot_token')

bot = Client("my_bot", api_id=api_id_env,
             api_hash=api_hash_env, bot_token=bot_token_env)


def pdf_cleaner():
    dir_name = "./paper/"
    list_dir = os.listdir(dir_name)
    for item in list_dir:
        if item.endswith(".pdf"):
            os.remove(os.path.join(dir_name, item))


@bot.on_message(filters.command('available_papers'))
def available_papers(bot, message):
    bot.send_photo(
        message.chat.id, "available_papers.png")


@bot.on_message(filters.command('upcoming_feature'))
def upcoming_feature(bot, message):
    message.reply_text(
        """
        Upcoming features ->\n1) Added other language newspaper.\n2) Able to download past newsapaper(eg: 5 years previous newspaper.)\n3) Able to download newsapaper with your choice pages(eg: if a day have 16 pages total paper then you are also able download the newspaper upto as your choice.).\n4) Many more .....
        """)


@bot.on_message(filters.command('about'))
def about(bot, message):
    message.reply_text(
        """
        Welcome to NewsDown.\nNewsDown download a newsapaper for you in just one click.\nNewsDown is built in python with ❤️.
        \nIt can download 9 English, 10 Hindi and 2 Bengali varient newspaper.\nIf you have any query, contact me - Bikram Purkait ( @IamBikramPurkait ).
        """)


@bot.on_message(filters.command('help'))
def help(bot, message):
    message.reply_text("""
    List of command ->\n/start -> Start the NewsDown.\n/download -> Download your selected newspaper.\n/about -> See the about section.\n/developer -> See the developer.\n/upcoming_feature -> See the upcoming features.\n/available_papers -> See the currently available papers.
    """)


@bot.on_message(filters.command('developer'))
def developer(bot, message):
    message.reply_text(
        "NewsDown is developed by Bikram Purkait ( @IamBikramPurkait )")


LANGUAGE_SELECT_BUTTON = [
    [
        InlineKeyboardButton('ENGLISH', callback_data="ENGLISH"),
        InlineKeyboardButton('HINDI', callback_data="HINDI"),
        InlineKeyboardButton('BENGALI', callback_data="BENGALI")

    ]
]

ENGLISH_NEWS_BUTTON = [
    [
        InlineKeyboardButton(
            'TIMES OF INDIA', callback_data="TIMES_OF_INDIA"),
        InlineKeyboardButton(
            'ECONOMIC TIMES', callback_data="ECONOMIC_TIMES")
    ],
    [
        InlineKeyboardButton('DECCAN CHRONICLE',
                             callback_data="DECCAN_CHRONICLE"),
        InlineKeyboardButton('FINANCIAL EXPRESS',
                             callback_data="FINANCIAL_EXPRESS")

    ],
    [
        InlineKeyboardButton('STATESMAN', callback_data="STATESMAN"),
        InlineKeyboardButton('TELEGRAPH', callback_data="TELEGRAPH")
    ],
    [
        InlineKeyboardButton('HINDU', callback_data="HINDU"),
        InlineKeyboardButton('TRIBUNE', callback_data="TRIBUNE"),
        InlineKeyboardButton('PIONEER', callback_data="PIONEER_ENGLISH")
    ],
    [
        InlineKeyboardButton('BACK', callback_data="BACK")
    ]
]


HINDI_NEWS_BUTTON = [
    [
        InlineKeyboardButton(
            'DAINAIK BHASKAR', callback_data="DAINAIK_BHASKAR"),
        InlineKeyboardButton(
            'DAINIK JAGRAN', callback_data="DAINIK_JAGRAN")
    ],
    [
        InlineKeyboardButton('DAINIK NAVAJYOTI',
                             callback_data="DAINIK_NAVAJYOTI"),
        InlineKeyboardButton('NAVBHARAT',
                             callback_data="NAVBHARAT")

    ],
    [
        InlineKeyboardButton(
            'PRABHAT KHABAR', callback_data="PRABHAT_KHABAR"),
        InlineKeyboardButton(
            'PUNJAB KESARI', callback_data="PUNJAB_KESARI")
    ],
    [
        InlineKeyboardButton('RASHTRIYA SAHARA',
                             callback_data="RASHTRIYA_SAHARA"),
        InlineKeyboardButton('RAJASTHAN PATRIKA',
                             callback_data="RAJASTHAN_PATRIKA")
    ],

    [
        InlineKeyboardButton('PIONEER', callback_data="PIONEER_HINDI"),
        InlineKeyboardButton('JANSATTA', callback_data="JANSATTA")

    ],
    [
        InlineKeyboardButton(
            'BACK', callback_data="BACK")
    ]
]

BENGALI_NEWS_BUTTON = [
    [
        InlineKeyboardButton(
            'ANANDABAZAR', callback_data="ANANDABAZAR"),
        InlineKeyboardButton('EKDIN', callback_data="EKDIN")
    ],

    [
        InlineKeyboardButton('BACK', callback_data="BACK")
    ]

]


START_MESSAGE = "Select a Langauge"
DOWNLOAD_MESSAGE = " paper selected. Press /download for download the newspaper."


@bot.on_message(filters.command('start'))
def start(bot, message):
    if paper_available_time >= current_time:
        bot.send_message(
            chat_id=message.chat.id, text="Note: Due to unavailable of paper in the repective newspaper site, everyday midnight 00:00 AM to 07:00 AM only previous day paper available for download.")
    message.reply(
        START_MESSAGE,
        reply_markup=InlineKeyboardMarkup(LANGUAGE_SELECT_BUTTON)
    )
    pdf_cleaner()


@bot.on_callback_query()
def callback_query(bot, callback):
    global file_name
    TEXT = "Choose a Paper"
    if callback.data == "ENGLISH":
        callback.edit_message_text(
            TEXT,
            reply_markup=InlineKeyboardMarkup(ENGLISH_NEWS_BUTTON)
        )

    elif callback.data == "HINDI":
        callback.edit_message_text(
            TEXT,
            reply_markup=InlineKeyboardMarkup(HINDI_NEWS_BUTTON)
        )
    elif callback.data == "BENGALI":
        callback.edit_message_text(
            TEXT,
            reply_markup=InlineKeyboardMarkup(BENGALI_NEWS_BUTTON)
        )
    elif callback.data == "BACK":
        callback.edit_message_text(
            START_MESSAGE,
            reply_markup=InlineKeyboardMarkup(LANGUAGE_SELECT_BUTTON)
        )
    elif callback.data == "TIMES_OF_INDIA":
        paper_name = "TIMES OF INDIA"
        file_name = paper_downloader(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )
    elif callback.data == "ECONOMIC_TIMES":
        paper_name = "ECONOMIC TIMES"
        file_name = paper_downloader(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )
    elif callback.data == "DECCAN_CHRONICLE":
        paper_name = "DECCAN CHRONICLE"
        file_name = paper_downloader(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )
    elif callback.data == "FINANCIAL_EXPRESS":
        paper_name = "FINANCIAL EXPRESS"
        file_name = paper_downloader(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )
    elif callback.data == "STATESMAN":
        paper_name = "STATESMAN"
        file_name = paper_downloader(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )
    elif callback.data == "TELEGRAPH":
        paper_name = "TELEGRAPHINDIA"
        file_name = anandabazar(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )
    elif callback.data == "HINDU":
        paper_name = "HINDU"
        file_name = paper_downloader(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )
    elif callback.data == "TRIBUNE":
        paper_name = "TRIBUNE"
        file_name = paper_downloader(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )
    elif callback.data == "PIONEER_ENGLISH":
        paper_name = "PIONEER-ENGLISH"
        file_name = pioneer(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )
    elif callback.data == "DAINAIK_BHASKAR":
        paper_name = "DAINAIK BHASKAR"
        file_name = paper_downloader(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )
    elif callback.data == "DAINIK_JAGRAN":
        paper_name = "DAINIK JAGRAN"
        file_name = paper_downloader(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )
    elif callback.data == "DAINIK_NAVAJYOTI":
        paper_name = "DAINIK NAVAJYOTI"
        file_name = paper_downloader(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )
    elif callback.data == "NAVBHARAT":
        paper_name = "NAVBHARAT"
        file_name = paper_downloader(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )
    elif callback.data == "JANSATTA":
        paper_name = "JANSATTA"
        file_name = paper_downloader(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )
    elif callback.data == "PUNJAB_KESARI":
        paper_name = "PUNJAB KESARI"
        file_name = paper_downloader(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )
    elif callback.data == "RASHTRIYA_SAHARA":
        paper_name = "RASHTRIYA SAHARA"
        file_name = paper_downloader(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )
    elif callback.data == "RAJASTHAN_PATRIKA":
        paper_name = "RAJASTHAN PATRIKA"
        file_name = paper_downloader(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )
    elif callback.data == "PRABHAT_KHABAR":
        paper_name = "PRABHAT KHABAR"
        file_name = paper_downloader(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )
    elif callback.data == "PIONEER_HINDI":
        paper_name = "PIONEER-HINDI"
        file_name = pioneer(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )
    elif callback.data == "ANANDABAZAR":
        paper_name = "ANANDABAZAR"
        file_name = anandabazar(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )
    elif callback.data == "EKDIN":
        paper_name = "EKDIN"
        file_name = ekdin(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )


@bot.on_message(filters.command('download'))
def document(bot, message):
    file_type = open(file_name, 'rb')

    bot.send_document(
        message.chat.id, file_type, caption="Enjoy your paper😊 and keep reading❤️", file_name=file_name.split('/')[2], protect_content=True)
    file_type.close()


print("ALIVE")
bot.run()
