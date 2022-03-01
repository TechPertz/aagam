import json

def number_to_string(inp, data):
    match inp:
        case 1:
            year(data)
        case 2:
            name(data)
        case 3:
            yearcat(data)
        case 4:
            alphabetically(data)

def year(data):
    inp = input("Year: ")

    for i in data['prizes']:
        if i['year'] == inp:
            for j in i['laureates']:
                print(j['firstname'] + ' ' + j['surname'])

def name(data):
    inp = input("Name: ")

    for i in data['prizes']:
        for j in i['laureates']:
            if (j['firstname'] + ' ' + j['surname']) == inp:
                print(i['year'] + ' ' + i['category'])

def yearcat(data):
    year = input("Year: ")
    category = input("Category: ")

    for i in data['prizes']:
        if i['year'] == year and i['category'] == category:
            for j in i['laureates']:
                print(j['firstname'] + ' ' + j['surname'])

def alphabetically(data):
    lst = []

    for i in data['prizes']:
        for j in i['laureates']:
            lst.append(j['firstname'] + ' ' + j['surname'] + ' ' + i['year'] + ' ' + i['category'])

    lst.sort()

    for i in lst:
        print(i)

def main():
    with open('prize.json') as json_file:
        data = json.load(json_file)

    menu = {1 : "Search By Year", 2: "Search by Name", 3: "Search by Year and Category", 4: "Alphabetical order"}

    for key,value in menu.items():
        print(key, ":", value)

    inp = int(input("Enter A nos: "))
    number_to_string(inp, data)


if __name__ == "__main__":
    main()