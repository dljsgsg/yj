#1
import random


def power(base, exp):
    if (exp == 1):
        return (base)
    if (exp != 1):
        return (base * power(base, exp - 1))


base = int(input("Введите число: "))
exp = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", power(base, exp))
#2
def num(a,b):
    if a > b:
        a,b = b,a
        total = 0
        for i in range(a,b +1):
            total += i
        return total
    else:
        total = 0
        for i in range(a, b + 1):
            total += i
        return total

# a = int(input("tell first number"))
# b = int(input("tell second number"))
# print(f"ot {a} before {b} =  {num(a,b)}")
#3
def star(n):
    if n > 0:
        print("*", end = ' ')
        star(n-1)
    else:
        print(' ')
a =  int(input("tell your number"))
star(a)
#4
board = list(range(1, 10))

def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)

#4
def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + "? ")
        try:
            player_answer = int(player_answer)
        except ValueError:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if 1 <= player_answer <= 9:
            if str(board[player_answer - 1]) not in "XO":
                board[player_answer - 1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")


def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#             take_input("X")
#         else:
#             take_input("O")
#         counter += 1
#
#         tmp = check_win(board)
#         if tmp:
#             print(tmp, "выиграл!")
#             win = True
#             break
#         if counter == 9:
#             print("Ничья!")
#             break
#    draw_board(board)


 main(board)

#5
def minka(nums,start = 0, min=float('inf'), minn = 0):
    if start+ + 10 >len(nums):
        return minn
    current_sum = sum(nums[start:start+10])
    if current_sum < min:
        min = current_sum
        minn=start
        return minka(nums, start+ 1, min, minn)
import random
random_numbers = [random.randint(1,100) for _ in range(100)]
start_p = minka(random_numbers)
#6
import datetime
def days_diff(start_date, end_date):
    date_format = "%Y-%m-%d"
    start_datetime = datetime.datetime.strptime(start_date, date_format)
    end_datetime = datetime.datetime.strptime(end_date, date_format)
    diff = end_datetime - start_datetime
    return diff.days

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
start_date = "2022-01-01"
end_date = "2022-12-31"
difference_in_days = days_diff(start_date, end_date)
print("Разница в днях между датами:", difference_in_days)

year = 2024
if is_leap_year(year):
    print(f"{year} является високосным годом")
else:
    print(f"{year} не является високосным годом")
