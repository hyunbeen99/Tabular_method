class TabularMethod:
    def __init__(self):
        self.checkPI = []
        self.sortedTerm = []
        self.binlist = []

    # change decximal to 4bit binary
    def dec2bin(self,n):
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
    def hammingDistance(self,a, b):
        count = 0
        firstTerm = list(a)
        secondTerm = list(b)

        for i in range(0,4):
            if (firstTerm[i] != secondTerm[i]):
                count += 1
        return count

    # count # of 1 for each terms     
    def numOfones(self,num):
        numcount = 0
        for i in num:
            if (int(i) == 1):
                numcount += 1
        return numcount
    
    def binary(self, bin1, bin2):
        firstBin = list(bin1)
        secondBin = list(bin2)
        resultBin = []

        for i in range(0,4):
            if (firstBin[i] == secondBin[i]):
                resultBin.append(i)
            else:
                resultBin.append('-')
        return str(resultBin)

    # set terms in order of the numOfones in each terms before grouping
    def sortingTermList(self,term):
    
        # in case of # of 1
        for i in range(len(term)):
            self.sortedTerm.append({self.numOfones(term[i]) : term[i]})
            self.sortedTerm.sort()

        #return sortedTerm

    def primeImplicants(self):
        for i in self.sortedTerm:
            for j in self.sortedTerm:
                if (self.hammingDistance(i.value(), j.value()) == 1):
                    self.checkPI.append(binary(i.value(), j.value())
        print(self.checkPI)


    def main(self):
        #raw_input; input minterms to strings
        minterms = raw_input("(ex, 0 1 2 3 4 5 6) >>> ")
        donCares = raw_input("(ex, 0 1) >> ")
        minterms = minterms.split(" ")
        donCares = donCares.split(" ")

        minterms.extend(donCares)

        for minterm in minterms:
            binary = self.dec2bin(int(minterm))
            self.binlist.append(binary)

        self.sortingTermList(self.binlist)
        self.primeImplicants()

if __name__ == "__main__":
    tabular = TabularMethod()
    tabular.main()
