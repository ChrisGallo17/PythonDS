# Given an array of strings, group anagrams together.

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
strs2 = ["eat", "tan", "ate"]
strs3 = ["hos", "boo", "nay", "deb", "wow", "bop", "bob", 
        "brr", "hey", "rye", "eve", "elf", "pup", "bum", "iva",
        "lyx", "yap", "ugh", "hem", "rod", "aha", "nam", "gap",
        "yea", "doc", "pen", "job", "dis", "max", "oho", "jed",
        "lye", "ram", "pup", "qua", "ugh", "mir", "nap", "deb",
        "hog", "let", "gym", "bye", "lon", "aft", "eel", "sol",
        "jab"] 

from collections import defaultdict
def groupAnagrams(strs):
    group = defaultdict(list)
    for i in strs:
        sorted_string = ''.join(sorted(i))
        group[sorted_string].append(i)
    print(group)
    return group.values()

groupAnagrams(strs)