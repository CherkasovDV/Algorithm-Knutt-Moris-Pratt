def prefix(s):
    pi = [0 for _ in range(len(s))]
    for i in range(1, len(s)):
        j = pi[i-1]
        while j > 0 and s[i] != s[j]: 
            j = pi[j-1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi

def kmp(P,T):
    pl, tl = len(P), len(T)
    res = [0] * tl
    p = prefix(P + "#" + T)
    count = 0
    for i in range(tl):
        if p[pl + i + 1] == pl:
            count += 1
            res[count] = i - pl
    return count, res

print('Строка:', 'ATATCCATC')
print('Подстрока:', 'ATC')
print(len('ATATCCATC'))
counter, arr = kmp('ATC', 'ATATCCATC')
print(arr)
print('Число вхождений подстроки в строку:', counter)
print('Индексы вхождений:')
print(', '.join([str(item) for item in arr[1:counter+1]]))
