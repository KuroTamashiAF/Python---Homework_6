
def view(data):
    print(data)


def enter_from_user():
    with open('input.txt','r') as data:
        user_data = data.read()          # не нашел любтмого отрывка из Война и мир, где Пьер Безухов пытается 
    return user_data                     # убить свою жену, так что вставил рандомный из 1 тома  
