'''
A file for the production code
'''
import sys


def reverse_word(word):
    return word[::-1]

def reverse_all_words(phrase):
    words = phrase.split()
    reversed_words = [reverse_word(word) for word in words]
    return ' '.join(reversed_words)
    
def main():
    phrase = sys.argv[1]
    print(reverse_all_words(phrase))

if __name__ == "__main__":
    main()