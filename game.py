#this is a game where you have to try to defeat Zorlock the wizard 

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
            player_health = player_health - 35
            enemy_health = enemy_health - 45
            print(f"[!] Your close range attck let {enemy_name} get a good hit on you, your health is now {player_health} and you dealt enough damage to the enemy that his health is now {enemy_health}")
            continue
        else:
            player_health = player_health - 35
            print(f"{username} didnt' act fast enough {enemy_name} attacked you for 35 making your new health {player_health}. ") 
            continue
    elif weapon.lower() == "staff":
        print(f"You have selcted: {weapon.lower()}")
        attack_decision = input("Attack enemy? (y/n) : " )

        if  attack_decision.lower() == 'y':
            player_health = player_health - 15
            enemy_health = enemy_health - 25
            print(f"[!] Your staff makes your reach longer so you did not take much damage your new health is {player_health} and your enemey is now at {enemy_health}")
            continue
        else:
            player_health = player_health - 10
            print(f"{username} didnt act fast enough {enemy_name} was able to hit you.. {username}, your new heal is {player_health}.")
            continue
    elif weapon.lower() == "shield":
        print(f"You have selcted: {weapon.lower()}")
        attack_decision = input("Attack enemy? (y/n) : " )

        if attack_decision.lower() == "y":
            player_health = player_health - 5
            enemy_health = enemy_health - 10
            print(f"{username}, your shield is durable but not strong in damage. you dealt 10 damage bringing {enemy_name} to {enemy_health}. He hit you for 5 bringing you to {player_health}")
            continue
        else: 
            player_health = player_health + 5
            print(f"{username} used the shield to reflect {enemy_name}'s attack. Good Job your health is now {player_health}")
            continue
    else:
        print("you need to choose a weapon in order to defeat", enemy_name)
        continue
if enemy_health <= 0: 
    print(f"Good job {username} you have defeated {enemy_name}!!")

if player_health <=0:
    print("Unlucky you have gotten defeated by Zorlock... Better luck next time.")
