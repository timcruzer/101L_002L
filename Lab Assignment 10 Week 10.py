import os
import string

def words():
    x = 1

    print("Most frequently used words")
    print("{:<}{:^20}{:>}".format("#", "Word", "Freq."))
    print("=" * 26)

    for key, value in dic.items():
        print("{:<3}{:<22}{:>}".format(x, key, value))
        x += 1
        
        if x > 10:
            break
    print()
    print(f"There are {single} words that occur only once")
    print(f"There are {unique} unique words in the document")

def grab(file):
    global dic
    global unique
    global single
    
    for line in file:
        for word in line.split():
            exclude = set(string.punctuation)
            word = "".join(ch for ch in word if ch not in exclude)
            word = word.lower()
            if len(word) > 3:
                if word in dic:
                    dic[word] += 1
                else:
                    dic[word] = 1
                    unique += 1

    for value in dic.values():
        if value == 1:
            single += 1

    dic = dict(sorted(dic.items(), key = lambda item: item[1], reverse = True))

    return
    
    

if __name__ == "__main__":
    using = True

    while using == True:
        global dic
        global single
        global unique
        dic = {}
        single = 0
        unique = 0

        try:
            file = input("Enter the name of the file to open: ")
            here = os.path.dirname(os.path.abspath(__file__))
            file = os.path.join(here, file)
            with open(file) as f:
                grab(f)
                words()
                
            using = False
        except FileNotFoundError:
            print("Could not open file", file)
            print("Please try again")