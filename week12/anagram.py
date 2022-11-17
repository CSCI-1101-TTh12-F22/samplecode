
# Treate your dictionary that maps strings of unique
# sorted letters to a list of words containing all
# of those letters (possibly more than once).
wordlist = {}

# Turn every word into a sorted, uniqued string of characters
# then have that as the key for a value that is a list of
# all words with that sorted, uniqued string of characters.
# ex: DICTATE => ACDEIT
def buildanagramlist():
    f = open("cmudict-utf8.txt")

    # read in dictionary of English and get first field
    for line in f:
        parts = line.split()
        word = parts[0]

        # if the word is longer than 3 and is all letters
        if len(word) > 3 and word.isalpha():

            # get the set of letters and then turn it into a list again
            letterlist = list(set(word))

            # sort that list of letters
            letterlist.sort()

            # turn that into a string, and make it the key
            stringword = "".join(letterlist)

            # add the current word to the list of possible
            # words for that key
            if stringword in wordlist:
                wordlist[stringword].append(word)
            else:
                wordlist[stringword] = [word]
            
            

    f.close()



# Turn your intput word into a sorted, uniqued string of characters.
# Look it up and print out all the anagrams.
def findanagram(s):
    # get the set of letters and then turn it into a list again
    letterlist = list(set(s))

    # sort that list of letters
    letterlist.sort()

    # turn that into a string, and make it the key
    stringword = "".join(letterlist)    

    print(stringword)
    # print it out

    # if the word (uppercase) is in the wordlist
    # print out all of its anagrams
    if stringword.upper() in wordlist:
        print(" ".join(wordlist[stringword.upper()]))
    else:
        print("no anagrams")

    # otherwise print "no anagrams"


def main():
    buildanagramlist()
    findanagram(input("Enter a word to find anagrams: "))

main()
                 
