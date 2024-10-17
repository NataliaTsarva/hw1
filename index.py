
# Упражнение 1

digits = [5, 2, 3]
digits2 = sorted([i**2 for i in digits])

print(digits)
print(digits2)

# Упражнение 2

tpl = (1, 2, 3, 4, 5, 6, 7)

print (tpl[-1])

# Упражнение 3

tpl1 = (1, 2, 3)
tpl2 = tpl1[:-1] + (4,)
print(tpl1)
print(tpl2)

# Упражнение 4

my_string = 'Hello Kitty'
my_list = list(my_string)
print(my_list[-2], my_list[-1])


# Упражнение 5

s1 = 'abcdabcd'
s2 = 'cdcdef'

for i in s1:
    for i in s2:
        s3 = set(s1).intersection(set(s2))
print(len(s3))

