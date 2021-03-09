import re

def nth_most_common_words(path, n):
    words = get_words(path)
    word_counts = count_words(words)
    return
def count_words(word_list):
    pass
   
def get_words(path):
    words = []
    for line in open(path):
        pass

def  word_probability(path, word):
    words = get_words(path)
    word_counts = count_words(words)
    
    return

def main():
    path = "test.txt"


    words = nth_most_common_words(path, n)
    print(words)

    prob = word_probability(path, word)
    print(prob)
    

if __name__ == "__main__":

    path = open("test.txt")
    
    file = close()
    
    words = nth_most_common_words(path, n)
    print(words)

    prob = word_probability(path, word)
    print(prob)
