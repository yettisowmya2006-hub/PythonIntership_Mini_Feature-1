P=[]
for i in range(2):
    name = str(input("Enter Name"))
    role = str(input("Enter Role"))
    P.append((name,role))
    print(f"Hello{name},your role is {role}")
    print(P)

for i in P:
    print(i)


P = []

while True:

    print("\n1.ADD")
    print("2.VIEW")
    print("3.INSERT")
    print("4.REMOVE")
    print("5.POP")
    print("6.COUNT")
    print("7.EXIT")

    ch = input("Enter Choice: ")

    # ADD
    if ch == "1":

        name = input("Enter Name: ")
        role = input("Enter Role: ")

        P.append((name, role))

        print("Added")

    # VIEW
    elif ch == "2":

        print(P)

    # INSERT
    elif ch == "3":

        pos = int(input("Enter Position: "))

        name = input("Enter Name: ")
        role = input("Enter Role: ")

        P.insert(pos, (name, role))

        print("Inserted")

    # REMOVE
    elif ch == "4":

        name = input("Enter Name to Remove: ")

        for i in P:
            if i[0] == name:
                P.remove(i)

        print("Removed")

    # POP
    elif ch == "5":

        P.pop()

        print("Last Item Deleted")

    # COUNT
    elif ch == "6":

        print("Total:", len(P))

    # EXIT
    elif ch == "7":

        print("Thank You")
        break

    else:
        print("Invalid Choice")



        movies = []

n = int(input("How many movies: "))

for i in range(n):
    name = input("Enter Movie Name: ")
    rating = float(input("Enter Rating: "))

    movies.append((name, rating))

    print(f"{name} movie rating is {rating}")

print("\nMovie List:")

for i in movies:
    print(i)

