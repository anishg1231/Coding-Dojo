import random                      # import the random module
class Human(object):               # define a new Human class
    def __init__(self, clan=None): # define a parameter with a default value, clan
      print 'New Human!!!'
      # define attributes
      self.health = 100
      self.clan = clan
      self.strength = 3
      self.intelligence = 3
      self.stealth = 3
    # define methods
    def taunt(self):               # pass self into all methods to access attributes
      print "You want a piece of me?"
    def attack(self):
      self.taunt()                 # use the random module to generate a number when we attack
      luck = round(random.random() * 100)
      if(luck > 50):
        if(luck * self.stealth > 150):
          print 'attacking!'
          return True
        else:
          print 'attack failed'
          return False
      else:
        self.health -= self.strength
        print "attack failed"
        return False
