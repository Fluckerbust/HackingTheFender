import csv
import json

compromised_users = []
slash_sig = """ _  _     ___   __  ____ 
/ )( \   / __) /  \(_  _) 
) \/ (  ( (_ \(  O ) )( 
\____/   \___/ \__/ (__) 
 _  _   __    ___  __ _  ____  ____ 
 / )( \ / _\  / __)(  / )(  __)( 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \ 
(___)  \___ \/ (_/\/    \\___ \) __ ( 
       (____/\____/\_/\_/(____/\_)(_/ 
 __ _  _  _  __    __ 
(  ( \/ )( \(  )  (  ) 
/    /) \/ (/ (_/\/ (_/\ 
\_)__)\____/\____/\____/"""


with open('passwords.csv') as passwords:
  
 dictionary_passwords = csv.DictReader(passwords)
 for item in dictionary_passwords:
  compromised_users.append(item['Username'])

with open('compromised_users.txt', 'w') as compromised_users_file:
  for user in compromised_users:
    compromised_users_file.write(user+'\n')


with open('compromised_users.txt') as comp_user:
  print(comp_user.read())

with open('boss_message.json', 'w') as boss_msg:
  boss_dict = {
    "recipient": "The Boss",
    "message": "Mission Success"
  }
  json.dump(boss_dict, boss_msg)

with open('boss_message.json') as boss_msg:
  print(json.load(boss_msg))


with open('new_passwords.csv', 'w') as new_passwords_obj:
  new_passwords_obj.write(slash_sig)

with open('new_passwords.csv') as new_passwords_obj:
  print(new_passwords_obj.read())

