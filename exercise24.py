def draw_horizontal():
    print('+---+---+---+')

def draw_vertical():
    print('|   |   |   |')

def draw_board():
    for i in range(3):
        draw_horizontal()
        for j in range(3):
            draw_vertical()
    draw_horizontal()

draw_board()