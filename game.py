# import random
# user_num = int(input('Pick a number between 0 and 10: '))
# random_num = (random.randint(0,10))
#
# while user_num != random_num:
#     if user_num < random_num:
#         print('Sorry, you lost! You guessed too low.')
#         user_num = int(input('Guess again:'))
#     elif user_num > random_num:
#         print('Sorry you lost! You guessed too high.')
#         user_num = int(input('Guess again:'))
#
# if user_num == random_num:
#     print(f'Congratulations you won! You guessed {random_num} correctly.')
#
import random
user_num = 'none'
random_num = (random.randint(1,10))

while user_num != random_num and user_num != 'no more magic':
    user_num = input('Pick a number between 1 and 10: ')
    end = user_num.lower()
    if end == 'no more magic':
        print('GAME OVER!')
        break

    user_num = int(user_num)
    if user_num < random_num:
        print('Sorry, you lost! You guessed too low. Please try again!')

    elif user_num > random_num:
        print('Sorry you lost! You guessed too high. Please try again!')

if user_num == random_num:
    print(f'Congratulations you won! You guessed {random_num} correctly.')
