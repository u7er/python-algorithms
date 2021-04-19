t = "другой"

p = [0]*len(t)
j = 0
i = 1

text = ''
import os
HERE = str(os.path.dirname(os.path.abspath(__file__)))
with open(HERE + '\\text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

while i < len(t):
    if t[j] == t[i]:
        p[i] = j+1
        i += 1
        j += 1
    else:
        if j == 0:
            p[i] = 0
            i += 1
        else:
            j = p[j-1]

print(p)

a = text
m = len(t)
n = len(a)

i = 0
j = 0
isFound = False
while i < n:
    if a[i] == t[j]:
        i += 1
        j += 1
        if j == m:
            isFound = True
            break
    else:
        if j > 0:
            j = p[j-1]
        else:
            i += 1

if i == n and not isFound:
    print(f"образ не найден {j} {i}")

print(f"образ найден на индексе {i}: {a[i-m-50:i-m]}{a[i-m:i].upper()}{a[i:i+50]}")
