import random
x = random.randint(1,3)

s = random.randint(1,1000)
if int(s) >= (1) and int(s) <= (400):
    sword = 4
    print("You got a wooden sword! 40%")
elif int(s) >= (501) and int(s) <= (550):
    sword = 1
    print("You got your fist..... SHELL POZO 5%")
elif int(s) >= (551) and int(s) <= (750):
    sword = 5
    print("You got a stone sword! 20%")
elif int(s) >= (401) and int(s) <= (500):
    sword = 7
    print("You got a diamond sword! 10%")
elif int(s) >= (751) and int(s) <= (800):
    sword = 9
    print("You got a netherite sword! 5%")
elif int(s) >= (801) and int(s) <= (999):
    sword = 6
    print("You got a iron sword! 19.9%")
elif int(s) == 1000:
    sword = 69420
    print("Bro got the UNFRIGGINBELIEVALIST. Use it wisely. 0.1%")
atk = sword
print(atk)


y = random.randint(1,1000)
if int(y) >= (1) and int(y) <= (200):
    armor = 3
    print("You got Leather Armor 20%")
if int(y) >= (651) and int(y) <= (800):
    armor = 4
    print("You got Gold Armor 15%")
elif int(y) >= (201) and int(y) <= (350):
    armor = 5
    print("You got Chainmail Armor 15%")
elif int(y) >= (351) and int(y) <= (500):
    armor = 6
    print("You got Iron Armor 15%")
elif int(y) >= (501) and int(y) <= (600):
    armor = 8
    print("You got Diamond Armor 10%")
elif int(y) >= (601) and int(y) <= (650):
    armor = 9
    print("You got Netherite Armor 5%")
elif int(y) >= (801) and int(y) <= (900):
    armor = 1
    print("No Armor...... SHELL POZO 10%")
elif int(y) >= (901) and int(y) <= (999):
    armor = 7
    print("You got Emerald...Armor? 9.9%")
elif int(y) == (1000):
    armor = 263319020
    print("You have obtained ShellPozer (Superior) (Spartan) Armor.... Use it wisely 0.1%")
defe = armor
print(defe)


class mob:
    def __init__(self, name):
        self.name = name
class zombie(mob):
    def __init__(self, name, ehp, eatk, edefe):
        super().__init__(name)
        self.ehp = ehp
        self.eatk = eatk
        self.edefe = edefe
    def __str__(self):
        return f"{self.ehp}, {self.eatk}, {self.edefe}"
class enderman(zombie):
    def __init__(self, name, ehp, eatk, edefe, eheal):
        super().__init__(name, ehp, eatk, edefe)
        self.eheal = eheal
    def __str__(self):
        return f"{self.ehp}, {self.eatk}, {self.edefe}, {self.eheal}"
class ravager(enderman):
    def __init__(self, name, ehp, eatk, edefe, eheal):
        super().__init__(name, ehp, eatk, edefe, eheal)
    def __str__(self):
        return f"{self.ehp}, {self.eatk}, {self.edefe}, {self.eheal}"

hp = 20
heal = 2

zomb = zombie('Zombie', '16', '4', '5')
end = enderman('Endermen', '26', '6', '6', '2')
rav = ravager('Ravager', '32', '10', '8', '4')

