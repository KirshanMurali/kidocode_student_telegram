import time
import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
import pickle
token = '592251535:AAECV51q0myLYpouj7lNs7IH28qSMw4KuU8'
TelegramBot = telepot.Bot(token)

# example_dict = {"date":"12/12/2012","kidoid":"kido2256","User":"Arsham","Time":"50","comment":"uvuwevwevwve onyetenyevwe ugwemubwem ossas why are you running"}
# pickle_out = open("dict.pickle","wb")
# pickle.dump(example_dict,pickle_out)
# pickle_out.close()


# pickle_out = open("dict.pickle","rb")
# pickle.load(pickle_out)
# print pickle_out.read()
# pickle_out.close()


latestId=0

def returnedInfo(kid):
    info={'kido3567':{'logs':[('date','sender','issue')]},
                'kido6788':{'logs':[('date','sender','issue'),('date','sender','issue')]}
            }
            
    theInfo=info.get(kid.lower(),'no data')
    return str(theInfo)

while True:
    #receiving messages from telegram
    messages=TelegramBot.getUpdates(offset=latestId)


    #geting the latest ID
    if messages:
        latestId=messages[-1]['update_id']+1
        for message in messages:
            # try:
            
            kidoID=message['message']['text']
            current_date = str(time.localtime(messages[0]["message"]["date"]).tm_mday) + "/" + str(time.localtime(messages[0]["message"]["date"]).tm_mon) + "/" + str(time.localtime(messages[0]["message"]["date"]).tm_year)
            # message[0]["message"]["date"] = current_date
            # pickle_out = open("dict.pickle","rb")
            # pickle.load(pickle_out)
            # p =  pickle_out.read()
            # pickle_out.close()
            
            # if kidoID == p[0]:
            #     print uvu
            # print latestId
            
           
          
            
            TelegramBot.sendMessage(message['message']['chat']['id'], "hi" + " " +  message['message']['from']['first_name'] + " " + current_date +" "+ returnedInfo(message['message']['text']),reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [KeyboardButton(text="Yes"), KeyboardButton(text="No")]
                                ]
                            ))
            
            #     answer="Kidoid: {}, user : {} , time : {} , comment {}".format(kidoID,)
            #     # TelegramBot.sendMessage(message['message']['chat']['id'],answer)
            # except:
                # TelegramBot.sendMessage(message['message']['chat']['id'],"This is Not What i expected")
        print messages
        print '-'*10
        

    if messages and messages[-1]['message']['text']=="stop":
        break