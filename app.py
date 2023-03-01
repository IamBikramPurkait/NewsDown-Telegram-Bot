# -*- coding: utf-8 -*-

import os
import time
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from scrapper import *


file_name = ""
not_available_papers = []
file_name_list = set()


load_dotenv()
api_id_env = os.getenv('api_id')
api_hash_env = os.getenv('api_hash')
bot_token_env = os.getenv('bot_token')

bot = Client("my_bot", api_id=api_id_env,
             api_hash=api_hash_env, bot_token=bot_token_env)


def pdf_cleaner_newsdown():
    dir_name = "./paper/"
    list_dir = os.listdir(dir_name)
    if list_dir:
        for item in list_dir:
            if item.endswith(".pdf"):
                os.remove(os.path.join(dir_name, item))


def file_name_generator(paper_name):
    global file_name
    for _ in range(1):
        try:
            file_name = alternate_downloader(paper_name)
            break
        except Exception:
            print("error1")

        try:
            file_name = paper_downloader(paper_name)
            break
        except Exception:
            print("error2")

        try:
            file_name = anandabazar(paper_name)
            break
        except Exception:
            print("error3")

        try:
            file_name = ekdin(paper_name)
            break
        except Exception:
            print("error4")

        try:
            file_name = pioneer(paper_name)
            break
        except Exception:
            print("error5")

    return file_name


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
        \nIt can download 14 English, 12 Hindi and 5 Bengali varient newspaper.\nIf you have any query, contact me - Bikram Purkait ( @IamBikramPurkait ).
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
            'HINDUSTAN TIMES', callback_data="HINDUSTAN_TIMES")
    ],

    [
        InlineKeyboardButton(
            'MUMBAI MIRROR', callback_data="MUMBAI_MIRROR"),
        InlineKeyboardButton(
            'ECONOMIC TIMES', callback_data="ECONOMIC_TIMES")
    ],
    [
        InlineKeyboardButton(
            'BUSINESS STANDARD', callback_data="BUSINESS_STANDARD"),
        InlineKeyboardButton(
            'BUSINESS LINE', callback_data="BUSINESS_LINE")
    ],
    [
        InlineKeyboardButton(
            'MINT', callback_data="MINT"),
        InlineKeyboardButton(
            'ASIAN AGE', callback_data="ASIAN_AGE")
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
        InlineKeyboardButton('HINDUSTAN DAINIK',
                             callback_data="HINDUSTAN_DAINIK")
    ],
    [
        InlineKeyboardButton('JANSATTA', callback_data="JANSATTA"),
        InlineKeyboardButton('NAVBHARAT', callback_data="NAVBHARAT")
    ],
    [
        InlineKeyboardButton('AMAR UJALA', callback_data="AMAR_UJALA"),
        InlineKeyboardButton('HARI BHOOMI', callback_data="HARI_BHOOMI")
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
        InlineKeyboardButton('DAINIK STATESMAN',
                             callback_data="DAINIK_STATESMAN")
    ],
    [
        InlineKeyboardButton('EISAMAY', callback_data="EISAMAY"),
        InlineKeyboardButton('EKDIN', callback_data="EKDIN")
    ],
    [
        InlineKeyboardButton('SANGBAD PRATIDIN',
                             callback_data="SANGBAD_PRATIDIN")
    ],
    [
        InlineKeyboardButton('BACK', callback_data="BACK")
    ]

]


START_MESSAGE = "Select a Langauge"
DOWNLOAD_MESSAGE = " paper selected. Press /download for download the newspaper."


