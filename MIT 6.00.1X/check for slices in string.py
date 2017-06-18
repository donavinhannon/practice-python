s = 'bobobob'
bobCount = 0

for i in range(len(s) - 2):
    if s[i:i+3] == 'bob':
        bobCount += 1
    else: continue

print('Number of times bob occurs is: ' + str(bobCount))
