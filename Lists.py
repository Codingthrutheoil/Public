beatles = [] # step 1

print("Step 1:", beatles)

beatles.append("John Lennon")

beatles.append("Paul McCartney")

beatles.append("George Harrison") # step 2

print("Step 2:", beatles)

for i in range (2):
    beatles.append(input("Please key in a band member: ")) # step 3

print("Step 3:", beatles)

for i in range (2):
    del(beatles[-1]) # step 4

print("Step 4:", beatles)

beatles.insert(0, "Ringo Starr") # step 5

print("Step 5:", beatles)

# testing list legth
print("The Fab", len(beatles))
