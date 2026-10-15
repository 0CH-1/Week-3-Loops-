#asking user how many rows
print("How many rows should I have? ")
rows=int(input())
print("How many columns should I have? ")
columns=int(input())

for row in range(0,rows,1):
    for column in range(0,columns,1):
        print(":-)", end="")
    print()


#asking the user for a sequence and marker
print("Please enter a sequence:")
sequence=input()
print("Please enter a character for the marker: ")
marker=input()

marker1=-1
marker2=-1

for position in range(0,len(sequence),1):
    letter=sequence[position]
    if letter==marker:
        if (marker1==-1):
            marker1=position
        else:
            marker2=position
print(f"The distance between the markers is {marker2 - marker1 -1}.")
