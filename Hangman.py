


def welcome():

    print("*"*5, "WELCOME TO HANGMAN", "*"*5)
    print("""
    ------------------
            |        |
            |        |
            O        |
           /|\       |
            |        |
           / \       |
                     |
    _Y_Y_Y_Y_Y_Y_Y_Y_|""")
    print("\n\t!!WARNING!!")
    print("\nA innocent person is being hanged to death, and only you can save him!!!")
    print("\nExecutioner is thinking of a word")
    print("\nHe will not be executd if you can guess all the character in the word that executioner is thinking.")
    print("\n\n!!! SAVE HIM !!!\n\n")


# In[26]:


def random_word():

    try:
        import nltk
        import sys
        from nltk.corpus import words
        import random
        nltk.download('words', quiet=True)
    except Exception as e:
        print("\nINSTALL DEPENDENICS")
        for exp in e.args:
            print("-> {}".format(exp))
        sys.exit()
    else:
        wordlist = words.words()
        random.shuffle(wordlist)
        wordlist = [w for w in wordlist if 5 <= len(w) <= 12][:200]
        return wordlist[random.randint(0, 200)]


def userguess(guess, word_user, word_sys):

    while guess in word_sys:
        index = word_sys.index(guess)
#         print(word_user,word_sys,life)
        word_user[index], word_sys[index] = word_sys[index], word_user[index]
    return(word_user, word_sys)


def main():

    welcome()
    word_sys = list(random_word())
    word_user = list("_" * len(word_sys))
    flag = False
    life = 5
    again = True
    while again:
        while life > 0:
            print(" ".join(char for char in word_user))
            while True:
                try:
                    guess = input("ENTER CHAR GUESS: ").lower()
                    assert len(guess) == 1
                    assert guess.isalpha()
                    break
                except:
                    print("Enter charaacter (a-z) or (A-Z)")
            if guess in word_sys:

                word_user, word_sys = userguess(guess, word_user, word_sys)
            else:
                life -= 1

            if "_" not in word_user:
                flag = True
                break
        if flag:
            print(" ".join(char for char in word_user))
            print("\n\n!!!THANK GOD!!!")
            print("\nYOU SAVED HIM")
        else:
            print("\n\nYOU LOST")
            print("\n\nHE IS DEAD")
        print("\n\n***Made with love by Ratnesh Kumar***")
        opt = input("\nWanna play again ^_^ (y/n)")
        again = True if opt == 'y' or opt == "Y" else False

if __name__ == '__main__':
    main()
