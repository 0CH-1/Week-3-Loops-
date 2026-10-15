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