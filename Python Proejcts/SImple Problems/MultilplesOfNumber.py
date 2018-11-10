
##This prints the sum of the multiples of numbers range between 1 to 1000
# For this program the int are 3 and 5

def main():
    num1=int(input('Give me first number: '))
    num2=int(input('Give me second number: 2'))
    sum=0


    for i in range(1,1000):
        mod1=i%num1;
        mod2=i%num2;
        if(mod1==0 or mod2==0):
            sum=sum+i


    print(sum)



if __name__=='__main__':
    main()


