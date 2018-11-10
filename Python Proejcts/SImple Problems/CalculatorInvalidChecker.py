import math


def main():
    print('Calculator');
    calculation();


def inputCheck():
    canContinue = True;
    while canContinue:
        inpt1 = input('Give a number:')
        num = 0;
        try:
            num = int(inpt1);
            '''try:
                inpt2=input('Give a number:')
                num2=int(inpt2);
            except:
                print('This input is invalid.');'''
        except:
            print('This input is invalid.');
        else:
            return num;
            canContinue = False;


def calculation():
    canContinue = True;
    num1 = inputCheck();
    num2 = inputCheck();
    while canContinue:
        print('(1) +');
        print('(2) -');
        print('(3) *');
        print('(4) /');
        print('(5)sin(number1/number2)');
        print('(6)cos(number1/number2)');
        print('(7)Change numbers');
        print('(8)Quit');
        print('Current numbers:' + str(num1) + ' ' + str(num2));
        operation = input('Please select something (1-6):');
        if (operation == '8'):
            print('Thank you!');
            canContinue = False;
        elif (operation == '1'):
            add = num1 + num2;
            print('The result is:' + str(add));
            continue;
        elif (operation == '2'):
            sub = num1 - num2;
            print('The result is:' + str(sub));
            continue;
        elif (operation == '3'):
            multiply = num1 * num2;
            print('The result is:' + str(multiply));
            continue;
        elif (operation == '4'):
            divide = num1 / num2;
            print('The result is:' + str(divide));
            continue;
        elif (operation == '5'):
            intoSin = math.sin(num1 / num2);
            print('The result is:' + str(intoSin));
            continue;
        elif (operation == '6'):
            intoCos = math.cos(num1 / num2);
            print('The result is:' + str(intoCos));
            continue;
        elif (operation == '7'):
            num1 = inputCheck();
            num2 = inputCheck();
            continue;
        else:
            break;


if __name__ == "__main__":
    main()