if hp > 0:
    fight = input('Do you want to fight? ')
    if fight == "yes":
        print('You are fighting the zombie')
        while zomb.ehp >= 0:
            move = input('What move do you want to do? (Ex. atk, defe, heal) ')
            if move == "atk":
                print("X IS:")
                print(int(x))
                if int(x) == 1:
                    atk = atk - zomb.edefe
                    zomb.ehp = zomb.ehp - atk
                    print('Zombie has defended itself.')
                    print("Zombie hp is now:")
                    print(zomb.ehp)
                    zomb.edefe = 5
                    atk = 5
                    x = random.randint(1,3)
                elif int(x) == 2 or 3:
                    zomb.ehp = zomb.ehp - atk
                    print("Zombie hp is")
                    print(zomb.ehp)
                    hp = hp - zomb.eatk
                    print('Zombie has hit you')
                    print('Your hp is now:')
                    print(hp)
                    zomb.eatk = 4
                    atk = 5
                    x = random.randint(1,3)
            elif move == "heal":
                print("X IS:")
                print(int(x))
                hp = hp + heal
                print("You have healed. Your hp is now:")
                print(hp)
                if int(x) == 1:
                    print('Zombie has defended itself.')
                    print("Zombie hp is now:")
                    print(zomb.ehp)
                    zomb.edefe = 5
                    x = random.randint(1,3)
                elif int(x) == 2 or 3:
                    hp = hp - zomb.eatk
                    print('Zombie has hit you')
                    print('Your hp is now:')
                    print(hp)
                    zomb.eatk = 4
                    x = random.randint(1,3)
            elif move == "defe":
                print("X IS:")
                print(int(x))
                if int(x) == 2 or 3:
                    zomb.eatk = zomb.eatk - defe
                    hp = hp - zomb.eatk 
                    if hp > 20:
                        hp = 20
                        print('Zombie has hit you')
                        print('You defended yourself')
                        print('Your hp is now:')
                        print(hp)
                        zomb.eatk = 4
                    else:
                        print('Zombie has hit you')
                        print('You defended yourself')
                        print('Your hp is now:')
                        print(hp)
                        zomb.eatk = 4
                    x = random.randint(1,3)
                if int(x) == 1:
                    print('Zombie has defended itself.')
                    print("Zombie hp is now:")
                    print(zomb.ehp)
                    zomb.edefe = 5
        print("The zombie has been slain.")
        print("You are fighting the enderman.")
        while ehp >= 0:
            move = input('What move do you want to do? (Ex. atk, defe, heal) ')
            if move == "atk":
                print("X IS:")
                print(int(x))
                if int(x) == 1:
                    atk = atk - edefe
                    ehp = ehp - atk
                    print('Enderman has defended itself.')
                    print("Enderman hp is now:")
                    print(ehp)
                    edefe = 6
                    atk = 5
                    x = random.randint(1,3)
                elif int(x) == 2 or 3:
                    ehp = ehp - atk
                    print("Enderman hp is")
                    print(ehp)
                    hp = hp - eatk
                    print('Enderman has hit you')
                    print('Your hp is now:')
                    print(hp)
                    eatk = 6
                    atk = 5
                    x = random.randint(1,3)
            elif move == "heal":
                print("X IS:")
                print(int(x))
                hp = hp + heal
                print("You have healed. Your hp is now:")
                print(hp)
                if int(x) == 1:
                    print('Enderman has defended itself.')
                    print("Enderman hp is now:")
                    print(ehp)
                    edefe = 6
                    x = random.randint(1,3)
                elif int(x) == 2 or 3:
                    hp = hp - eatk
                    print('Enderman has hit you')
                    print('Your hp is now:')
                    print(hp)
                    eatk = 6
                    x = random.randint(1,3)
            elif move == "defe":
                print("X IS:")
                print(int(x))
                if int(x) == 2 or 3:
                    eatk = eatk - defe
                    hp = hp - eatk 
                    if hp > 20:
                        hp = 20
                        print('Enderman has hit you')
                        print('You defended yourself')
                        print('Your hp is now:')
                        print(hp)
                        eatk = 6
                    else:
                        print('Enderman has hit you')
                        print('You defended yourself')
                        print('Your hp is now:')
                        print(hp)
                        eatk = 6
                    x = random.randint(1,3)
                if int(x) == 1:
                    print('Enderman has defended itself.')
                    print("Enderman hp is now:")
                    print(ehp)
                    edefe = 6
        print("The enderman has been slain.")
        print("You are now fighting the ravager.")
if hp <= 0:
    print("You have died. SHELLPOZO. Try again, or are you a pu-")
