beatles = []

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

new_members = ["Stu Sutcliffe", "Pete Best"]

for i in new_members:
    beatles.append(i)

print("\nHere is the updated Beatles:", beatles)

del beatles[-1]
del beatles[-1]
print("\nHere is the updated Beatles:", beatles)

beatles.insert(0, "Ringo Starr")

print("\nHere is the updated Beatles:", beatles)