s = input().strip()
a = []

for i in range(0, len(s) - 1, 2):
    t = int(s[i:i+2])
    a.append(t)

unique_sorted_numbers = sorted(set(a))

print(" ".join(map(str, unique_sorted_numbers)))