@ bot.on_message(filters.command('start'))
def start(bot, message):
    time_stamp = get_time()
    current_time = time_stamp.get("current_time")
    paper_available_time = time_stamp.get("paper_available_time")

    print("Current time -->", current_time)

    if current_time <= paper_available_time:
        bot.send_message(
            message.chat.id, "Note: Due to unavailable of paper in the repective newspaper site, everyday midnight 00:00 AM to 07:00 AM only previous day paper available for download.")
    message.reply(
        START_MESSAGE,
        reply_markup=InlineKeyboardMarkup(LANGUAGE_SELECT_BUTTON)
    )


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
        paper_name = "TIMES_OF_INDIA"
        file_name = file_name_generator(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )

    elif callback.data == "HINDUSTAN_TIMES":
        paper_name = "HINDUSTAN_TIMES"
        file_name = file_name_generator(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )

    elif callback.data == "MUMBAI_MIRROR":
        paper_name = "MUMBAI_MIRROR"
        file_name = file_name_generator(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )

    elif callback.data == "ECONOMIC_TIMES":
        paper_name = "ECONOMIC_TIMES"
        file_name = file_name_generator(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )

    elif callback.data == "BUSINESS_STANDARD":
        paper_name = "BUSINESS_STANDARD"
        file_name = file_name_generator(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )

    elif callback.data == "BUSINESS_LINE":
        paper_name = "BUSINESS_LINE"
        file_name = file_name_generator(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )

    elif callback.data == "MINT":
        paper_name = "MINT"
        file_name = file_name_generator(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )

    elif callback.data == "ASIAN_AGE":
        paper_name = "ASIAN_AGE"
        file_name = file_name_generator(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )

    elif callback.data == "DECCAN_CHRONICLE":
        paper_name = "DECCAN_CHRONICLE"
        file_name = file_name_generator(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )
    elif callback.data == "FINANCIAL_EXPRESS":
        paper_name = "FINANCIAL_EXPRESS"
        file_name = file_name_generator(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )
    elif callback.data == "STATESMAN":
        paper_name = "STATESMAN"
        file_name = file_name_generator(paper_name)

        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )

    elif callback.data == "TELEGRAPH":
        paper_name = "TELEGRAPHINDIA"
        file_name = file_name_generator(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )

    elif callback.data == "TRIBUNE":
        paper_name = "TRIBUNE"
        file_name = file_name_generator(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )

    elif callback.data == "PIONEER_ENGLISH":
        paper_name = "PIONEER-ENGLISH"
        file_name = file_name_generator(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )

    elif callback.data == "DAINAIK_BHASKAR":
        paper_name = "DAINAIK_BHASKAR"
        file_name = file_name_generator(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )

    elif callback.data == "DAINIK_JAGRAN":
        paper_name = "DAINIK_JAGRAN"
        file_name = file_name_generator(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )

    elif callback.data == "DAINIK_NAVAJYOTI":
        paper_name = "DAINIK_NAVAJYOTI"
        file_name = file_name_generator(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )

    elif callback.data == "PUNJAB_KESARI":
        paper_name = "PUNJAB_KESARI"
        file_name = file_name_generator(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )

    elif callback.data == "RASHTRIYA_SAHARA":
        paper_name = "RASHTRIYA_SAHARA"
        file_name = file_name_generator(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )

    elif callback.data == "RAJASTHAN_PATRIKA":
        paper_name = "RAJASTHAN_PATRIKA"
        file_name = file_name_generator(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )

    elif callback.data == "PIONEER_HINDI":
        paper_name = "PIONEER-HINDI"
        file_name = file_name_generator(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )

    elif callback.data == "HINDUSTAN_DAINIK":
        paper_name = "HINDUSTAN_DAINIK"
        file_name = file_name_generator(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )

    elif callback.data == "JANSATTA":
        paper_name = "JANSATTA"
        file_name = file_name_generator(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )

    elif callback.data == "NAVBHARAT":
        paper_name = "NAVBHARAT"
        file_name = file_name_generator(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )

    elif callback.data == "AMAR_UJALA":
        paper_name = "AMAR_UJALA"
        file_name = file_name_generator(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )

    elif callback.data == "HARI_BHOOMI":
        paper_name = "HARI_BHOOMI"
        file_name = file_name_generator(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )

    elif callback.data == "ANANDABAZAR":
        paper_name = "ANANDABAZAR"
        file_name = file_name_generator(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )

    elif callback.data == "DAINIK_STATESMAN":
        paper_name = "DAINIK_STATESMAN"
        file_name = file_name_generator(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )

    elif callback.data == "EISAMAY":
        paper_name = "EISAMAY"
        file_name = file_name_generator(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )

    elif callback.data == "EKDIN":
        paper_name = "EKDIN"
        file_name = file_name_generator(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )

    elif callback.data == "SANGBAD_PRATIDIN":
        paper_name = "SANGBAD_PRATIDIN"
        file_name = file_name_generator(paper_name)
        callback.edit_message_text(
            text=f"{paper_name}{DOWNLOAD_MESSAGE}"
        )


@bot.on_message(filters.command('download'))
def document(bot, message):
    file_type = open(file_name, 'rb')

    bot.send_document(
        message.chat.id, file_type, caption="Enjoy your paper😊 and keep reading❤️", file_name=file_name.split('/')[2], protect_content=True)
    file_type.close()
    pdf_cleaner_newsdown()


@bot.on_message(filters.command("forward"))
def forward_messages(bot, message):

    def send_document(file_name):
        file_type = open(file_name, 'rb')
        # time.sleep(30)
        bot.send_document(
            message.chat.id, file_type, file_name=file_name.split('/')[2])

    def paper():
        print("Start Forwarding")
        file_name_list.clear()

        # LIST OF PAPERS
        for name, value in alternate_papers_link.items():
            try:
                file_name = file_name_generator(name)
                file_name_list.add(file_name)
            except Exception:
                print("error")
                continue

        # ANANDABAZAR AND TELEGRAPHINDIA
        for name in anandabazar_papers_list:
            try:
                file_name = file_name_generator(name)
                file_name_list.add(file_name)
            except Exception:
                print("error")
                continue

        # EKDIN
        try:
            file_name = ekdin("EKDIN")
            file_name_list.add(file_name)
        except Exception:
            print("error")

        # PIONEER
        for name in pioneer_paper_list:
            try:
                file_name = pioneer(name)
                file_name_list.add(file_name)
            except Exception:
                print("error")
                continue

        bot.send_message(message.chat.id, "Start Forwarding")
        for name in file_name_list:
            bot.send_sticker(
                message.chat.id, f"./sticker/{name.split(' ')[1].split('.')[0]}.webp")
            send_document(name)
        print(file_name_list)

        pdf_cleaner_newsdown()
        file_name_list.clear()

        print(not_available_papers)
        print("Done")

    paper()


print("ALIVE")
bot.run()
