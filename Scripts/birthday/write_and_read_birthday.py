def write_birthday(name, birthday, sign):
    with open('Scripts/birthday/user_data.txt', 'w') as f:
        f.write(f"{name}:{birthday}:{sign}")


def read_birthday():
    with open('Scripts/birthday/user_data.txt', 'r') as f:
        f = f.readline()
        data_user = f.split(':')

    return data_user
