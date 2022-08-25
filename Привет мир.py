spisok = ['privet', 'ti', 'idi']
def count_letter(a):
    b = 0
    for word in spisok:

        if a in word:
            b += 1
    print(b)
count_letter('t')