def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    s_temp = s
    t_temp = list(t)
    for i in s:
        if i in t_temp:
            t_temp.remove(i)
    print(t_temp)
    return (len(t_temp) == 0)


print(isAnagram("nagaram", "anagram"))