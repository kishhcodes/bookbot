def get_words_count(file_contents):
    file_contents = file_contents.lower()
    words = file_contents.split()
    return len(words)
    
def word_dictionary(file_contents):
    file_contents = file_contents.lower()
    words = file_contents.split()
    
    count_dict = {}
    for word in words:
        for w in word:
            if w not in count_dict:
                count_dict[w] = 1
            else:
                count_dict[w] += 1

    return count_dict


def sort_on(items):
    return items["num"]

def sort_it(file_contents):
    count_dict = word_dictionary(file_contents)
    reslist = []

    for key, value in count_dict.items():
        item = {"char": key, "num": value}
        reslist.append(item)
    reslist.sort(reverse=True, key=sort_on)
    
    return reslist
