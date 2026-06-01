def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    print("List of words with the first and last letter same \n", lst)
    return ctr
count = match_words(["abc", "cfc", "1221", "xyz", "mom"])
print("number of words having the first letter same: ", count)
