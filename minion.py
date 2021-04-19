from card import Card
# child class inherit from parents class
class Minion(Card):
    def __init__(self, name, cost, attackPoints, healthPoints):
        Card.__init__(self, name, cost)
        self.attackPoints = attackPoints
        self.healthPoints = healthPoints
    def printCard(self):
        Card.printCard(self); # go into card class
        print('Attack Point: ', self.attackPoints)
        print('Health Point: ', self.healthPoints)