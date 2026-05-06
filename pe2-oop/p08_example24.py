string = input("Enter a string: ")
count_a = 0

# Count occurrences of 'a' (case-insensitive)
for char in string.lower():
  if char == 'a':
    count_a += 1

print(f"Number of 'a' characters: {count_a}")
