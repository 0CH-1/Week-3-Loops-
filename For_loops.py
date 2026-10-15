print("How many mountains should I display? ")
mountains=int(input())
print("Displaying...")

for mountain in range(mountains):
    print(print("""
               ___
              /   \\_
             /^     \\
            /  ^     \\_
          _/ ^ ^       ^\\
         / ^        ^    \\
"""))

#ask the user for distance
print("How far are we from the target? ")
distance=int(input())
print()
for count in range(distance,0,-1):
    print(f"{count} steps remaining")
print("Target achieved")

#asking user for brightness level
print("What level of brightness is required? ")
brightness=int(input())
print("\nAdjusting brightness...\n")
for brightness in range(2, brightness +1, 2):
    print(f"Brightness level: {'*' * brightness}")
print("Complete")

#asking the user for a word
print("What word do you see?")
word=input()
print("\nDisplaying index options...\n")
for count in range(0, len(word),1):
    print(f"index: {count}:", word[count])
print("Done!")

