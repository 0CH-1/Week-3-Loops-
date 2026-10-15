#number of apples to be removed
print ("How many apples should I remove? ")
apples_to_remove= int(input())

#control variable
apples_removed= 0

#removing apple

print()
while apples_removed<apples_to_remove:
 print("Removed apple.")
 apples_removed = apples_removed+1


#number of obstacles to avoid
print ("How many obstacles should I avoid?")
obstacles_to_avoid=int(input())
obstacles_avoided=0
print()
while obstacles_avoided<obstacles_to_avoid:
 print("Avoiding...", end="")
 obstacles_avoided= obstacles_avoided+1
 print(f"Done! {obstacles_avoided} obstacles avoided.")
