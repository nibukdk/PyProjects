import time


def gameStart():
    canStart = True;
    while canStart:
        print('(1) Read the notebook');
        print('(2) Add note');
        print('(3) Empty the notebook');
        print('(4) Quit');
        usrInpt = int(input('Please select one:'));
        if (usrInpt == 1):
            readNote();
            continue;
        elif (usrInpt == 2):
            writeNote();
            continue;
        elif (usrInpt == 3):
            emptyNote();
            continue;
        elif (usrInpt == 4):
            print('Notebook shutting down, thank you.');
            canStart = False;
        else:
            print('Wrong Selection');
            continue;


def writeNote():
    newText = input('Write a new note:');
    lenNewText = len(newText);
    # findLength=seek(lenNewText);
    newTextTime = newText + ':::' + time.strftime("%X %x");
    note = open('notebook.txt', 'a');
    note.write(newTextTime);
    note.close();


def readNote():
    readfile = open('notebook.txt', 'r');
    content = readfile.read();
    print(content);
    readfile.close();


def emptyNote():
    note = open('notebook.txt', 'w');
    note.close()


def main():
    gameStart();


if __name__ == "__main__":
    main();