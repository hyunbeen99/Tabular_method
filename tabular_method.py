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
    firstTerm = list(a)
    secondTerm = list(b)

    for i in range(0,4):
        if (firstTerm[i] != secondTerm[i]):
            count += 1
    return count

# count # of 1 for each terms     
def numOfones(num):
    numcount = 0
    for i in num:
        if (int(i) == 1):
            numcount += 1
    return numcount

# set terms in order of the numOfones in each terms before grouping
def sortingTermList(term):
    sortedTerm = []
  
    for i in range(len(term)):
        sortedTerm.append({numOfones(term[i]) : term[i]})
        sortedTerm.sort()

    #return sortedTerm
    print(sortedTerm)


''' TODO
    setTermList();
    grouping();
    makePIchart();
    printPIchart();
    findEPInPI();
    printEPInPI();
    findlogic();
'''
def main():
    #raw_input; input minterms to strings
    binlist = []
    minterms = raw_input("(ex, 0 1 2 3 4 5 6) >>> ")
    donCares = raw_input("(ex, 0 1) >> ")
    minterms = minterms.split(" ")
    donCares = donCares.split(" ")

    minterms.extend(donCares)

    for minterm in minterms:
        binary = dec2bin(int(minterm))
        binlist.append(binary)

    sortingTermList(binlist)

if __name__ == "__main__":
    main()
