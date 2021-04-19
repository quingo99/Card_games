from card import Card
from minion import Minion

def main():

    deck = []

    cards = open("Cards.txt", 'r')
    
    for card in cards:
        cardInfo = card.split(',')
        lengthOfList = len(cardInfo)
        nameOfCard = cardInfo[0]
        costOfCard = cardInfo[1]

        if lengthOfList == 2:
            cardData = Card(nameOfCard, costOfCard)
        if lengthOfList == 4:
            attackPoint = cardInfo[2]
            healthPoint = cardInfo[3]
            cardData = Minion(nameOfCard, costOfCard, attackPoint, healthPoint)
        deck.append(cardData)

    cards.close()
    
    for card in deck:
        card.printCard()
        print("\n")

if __name__== "__main__":
    main()
    # acornBearer = Minion('Acorn Bearer', 1, 2, 1)
    # deck.append(acornBearer)

    # crystalPower = Card('Crystal Power', 1)
    # deck.append(crystalPower)

    # razorBoar = Minion('Razor Boar', 2, 2, 2)
    # deck.append(razorBoar)

    # vileCall = Card('Vile Call', 3)
    # deck.append(vileCall)

    

