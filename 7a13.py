file_name = "name.txt"
names_list = []
names_file = open(file_name)
for name in names_file:
    name = name.strip().split(",")
    names_list.append(name)
names_file.close()

for name in names_list:
    first_name, last_name = name[1], name[0]
    name = f"{first_name} {last_name}".title()
    print(name)



