# Find the sum of first prime factors of repunit of length 10ˆ9

import sympy

def main():

    lengthOfRepunit = 10**9
    repunit=int((lengthOfRepunit-1)/9)
    factors=[]
    primeFactors=[]
    sumOfPrimeFactors=0

    #Determine Factors of given repunit
    determineFactors(repunit, factors)

    #Separate prime factors from list of factors
    determinePrimeFactors(factors, primeFactors)

    #Determine sum of prime factors
    for z in range(0, len(primeFactors)):
        sumOfPrimeFactors=sumOfPrimeFactors+primeFactors[z]

    print(sumOfPrimeFactors)



def determineFactors(repunit, factors):
    for x in range(1, repunit):
        if (repunit % x == 0):
            factors.append(x)
def determinePrimeFactors(factors, primeFactors):
    for z in range(0, len(factors)):
        isPrime = sympy.isprime(factors[z])
        if (isPrime == True):
            primeFactors.append(factors[z])


if __name__ == '__main__':
    main()
