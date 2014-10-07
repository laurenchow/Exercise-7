import string

def read_data_from_file():

    word_list=[]
    word_counter = {}

    f=open('twain.txt')

    for line in f:
        line = line.strip()
        words = line.split()

        for anyword in words: #why does this work when in same function but not when we break into different functions
            word_count=word_counter.get(anyword, 0) + 1
            word_counter[anyword]=word_count
    
    return word_counter, word_list
    

def remove_punctuation(word_list):

    for each_word in word_list:
        print type(each_word)

        if string.endswith("!"):
           word_list[each_word]=word_list[each_word].rstrip()

def print_word_counts(word_list, word_counter):

    for words in sorted(word_counter):
        print "This word %s happens %s times. \n"  % word_list[words], 
        word_counter[words] 

    #print word_list, word_counter[words]

def main():
  
    word_list, word_counter=read_data_from_file() 
    remove_punctuation(word_list)
    print_word_counts(word_list, word_counter)
    
if __name__ == "__main__":
    main()