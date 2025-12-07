def word_count(text):
    return len(text.split())

def char_count(text):
    text = text.lower()
    char_dict = {}
    for char in text:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict
    
def sort_list(list):
    sorted_list = []
    for ch in list:
        if ch.isalpha():
            sorted_list.append({"char": ch, "num": list[ch]})
    
    def sort_on(items):
        return items["num"]
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list