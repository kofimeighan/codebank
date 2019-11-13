# kofi meighan/km3547 & isabella arevalo/ia2422
def count_ngrams(filename, n=2): 
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~''' 
    f = open(filename,'r')
    story_string = []
    for line in f:
        for word in line.split():
            lowercase = word.lower().strip(punctuation)
            story_string.append(lowercase)
    
    ngram_list = []
    for i in range((len(story_string))-n+1):
        ngram_string = story_string[i:i+n]
        ngram_list.append(ngram_string)
    ngram_count_dict = {}
    print(ngram_list)

    ngram_tuple = []
    for i in ngram_list:
        ngram_tuple.append(tuple(i))
    print(ngram_tuple)
    
    for i in ngram_tuple:
        if i not in ngram_count_dict:
            ngram_count_dict[i] = 1
        elif i in ngram_count_dict:
            ngram_count_dict[i] += 1
    return ngram_count_dict


def single_occurences(ngram_count_dict): 
    single_ngrams = []
    for i in ngram_count_dict:
        if ngram_count_dict[i] == 1:
            single_ngrams.append(i)
    return single_ngrams


def most_frequent(ngram_count_dict, num = 5):
    frequency_to_n = []
    frequency_list = []
    for key in ngram_count_dict:
        frequency_to_n.append((ngram_count_dict[key],key))
    
    frequency_to_n.sort(reverse = True)
    
    x = 0
    while num > x:
        frequency_list.append(frequency_to_n[x][1])
        x += 1
    
    return frequency_list

def main():
    filename = "alice.txt"
    n = 3
    most_frequent_k = 5

    ngram_counts = count_ngrams(filename, n)

    print('{}-grams that occur only once:'.format(n))
    print(single_occurences(ngram_counts))

    print('{} most frequent {}-grams:'.format(most_frequent_k, n))
    print(most_frequent(ngram_counts, most_frequent_k))

if __name__ == "__main__":
    main()
