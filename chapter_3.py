# Strings in Python
# Strings are immutable, means cannot changed
# For String slicing in python it is done with [starting_index:ending_index]
# Example Given

# name = "Tehami"

# Positive Indexing starts from 0 till length -1

# Index = 012345

# In Positive Indexing if I want to get output 'eham' in my string
# print(name[1:5])

# Negative Indexing starts from -length till 0 minus 1

#Index = -6,-5,-4,-3,-2,-1

# word =  t, e, h, a, m, i

# In Negative Indexing if I want to get output 'eham' in my string
# print(name[-5:-1])


# String skipping in python
# Syntax [starting_index:ending_index: characters_to_skip]
string = "abcdefghijklmnopqrstuvwxyz"
print(string[:27:3])
print(string[:27:2])
print(string[:27:1])

# String Functions
# 1. Length syntax: len()
# 2. Check string ending with? syntax: endsWith()
# 3. Check string starting with? syntax: startsWith()
# 4. To capitalize the string? syntax: capitalize() 
# 5. To lowercase the string? syntax: lower() 
# 6. To uppercase the string? syntax: upper() 
# 7. To find the string or word? syntax: find() 
# 8. To count the string or word? syntax: count() 
# 9. To replace the string or word? syntax: replace() 


# Escape sequence characters
# \n - innserts a new line
# \t - gives spacing of tab
# \' - used to print singlequotes in string
# \" - used to print doublequotes in string
# \\ - used to print backslash in string