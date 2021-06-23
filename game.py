#this is a game where you have to try to defeat Zorlock the wizard 

import random

username = input('Enter a username : ') 
print(f"Welcome {username.lower()}! ")
player_health = 100
enemy_health = 100
enemy_name = "Zorlock"
# this loop will keep asking to pick a weapon till either you die or enemy dies.
while enemy_health > 0 :
    weapon = input("Please type Which weapon you would like to select : sword / staff / shield : ")
    if weapon.lower() == "sword": 
        print('You have selected: ' , weapon.lower())
        attack_decision = input("Attack enemy? (y/n) : ")

        if attack_decision.lower() == 'y':
            player_health = player_health - random.randint(15, 35)
            enemy_health = enemy_health - random.randint(20, 45)
            print(f"[!] Your close range attck let {enemy_name} get a good hit on you, your health is now {player_health} and you dealt enough damage to make his health {enemy_health}")
            continue
        else:
            player_health = player_health - random.randint(5, 40)
            print(f"[!]{username} didnt' act fast enough {enemy_name} attacked you, making your new health {player_health}. ") 
            continue

    elif weapon.lower() == "staff":
        print(f"You have selcted: {weapon.lower()}")
        attack_decision = input("Attack enemy? (y/n) : " )

        if  attack_decision.lower() == 'y':
            player_health = player_health - random.randint(10, 25)
            enemy_health = enemy_health - random.randint(10, 19)
            print(f"[!] Your staff makes your reach longer, you didn't take much damage your health is now {player_health} and zorlocks is now at {enemy_health}")
            continue
        else:
            player_health = player_health - random.randint(11, 24)
            print(f"[!]{username} didnt act fast enough! {enemy_name} was able to hit you.. {username}, your health is {player_health}.")
            continue

    elif weapon.lower() == "shield":
        print(f"You have selcted: {weapon.lower()}")
        attack_decision = input("Attack enemy? (y/n) : " )

        if attack_decision.lower() == "y":
            player_health = player_health - random.randint(0, 10)
            enemy_health = enemy_health - random.randint(10, 15)
            print(f"[!]{username}, your shield is durable but not strong in damage. {enemy_name}'s health is now {enemy_health}.Good thing you had a shield he wasnt able to do much damage. Your health is {player_health}")
            continue
        else: 
            player_health = player_health + random.randint(10, 21)
            print(f"[!]{username} used the shield to reflect {enemy_name}'s attack. Good Job your health is now {player_health}")
            continue
    else:
        print("You need to choose a weapon in order to defeat", enemy_name)
        continue

if enemy_health <= 0: 
    print(f"Good job {username} you have defeated {enemy_name}!!")

if player_health <=0:
    print(f"Unlucky you have gotten defeated by {enemy_name}... Better luck next time.")
