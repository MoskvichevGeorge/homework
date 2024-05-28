def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if root_word in word or word in root_word:
            same_words.append(word)
    return same_words


root_word = 'rich'
other_words = ['richiest', 'orichalcum', 'cheers', 'richies']
result = single_root_words(root_word, *other_words)
print(result)
