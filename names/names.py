import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# duplicates = [i for i in names_1 if i in names_2]

# Gets all duplicates from each list and across lists in under 100th of a second. Wording is vague and doesn't specify
# if you should show ALL duplicates or only elements duplicated across lists. Each individual list has
# duplicates that aren't being reported in the starter code.
last_value = ""
for i, v in enumerate(sorted(names_1 + names_2)):
    if last_value == v:
        duplicates.append(v)
    last_value = v


# duplicates = list(set(names_1) & set(names_2))  # Stretch response

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
