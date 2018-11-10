def arrayMaker():
    openFile = open('words.txt', 'r');
    readFile = openFile.readlines();
    fileList = [];
    for i in readFile:
        fileList.append(i.rstrip());
    return fileList;


def main():
    receivedFile = arrayMaker();
    receivedFile.sort();
    print('Words in an alphabetical order:');
    for i in receivedFile:
        print(i);


if __name__ == '__main__':
    main();

