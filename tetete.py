from simple_term_menu import TerminalMenu
import requests
import time
abrido = False
print(r"""/ 
     _______.     ___       _______  .___  ___.      ___      .__   __. 
    /       |    /   \     |       \ |   \/   |     /   \     |  \ |  | 
   |   (----`   /  ^  \    |  .--.  ||  \  /  |    /  ^  \    |   \|  | 
    \   \      /  /_\  \   |  |  |  ||  |\/|  |   /  /_\  \   |  . `  | 
.----)   |    /  _____  \  |  '--'  ||  |  |  |  /  _____  \  |  |\   | 
|_______/    /__/     \__\ |_______/ |__|  |__| /__/     \__\ |__| \__| 
                                                                        
 """)

url = "https://temp-mail44.p.rapidapi.com/api/v3/email/new"
time.sleep[2]

abrido = True
payload = {
	"key1": "value",
	"key2": "value"
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "e3d37b0f8emshcd9cf24df8b221ep10e843jsnb0e21fb6ccbb",
	"X-RapidAPI-Host": "temp-mail44.p.rapidapi.com"
}

MailCriado = requests.request("POST", url, json=payload, headers=headers)


mailboxx = "https://temp-mail44.p.rapidapi.com/api/v3/email/fhvw0u7u3e@plancetose.com/messages"

headers = {
	"X-RapidAPI-Key": "e3d37b0f8emshcd9cf24df8b221ep10e843jsnb0e21fb6ccbb",
	"X-RapidAPI-Host": "temp-mail44.p.rapidapi.com"
}

Caidadeentrada = requests.request("GET", mailboxx, headers=headers)



terminal_menu = TerminalMenu(["criar email", "caixa de entrada"])
 
if abrido == True:
  choice_index = terminal_menu.show()
    
   


if terminal_menu.chosen_menu_entry[1]:
    print(MailCriado)

if terminal_menu.chosen_menu_entry[2]:
    print(Caidadeentrada)