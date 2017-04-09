#!/usr/bin/env python

from telegram.ext import MessageHandler, Filters, CommandHandler, Updater
import requests
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import sys

# Args order - api_key, token, board_id

TEXT = """
    Hello! I am dapulseBot! Feel free to write any task that you want to add to your specific board, with the user's first name inside angle brackets.
    For example - send me:
    
    Call mom! <tal>

    And watch it created at Dapulse :) N~Joy!
    """

def init():
    if len(sys.argv) != 4:
        print("Error! Please add all arguments")
        print("Number of given arguments: " + str(len(sys.argv) -1 ) )
        print("Your arguments:" + str(sys.argv[1:len(sys.argv)]))
        sys.exit()

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=TEXT)

def addTask(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=parseRequest(update.message.text))

def httpOK(r):
    return r >= 200 and r < 300


def getUsers():
    users = []
    r = requests.get("https://api.dapulse.com:443/v1/users.json?api_key=" + sys.argv[1] ) # api_key
    if not httpOK(r.status_code):
        return []
    data = json.loads(r.content.decode('utf-8'))
    for user in data:
        users.append((user['name'], user['id']))
    return users

def parseRequest(text):
    retId = 0
    retUser = ""
    task = text[:text.find("<")] 
    user = text.split("<",1)[1][:-1]

    users = getUsers()
    if not users:
        return "Error getting users!"

    for name, ids in users:
        if user.lower() in name.lower():
            retId = ids 
            retUser = name 

    if retUser == "":
        return "User " + user + " is wrong. fix and try again"

    url = "https://api.dapulse.com:443/v1/boards/" + sys.argv[3] + "/pulses.json?api_key=" + sys.argv[1] # board_id, api_key
    payload = { "pulse": { "name": task }, "user_id": retId }

    r = requests.post(url, data=json.dumps(payload))
    print(r)
    if not httpOK(r.status_code):
        return "Error! Code: " + str(r.status_code)
    return "Added task: " + task + ", Dest user: " + retUser 

def main():
    init()
    token = sys.argv[2] #token
    updater = Updater(token=token)
    dispatcher = updater.dispatcher
    
    start_handler = CommandHandler('start', start)
    add_pulse_handler = MessageHandler(Filters.text, addTask)
    
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(add_pulse_handler)
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
