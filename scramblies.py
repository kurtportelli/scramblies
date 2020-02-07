def scramble(s1, s2):
    from collections import Counter
    dict1 = Counter(s1)
    dict2 = Counter(s2)
    for key in dict2:
        if dict2[key] > dict1[key]:
            return False
    return True
