def game(m1, b1, numberOfRounds, rounds):
    totalMoney = int(m1)
    betAmount = int(b1)
    for i in rounds:
        if i == '0':
            totalMoney = totalMoney - betAmount
            betAmount = min(2 * betAmount, totalMoney)
            if totalMoney == 0:
                return "BROKE"
            print("lala", totalMoney)
        if i == '1':
            totalMoney = totalMoney + betAmount
            betAmount = min(int(b1), totalMoney)
            print("oooo", totalMoney)
    return totalMoney

if __name__ == "__main__":

    m1 = input()
    b1 = input()
    numberOfRounds = int(input()) 
    rounds = input().split()
    print(game(m1, b1, numberOfRounds, rounds))
    

