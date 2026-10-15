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


#number of bars
print("How many bars should be charged?")
bars_to_charge=int(input())
bars_charged=0
print()
while bars_charged<bars_to_charge:
 bars_charged=bars_charged +1
 print(f"Charging: {'█' * bars_charged}")
print("The battery is fully charged")


#asking the user for a phrase
print("Please enter a phrase: ")
phrase=input()

Hellos=0

print()
while Hellos< len(phrase):
 print("Hi ",end="")
 Hellos= Hellos+1