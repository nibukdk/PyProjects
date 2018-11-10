import random


def game():
    winCounter = 0;
    roundCounter = 0;
    lossCounter = 0;
    tieCounter = 0;
    startGame = True;
    while startGame:
        usrChoice = input('Foot, Nuke or Cockroach? (Quit ends):');
        compValue = compChoice();
        if (usrChoice == compValue):
            onTie(lossCounter, usrChoice, compValue);
            tieCounter = tieCounter + 1;
            roundCounter = roundCounter + 1;
            continue;
        elif (usrChoice == 'Cockroach'):
            if (compValue == 'Foot'):
                onLoss(lossCounter, usrChoice, compValue);
                lossCounter = lossCounter + 1;
                roundCounter = roundCounter + 1;
            else:
                onWin(winCounter, usrChoice, compValue);
                winCounter = winCounter + 1;
                roundCounter = roundCounter + 1;
            continue;
        elif (usrChoice == 'Nuke'):
            if (compValue == 'Cockroach'):
                onLoss(lossCounter, usrChoice, compValue);
                lossCounter = lossCounter + 1;
                roundCounter = roundCounter + 1;
            else:
                onWin(winCounter, usrChoice, compValue);
                winCounter = winCounter + 1;
                roundCounter = roundCounter + 1;
            continue;
        elif (usrChoice == 'Foot'):
            if (compValue == 'Nuke'):
                onLoss(lossCounter, usrChoice, compValue);
                lossCounter = lossCounter + 1;
                roundCounter = roundCounter + 1;
            else:
                onWin(winCounter, usrChoice, compValue);
                winCounter = winCounter + 1;
                roundCounter = roundCounter + 1;
            continue;
        elif (usrChoice == 'Quit'):
            print('You played ' + str(roundCounter) + ' rounds, and won ' + str(
                winCounter) + ' rounds, playing tie in ' + str(tieCounter) + ' rounds.');
            startGame = False;
        else:
            print('Incorrect Selection.');
            continue;


def compChoice():
    computerChoice = '';
    randInt = random.randint(1, 3);
    if (randInt == 1):
        computerChoice = 'Foot';
    elif (randInt == 2):
        computerChoice = 'Nuke';
    else:
        computerChoice = 'Cockroach';
    return computerChoice;


def onWin(winCounter, usrChoice, compValue):
    winCounter = 1;
    print('You chose:', usrChoice);
    print('Computer chose:', compValue);
    print('You WIN!');
    return winCounter;


def onTie(tieCounter, usrChoice, compValue):
    tieCounter = 1;
    print('You chose:', usrChoice);
    print('Computer chose:', compValue);
    print('It is a TIE!');
    return tieCounter;


def onLoss(lossCounter, usrChoice, compValue):
    lossCounter = 1;
    print('You chose:', usrChoice);
    print('Computer chose:', compValue);
    print('You LOSE!');
    return lossCounter;


def main():
    game();


if __name__ == "__main__":
    main();
