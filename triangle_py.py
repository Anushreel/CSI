# Question - Create lower triangular, upper triangular and pyramid containing the "*" character.

size=int(input("enter the number rows in the triangle: "))
print("*** LOWER TRIANGLE ***")
print("\n")
for i in range(1,size+1):
    print(" * "*i)

print("\n")

print("*** UPPER TRIANGLE ***")
print("\n")
for i in range(size,0,-1):
    print("   "*(size-i)+" * "*i)

print("\n")

print("*** PYRAMID ***")
print("\n")
for i in range(1,size+1):
    print("   "*(size-i)+" * "*(2*i-1))