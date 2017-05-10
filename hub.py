import sys


print()
file = ""
use_tt = False
use_lsa = False
f_measure = 0
for i in sys.argv:
    if str(i).startswith("-file"):
        file = str(i).split("=")[1]

    if str(i).startswith("-lsa+tt"):
        use_lsa = True

    if str(i).startswith("-tt"):
        use_tt = True


print(file)
print(use_lsa)
print(use_tt)

