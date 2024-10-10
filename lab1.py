print(f'\x1b[48;5;9m{" "*29}\x1b[0m')
print(f'\x1b[48;5;9m{" "*11}\x1b[0m\x1b[48;5;255m{" "*7}\x1b[0m\x1b[48;5;9m{" "*11}\x1b[0m')
print(f'\x1b[48;5;9m{" "*4}\x1b[0m\x1b[48;5;255m{" "*21}\x1b[0m\x1b[48;5;9m{" "*4}\x1b[0m')
print(f'\x1b[48;5;9m{" "*4}\x1b[0m\x1b[48;5;255m{" "*21}\x1b[0m\x1b[48;5;9m{" "*4}\x1b[0m')
print(f'\x1b[48;5;9m{" "*11}\x1b[0m\x1b[48;5;255m{" "*7}\x1b[0m\x1b[48;5;9m{" "*11}\x1b[0m')
print(f'\x1b[48;5;9m{" "*29}\x1b[0m')
 
 
def draw_line(lenght=1,offset=0, prob=0, probel=0):
    line = " " * lenght
    print(f'{" " * offset}\x1b[48;5;255m{line}\x1b[0m{" " * prob}\x1b[48;5;255m{line}\x1b[0m{" " * probel}\x1b[48;5;255m{line}\x1b[0m{" " * prob}\x1b[48;5;255m{line}\x1b[0m')


def circle():
    height = 8
    step=2
    lenght=2
    offset=15
    probel = 12
    prob=height*2-step*lenght
    center = height/2
    for line in range(height+1):
        if line == 0:
            draw_line(height, offset,  0, probel)
        elif line < center:
            offset -= step
            probel -= step*2
            prob += step*lenght
            draw_line(lenght, offset, prob, probel)
        elif line == center or line == center+1:
            #prob += step
            draw_line(lenght, offset, prob, probel)
        elif line == height:
            offset += step
            probel += step*2
            draw_line(height, offset, 0, probel)
        else:
            prob -= step*lenght
            offset += step
            probel += step*2
            draw_line(lenght, offset, prob, probel)


if __name__=='__main__':
    circle() 


s = [float(x) for x in open('sequence.txt')]
res = []
for c in s:
    if c >= -3 and c <= 3:
        res.append(c)
a=len(s)-len(res)
b=len(res)
print(" ","30,4%", "(76 чисел))"," "*20,"69,6%", "(174 числа)")
print(f'\x1b[48;5;202m{" "*(b//2)}\x1b[0m\x1b[48;5;10m{" "*(a//2)}\x1b[0m')
print("Всего: 250 чисел")