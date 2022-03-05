from prettytable import PrettyTable


def find_item(arr):
    table1 = PrettyTable()
    table1.field_names = ["Name", "shop", "cost", "weight"]

    search = input("Type what to find: ")

    for i in range(0, len(arr)):
        if arr[i][0].lower() == search.lower():
            table1.add_row(arr[i])

    fieldname = 'ID'
    table1._field_names.insert(0, fieldname)
    table1._align[fieldname] = 'c'
    table1._valign[fieldname] = 't'
    for i, _ in enumerate(table1._rows):
        table1._rows[i].insert(0, i)
    print(table1)


def namesort(arr):
    name = []
    for i in range(0, len(arr)):
        name.append(arr[i][0])
    name.sort()
    new_arr = []
    for i in range(0, len(arr)):
        if i != len(arr) - 1 and name[i + 1] == name[i]:
            continue
        for j in range(0, len(arr)):
            if name[i] == arr[j][0]:
                new_arr.append(arr[j])

    update_list(new_arr)
    print("Sorted")


def change_value(arr):
    id = input("Type what product ID: ")
    if not (id.isnumeric() and 0 <= int(id) < len(arr)):
        print("Number is out of range")
        return
    print("Type new values")
    new_line = input("Name shop cost weight (for cost and weight use only numbers) \n")
    new_line = new_line.split()
    if len(new_line) != 4:
        print("Incorrect number of arguments")
        return
    new_line[2] = new_line[2] + "тыс.руб."
    new_line[3] = new_line[3] + "кг"
    for i in range(0, len(new_line)):
        arr[int(id)][i] = new_line[i]
    update_list(arr)
    print("Jobs done")


def update_list(arr):
    content = ""
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            content = content + arr[i][j] + "\t"
        content = content + "\n"
    f = open("list.txt", "w")
    f.write(content)
    f.close()


def add_record(arr):
    print("Type values separated by a space")
    line = input("Name shop cost weight (for cost and weight use only numbers) \n")
    line = line.split()
    if len(line) != 4:
        print("Incorrect input")
        return
    line[2] = line[2] + "тыс.руб."
    line[3] = line[3] + "кг"
    arr.append(line)
    update_list(arr)


def parse_file():
    with open("list.txt") as f:
        content = f.read()

    table = PrettyTable()
    table.field_names = ["Name", "shop", "cost", "weight"]

    arr = []
    lines = content.split('\n')
    for i in range(0, len(lines) - 1):
        arr.append(lines[i].split())
        table.add_row(arr[i])

    fieldname = 'ID'
    table._field_names.insert(0, fieldname)
    table._align[fieldname] = 'c'
    table._valign[fieldname] = 't'
    for i, _ in enumerate(table._rows):
        table._rows[i].insert(0, i)

    return arr, table


def save_to():
    with open("list.txt") as f:
        content = f.read()
    new_file_name = input("Type new file name: ")
    f = open(new_file_name, "w")
    f.write(content)
    f.close()
    print("Saved")


def print_menu():
    print("""Choose an option:
    1. print all products
    2. add
    3. change
    4. sort by name
    5. find product
    6. save to...
    
    0. to exit""")


def start():
    while True:
        print_menu()
        arr, table = parse_file()
        option = int(input(">:"))
        if option == 1:
            print(table)
        elif option == 2:
            add_record(arr)
        elif option == 3:
            print(table)
            change_value(arr)
        elif option == 4:
            namesort(arr)
        elif option == 5:
            find_item(arr)
        elif option == 6:
            save_to()
        elif option == 0:
            break
        else:
            print("Incorrect input")


if __name__ == '__main__':
    start()
