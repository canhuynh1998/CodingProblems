"""
Lenny is playing a game on a 3 × 3 grid of lights. In the beginning of the game all lights are switched on. Pressing any of the lights will toggle it and all side-adjacent lights. The goal of the game is to switch all the lights off. We consider the toggling as follows: if the light was switched on then it will be switched off, if it was switched off then it will be switched on.

Lenny has spent some time playing with the grid and by now he has pressed each light a certain number of times. Given the number of times each light is pressed, you have to print the current state of each light.

Input
The input consists of three rows. Each row contains three integers each between 0 to 100 inclusive. The j-th number in the i-th row is the number of times the j-th light of the i-th row of the grid is pressed.

Output
Print three lines, each containing three characters. The j-th character of the i-th line is "1" if and only if the corresponding light is switched on, otherwise it's "0".
"""

def main():
    pressed_times = []
    for _ in range(3):
        row = list(map(int, input().split(" ")))
        pressed_times.append(row)
    
    row11 = "1" if (pressed_times[0][0] +pressed_times[0][1] + pressed_times[1][0]) % 2 == 0 else "0"
    row12 = "1" if (pressed_times[0][0] + pressed_times[0][1] + pressed_times[0][2] + pressed_times[1][1]) % 2 == 0 else "0"
    row13 = "1" if (pressed_times[0][1] + pressed_times[0][2] + pressed_times[1][2] ) % 2 == 0 else "0"
    first_row = "{}{}{}".format(row11, row12, row13)

    row21 = "1" if (pressed_times[1][0] + pressed_times[1][1] + pressed_times[0][0] + pressed_times[2][0]) % 2 == 0 else "0"
    row22 = "1" if (pressed_times[1][0] + pressed_times[1][1] + pressed_times[0][1] + pressed_times[1][2]+pressed_times[2][1]) % 2 == 0 else "0"
    row23 = "1" if (pressed_times[1][2] + pressed_times[1][1] + pressed_times[0][2] + pressed_times[2][2] ) % 2 == 0 else "0"
    second_row = "{}{}{}".format(row21, row22, row23)

    row31 = "1" if (pressed_times[2][0] + pressed_times[2][1] + pressed_times[1][0]) % 2 == 0 else "0"
    row32 = "1" if (pressed_times[2][1] + pressed_times[2][0] + pressed_times[1][1] + pressed_times[2][2] ) % 2 == 0 else "0"
    row33 = "1" if (pressed_times[2][2] + pressed_times[2][1] + pressed_times[1][2]) % 2 == 0 else "0"
    third_row = "{}{}{}".format(row31, row32, row33)

    print("{}\n{}\n{}".format(first_row, second_row, third_row))
if __name__ == "__main__":
    main()