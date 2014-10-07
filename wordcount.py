

word_counter = {}
def main():

    f=open('twain.txt')

    for line in f:
        #line = line.strip(string.punctuation)
        line = line.strip()
        words = line.split()
      
        for anyword in words:
            word_count=word_counter.get(anyword, 0) + 1
            word_counter[anyword]=word_count

       # print words

    for words in sorted(word_counter):
        print words, word_counter[words] 

if __name__ == "__main__":
    main()