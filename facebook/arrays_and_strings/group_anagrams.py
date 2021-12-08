# Author: Shyama Arunachalam


def groupAnagrams(strs):
    groups = {}
    for word in strs:
        sorted_list = sorted(word)
        sorted_word = ''
        for letter in sorted_list:
            sorted_word = sorted_word + letter
        if sorted_word not in groups:
            groups[sorted_word] = [word]
        else:
            groups[sorted_word].append(word)
    clusters = []
    for key, group in groups.items():
        clusters.append(group)
    return clusters

strs = ["eat","tea","tan","ate","nat","bat"]
grouped = groupAnagrams(strs)
print(grouped)
