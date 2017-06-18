arrays =[]

for i in range(len(s)):
    str = [s[i]]
    while i + 1 < len(s) and s[i] <= s[i+1]:
        str.append(s[i+1])
        i += 1
    arrays.append(str)

greatest_array = arrays[0]
for i in range(len(arrays)):
    if len(greatest_array) < len(arrays[i]):
        greatest_array = arrays[i]

greatest_substring = "".join(greatest_array)
print('Longest substring in alphabetical order is: ' + greatest_substring)