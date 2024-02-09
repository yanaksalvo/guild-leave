import time
import requests

TOKEN_DELETER = input("Token: ")
GUILD_ID = input("Guild ID: ")

DELETER_HEADERS = {
    "Authorization": TOKEN_DELETER,
}

def deleter_action():
    time.sleep(1)
    response = requests.delete(f"https://discord.com/api/v10/users/@me/guilds/{GUILD_ID}",
                               headers=DELETER_HEADERS)
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")

deleter_action()