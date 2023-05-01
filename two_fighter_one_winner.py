'''Create a function that returns the name of the winner in a fight between two fighters.

Each fighter takes turns attacking the other and whoever kills the other first is victorious. Death is defined as having health <= 0.

Each fighter will be a Fighter object/instance. See the Fighter class below in your chosen language.

Both health and damagePerAttack (damage_per_attack for python) will be integers larger than 0. You can mutate the Fighter objects.

Your function also receives a third argument, a string, with the name of the fighter that attacks first.'''

class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack
        
    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
    __repr__=__str__

def declare_winner(fighter1, fighter2, first_attacker):
    if fighter1.name == first_attacker:
        attacker, defender = fighter1, fighter2
    attacker, defender = fighter2, fighter1
    while True:
        defender.health -= attacker.damage_per_attack
        if defender.health <= 0:
            return attacker.name
        attacker, defender = defender, attacker
  


print(declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4),Fighter('Lew')))







print()

