from mimetypes import read_mime_types

list = [['X', 'O', 'X'],
        ['O', 'X', 'O'],
        ['O', 'X', 'O']]


def find_winner():
    for i in range(len(list) - 1):
        if list[i][0] == list[i][1] == list[i][2]:
            print(list[i][0] + " Wins")
            break
        if list[0][i] == list[1][i] == list[2][i]:
            print(list[0][i] + " Wins")
            break

    x = 0

    while x < len(list) - 1:
        if list[x][x] == list[x + 1][x + 1]:
            if x == len(list) - 1:
                print(list[x][x] + " Wins")
                break
            x += 1
        else:
            break

    x = len(list) - 1
    i = 0

    while i < len(list) - 1:
        if list[x][x] == list[i + 1][x - 1]:
            if i == len(list) - 1:
                print(list[x][x] + " Wins")
                break
            x -= 1
            i += 1
        else:
            break

    print("No One Wins. Its a Draw")



find_winner()