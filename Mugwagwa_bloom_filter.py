#My name is Charles Mugwagwa. This is an implementation of a bloom filter.

#I decided to use 8 hash functions and 1259350 for the number of bits for the bitarray(). 
#p(the desired probability) was given as being less than 0.5%, so I used 0.4%.
#n (the number of items inserted into the bloom filtered) was the count of the words in the dictionary which is 109 583.
#The number of bits(m) for the bitarray was calculated using the formular m = -(nlnp)/((ln2)**2)
#The number of hash functions(k) was calculated using the formular k = (m/n)ln2

from bitarray import bitarray

class hashFunction:
    def __init__(self, string):        
        self.string = string
        
    def hashIt(self, item):
        return hash(item+self.string) 

class BloomFilter:    
    def __init__(self, numOfHashFunctions, numOfBits):
        self.numOfBits = numOfBits
        self.hashSet = set()
        self.array = bitarray(numOfBits)
        for y in range(numOfBits):#setting all bits to 0/false. 
            self.array[y] = False                
        for x in range(numOfHashFunctions): 
            self.hashSet.add(hashFunction(str(x))) 
            
    def __str__(self):
        return self.array.__str__()
            
    def insert(self, item):        
        for x in self.hashSet: #x = hashFunction            
            index = (x.hashIt(item))% self.numOfBits            
            self.array[index] = True #turning on the bits      
        
    def __contains__(self, item):        
        membership = True
        for x in self.hashSet: #x = hashFunction            
            index = (x.hashIt(item))% self.numOfBits            
            if self.array[index] == False: 
                membership = False
        return membership
    
def main():   
    m = 1259350
    k = 8
    bf = BloomFilter(k,m)
    
    file = open('wordsEn.txt','r')
    for line in file:
        bf.insert(line)
    file.close()
    
    file = open('declaration_of_independence.txt','r')              
    lineCount = sum(1 for line in file) #includes blank lines   
    file.seek(0) 
    for t in range(lineCount):
        line = file.readline()
        if line != "":
            splitLine = line.split()            
            for word in splitLine:                
                if word[-1]==',' or word[-1]=='.' or word[-1]==';' or word[-1]==':':
                    word = word[:-1]
                word = word.lower()+'\n'                
                if word not in bf:
                    print(word)
                
if __name__ == '__main__':
    main()