import random
import pymorphy2 as pm


morph = pm.MorphAnalyzer()

print("Я загадал 4значное число, все цифры которого различны. Попробуй его угадать:")


num_list = list(range(10)) 
num_list1 = [str(i) for i in num_list]
to_guess = random.sample(num_list1, 4)
num_2_guess = ''.join(to_guess)


def bk(number_2_guess, guess_try):
    b = 0 # количество быков
    k = 0 # количество коров
    common = set(list(num_2_guess)) & set(list(guess_try)) # находим пересечение множества цифр загадонного числа и введенного
    if len(common) == 0:
        pass
    else:
        for el in list(common):
            if number_2_guess.index(el) == guess_try.index(el):
                b += 1
            else:
                k += 1
    bull = morph.parse('бык')[0]
    cow = morph.parse('корова')[0]
    if b < 4:
        return str(b) + ' ' + bull.make_agree_with_number(b).word + ' ' + str(k) + ' ' + cow.make_agree_with_number(k).word
    else:
        return "Ура! Ты угадал моё число!"


tries_count = 0
try_lemma = morph.parse('попытка')[0]


while True:
    guess_try = input()
    tries_count += 1
    print(bk(num_2_guess, guess_try))
    if bk(num_2_guess, guess_try) == "Ура! Ты угадал моё число!":
        print("Тебе понадобилось", tries_count, try_lemma.make_agree_with_number(tries_count).word)
        break


        

