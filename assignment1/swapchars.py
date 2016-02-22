from collections import Counter

def swapchars(argv):
    #separate string into chars and determine most and least common char
    lst = list(argv)
    nospace = argv.replace(" ","")
    most = Counter(nospace).most_common(1)
    least = Counter(nospace).most_common()[-1]

    #swap most common char with least common char and vice versa
    for x in range(len(lst)):
        s = ""
        if lst[x] == " ":
            pass
        elif lst[x] == most[0][0]:
            lst[x] = least[0]
        elif lst[x] == least[0]:
            lst[x] = most[0][0]
    final = s.join(lst)
    return final

#print 
print swapchars("mississippi")