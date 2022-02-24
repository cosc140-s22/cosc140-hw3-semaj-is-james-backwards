#######################################################
#
# COSC 140 Homework 3: ghost
#
#######################################################

def load_wordlist():
    '''
    Function written for you that reads contents of words.txt and 
    returns a list of words, each word in uppercase.
    '''
    wordlist = []
    with open("words.txt") as infile:
        for line in infile:
            wordlist.append(line.strip().upper())
    return wordlist

def main():
    words = load_wordlist()
    print(f"{len(words)} words loaded.")

    # you can start your code here, inside main

main()
