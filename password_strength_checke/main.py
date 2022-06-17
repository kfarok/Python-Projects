import string
import pandas as pd

password = input('Type your password: ')

with open('common.txt', 'r') as f:
    content = f.read().splitlines()


def check(password):
    score = 0

    punc = any([1 if char in string.punctuation else 0 for char in password])
    digits = any([1 if char in string.digits else 0 for char in password])
    upper_case = any([1 if char in string.ascii_uppercase else 0 for char in password])
    lower_case = any([1 if char in string.ascii_lowercase else 0 for char in password])

    add_up = [upper_case, lower_case, punc, digits]

    if password in content:
        print("!!!Your password is compermised!!!")

    # checking_length
    if len(password) > 8:
        score += 1
    if len(password) > 10:
        score += 1
    if len(password) > 12:
        score += 1
    if len(password) > 14:
        score += 1
    if len(password) > 16:
        score += 1
    if len(password) > 20:
        score += 1

    # checking_characters
    if sum(add_up) == 1:
        score += 1
    if sum(add_up) > 1:
        score += 1
    if sum(add_up) > 2:
        score += 1
    if sum(add_up) > 3:
        score += 1

    # Scoring
    if score < 4:
        print(f"Your password is weak!  with {len(password)} character and {sum(add_up)} Types.")
    if score ==  4:
        print(f"Your password is Fair!  with {len(password)} character and {sum(add_up)} Types.")
    if 4 < score < 6:
        print(f"Your password is Good!  with {len(password)} character and {sum(add_up)} Types.")
    if score > 6:
        print(f"Your password is Excellent!  with {len(password)} character and {sum(add_up)} Types.")

if __name__ == '__main__':
    check(password)
