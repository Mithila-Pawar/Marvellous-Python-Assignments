c = input("Enter character:")
def vowel(x):
    if(x == 'a'or x == 'e'or x == 'i' or x == 'o'or x == 'u'or x == 'A' or x == 'E'or x == 'I' or x == 'O' or x == 'U'):
        print("Vowels")
    else:
        print("Constant")   

    return c    

if __name__ == '__main__':
    vowel(c)