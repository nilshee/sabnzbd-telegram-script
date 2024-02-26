import sys
import os
import requests

#print( os.environ.get("SAB_NOTIFICATION_PARAMETERS"))
try:
    (scriptname, notification_type, notification_title, notification_text) = sys.argv
except:
    print("No commandline parameters found")
    sys.exit(1)
parameters = os.environ.get("SAB_NOTIFICATION_PARAMETERS")
if parameters == "" or ',' not in parameters:
    print("No Commandline paramaeter. Pls specify as Bot_token,chat_id without spaces-")
    sys.exit(1)
# continue script
bot_token, chat_id =parameters.split(",")
url= "https://api.telegram.org/bot" + bot_token + "/sendMessage"
# Your code goes here
data = {"text": notification_title + "\nType: " + notification_type + "\n" + notification_text, "chat_id": chat_id}
response = requests.post(url=url, json=data)
if response.status_code == 200:
    #everything is fine exit with 0
    sys.exit(0)
elif response.status_code == 401:
    # Telegram replies with unauthorized so there is either no valid bot_token or the bot_token is not allowed to send in the supplied chat
    print("Either the bot_token is not valid or the bot is not allowed to send in the supplied chat.\nDetailed error message: " + response.text)
else:
    #general catch for errors
    print("Error: \nMessage: " +response.text)
# Success code
sys.exit(1)
