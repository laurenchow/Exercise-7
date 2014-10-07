#import string

def read_data_from_file():

    word_list=[]
    word_counter = {}

    f=open('twain.txt')

    for line in f:
        line = line.strip()
        print type(line)
        words = line.split()

        for anyword in words:
            word_count=word_counter.get(anyword, 0) + 1
            word_counter[anyword]=word_count
    
    return word_counter, word_list
    

def remove_punctuation():
    pass
    
def print_word_counts(word_list, word_counter):

    for words in sorted(word_counter):
        print word_list, word_counter[words] 

    print word_list, word_counter

def main():
  
    word_list, word_counter=read_data_from_file() 
    remove_punctuation()
    print_word_counts(word_list, word_counter)
    
if __name__ == "__main__":
    main()