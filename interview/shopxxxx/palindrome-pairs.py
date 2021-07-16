def is_palindrome(check):
    return check == check[::-1]


def palindrome_pairs(input_array):
    words = {word: i for i, word in enumerate(input_array)}
    res = 0
    for word, k in words.iteritems():
        n = len(word)
        for j in range(n+1):
            pref = word[:j]
            suf = word[j:]
            if is_palindrome(pref):
                back = suf[::-1]
                if back != word and back in words:
                    res += k + words[back]
            if j != n and is_palindrome(suf):
                back = pref[::-1]
                if back != word and back in words:
                    res += k + words[back]
    return res
