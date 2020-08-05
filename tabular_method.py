# change decximal to 4bit binary
def dec2bin(n):
    result = ['0','0','0']    
    bStr = ""
    if n < 0 :
        raise ValueError, "must be a positive integer"

    if n == 0 :
        return '0000'

    while n > 0 :
        bStr = str( n % 2 ) + bStr
        n = n // 2
    
    result.extend(list(bStr))
    while (len(result) != 4):
        del result[0]

    return ''.join(result)

# to get HD
def hammingDistance(a, b):
    count = 0
    first = []
    second = []
    first.append(dec2bin(a))
    second.append(dec2bin(b))

    for i in range(0,4):
        if (first[i] != second[i]):
            count += 1

# count # of 1 for each terms     
def numOfones(num):
    numcount = 0

    for i in num:
        if (int(i) == 1):
            numcount += 1
    return numcount

def primeImplicants(term):
    sortedTerms = []      # ['0000'], ['0101'], ['0001'] ...... ['1111']
    
    for i in range(0,16):
        if(numOfones(term) == i):
            sortedTerms[i].append(numOfones(term))
    print(sortedTerms)

def main():
    #input to strings
    minterms = raw_input("(ex, 0 1 2 3 4 5 6) >>> ")
    minterms = minterms.split(" ")
    for minterm in minterms:
        binary = dec2bin(int(minterm))
        primeImplicants(binary)

if __name__ == "__main__":
    main()
