class Character(object):
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

#comments
class Hero(Character):
    def __init__(self):
        self.health = 10
        self.power = 5

    def attack(self, enemy):
        enemy.health -= self.power
        print "You do %d damage to the goblin." % self.power
        if enemy.health <= 0:
            print "The goblin is dead."

    def print_status(self):
        print "You have %d health and %d power." % (self.health, self.power)


class Goblin(Character):
    def __init__(self):
        self.health = 6
        self.power = 2

    def attack(self, enemy):
        enemy.health -= self.power
        print "The goblin does %d damage to you." % self.power
        if enemy.health <= 0:
            print "You are dead."

    def print_status(self):
        print "The goblin has %d health and %d power." % (self.health, self.power)
# this is a message

def main():
    barry_the_hero = Hero()
    steve_the_goblin = Goblin()

    while steve_the_goblin.alive() and barry_the_hero.alive():
        barry_the_hero.print_status()
        steve_the_goblin.print_status()
        print
        print "What do you want to do?"
        print "1. fight goblin"
        print "2. do nothing"
        print "3. flee"
        print "> ",
        input = raw_input()
        if input == "1":
            # Hero attacks goblin
            barry_the_hero.attack(steve_the_goblin)
        elif input == "2":
            pass
        elif input == "3":
            print "Goodbye."
            break
        else:
            print "Invalid input %r" % input

        if steve_the_goblin.alive():
            # Goblin attacks hero
            steve_the_goblin.attack(barry_the_hero)


main()






# In this simple RPG game, the hero fights the goblin. He has the options to:
# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

def main():
    hero_health = 10
    hero_power = 5
    goblin_health = 6
    goblin_power = 2

    while goblin_health > 0 and hero_health > 0:
        print "You have %d health and %d power." % (hero_health, hero_power)
        print "The goblin has %d health and %d power." % (goblin_health, goblin_power)
        print
        print "What do you want to do?"
        print "1. fight goblin"
        print "2. do nothing"
        print "3. flee"
        print "> ",
        input = raw_input()
        if input == "1":
            # Hero attacks goblin
            goblin_health -= hero_power
            print "You do %d damage to the goblin." % hero_power
            if goblin_health <= 0:
                print "The goblin is dead."
        elif input == "2":
            pass
        elif input == "3":
            print "Goodbye."
            break
        else:
            print "Invalid input %r" % input

        if goblin_health > 0:
            # Goblin attacks hero
            hero_health -= goblin_power
            print "The goblin does %d damage to you." % goblin_power
            if hero_health <= 0:
                print "You are dead."


main()

