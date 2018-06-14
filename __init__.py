import time, pickle, telepot, json
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
from databases.user_database import save_user, get_user
from databases.Menu import Menu
token = '592251535:AAECV51q0myLYpouj7lNs7IH28qSMw4KuU8'
TelegramBot = telepot.Bot(token)

latestId=0
initial_message_sent = False
admins = ["Kirshan", "Arsham"]

def send_message(chat_id, message, reply_markup=[]):
    keyboard_buttons = []
    for i in reply_markup:
#         if len(keyboard_buttons) >= 3:
#             print keyboard_buttons
#             break
        keyboard_buttons.append([KeyboardButton(text=i)])
    TelegramBot.sendMessage(chat_id, message, reply_markup = ReplyKeyboardMarkup(keyboard = keyboard_buttons))

while True:
    #receiving messages from telegram
    messages=TelegramBot.getUpdates(offset=latestId)

    #geting the latest ID
    if messages:
        latestId=messages[-1]['update_id']+1
        if initial_message_sent == False:
            TelegramBot.sendMessage(messages[0]['message']['chat']['id'], "Keyboard Buttons Activated", reply_markup=ReplyKeyboardMarkup(
                                    keyboard=[
                                        [KeyboardButton(text="Hi"), KeyboardButton(text="Buy")]
                                    ]
                                ))
            initial_message_sent = True
        else:
            for message in messages:
                current_message = message["message"]["text"]
                chat_id = message['message']['chat']['id']
                user_info = message['message']['from']
                date_info = time.localtime(messages[0]["message"]["date"])
                current_date = "{}/{}/{}".format(date_info.tm_mday, date_info.tm_mon, date_info.tm_year)
                # try:
                if current_message == "Hi":
                    send_message(chat_id, "Hi {} Today is {}".format(user_info['first_name'], current_date))
                elif current_message == "Buy":
                    menu = Menu("menu.json")
                    menu_items = menu.get_menu(spec_item="name")
                    print "start"
                    print menu.add_item("","","")
                    print "end"
                    send_message(chat_id, "What to buy?", menu_items)#reply_markup=ReplyKeyboardMarkup(
                                    # keyboard=[
                                    #     [KeyboardButton(text="Cheese naan"), KeyboardButton(text="Garlic Naan"), KeyboardButton(text="Butter Naan")],
                                    #     [KeyboardButton(text="Naan"), KeyboardButton(text="Tandoori Chicken"), KeyboardButton(text="Biriyani")], 
                                    #     [KeyboardButton(text="Cold Storage"), KeyboardButton(text="Jooje Kebab"), KeyboardButton(text="Khash Khash Kebab")], 
                                    #     [KeyboardButton(text="Lari Kebab"), KeyboardButton(text="Nandos Chicken"), KeyboardButton(text="More...")]
                                    # ]
                                #))
                
        print messages
        print '-'*10

    if messages and messages[-1]['message']['text']=="stop":
        break