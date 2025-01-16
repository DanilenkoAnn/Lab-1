# Задание №1
def draw_swiss_flag():
    flag_width = 10
    flag_height = 5
    
    RED = '\033[41m  \033[0m'   
    WHITE = '\033[47m  \033[0m'   

    for i in range(flag_height):
        if i == 0:   
            print(RED * flag_width)
        elif i == 1:  
            print(RED * 4 + WHITE * 2 + RED * 4)
        elif i == 2:  
            print(RED * 2 + WHITE * 6 + RED * 2)
        elif i == 3:
            print(RED * 4 + WHITE * 2 + RED * 4)
        elif i == 4:  
            print(RED * flag_width)

if __name__=='__main__':
    draw_swiss_flag() 

 
 
# Задание №2
def draw_line(lenght = 1,offset = 0, gap = 0, whitespacel = 0):
    line = " " * lenght
    print(
        f'{" " * offset}'
        f'\x1b[48;5;255m{line}\x1b[0m{" " * gap}'
        f'\x1b[48;5;255m{line}\x1b[0m{" " * whitespacel}'
        f'\x1b[48;5;255m{line}\x1b[0m{" " * gap}'
        f'\x1b[48;5;255m{line}\x1b[0m'
    )

def circle():
    height = 8
    step = 2
    lenght = 2
    offset = 15
    whitespacel = 12
    gap = height * 2 - step * lenght
    center = height / 2
    for line in range(height + 1):
        if line == 0:
            draw_line(height, offset,  0, whitespacel)
        elif line < center:
            offset -= step
            whitespacel -= step * 2
            gap += step * lenght 
            draw_line(lenght, offset, gap, whitespacel)
        elif line == center or line == center + 1:
            #gap += step
            draw_line(lenght, offset, gap, whitespacel)
        elif line == height:
            offset += step
            whitespacel += step * 2 
            draw_line(height, offset, 0, whitespacel)
        else:
            gap -= step * lenght
            offset += step
            whitespacel += step * 2
            draw_line(lenght, offset, gap, whitespacel)


if __name__=='__main__':
    circle() 


#Задание №3
for x in range(28, 0, -3):
    print (f'{" " * x * 3}\x1b[48;5;255m{" " * 3 * 3}\x1b[0m')


#Задание №4
with open("sequence.txt") as sequence:
    dates = [float(line) for line in sequence] 
res = []
for data in dates:
    if data >= -3 and data <= 3:
        res.append(data)
a = len(dates) - len(res)
b = len(res)
print(" ","30,4%", "(76 чисел))"," "*20,"69,6%", "(174 числа)")
print(f'\x1b[48;5;202m{" "*(b // 2)}\x1b[0m\x1b[48;5;10m{" " * (a//2)}\x1b[0m')
print("Всего: 250 чисел")