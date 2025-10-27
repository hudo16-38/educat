import tkinter as tk
from random import choice

WIDTH, HEIGHT = 1000, 800

canvas = tk.Canvas(width=WIDTH, height=HEIGHT, bg="white")
entry = tk.Entry()
button = tk.Button(text="Kresli rozklad", command=lambda: kresli_rozklad(n=int(entry.get()), sirka=200, x=WIDTH // 2, y=20))
entry.pack()
button.pack()
canvas.pack()


def je_prvocislo(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def delitele(n: int) -> list[int]:
    delitele_list = []
    for i in range(2, n):
        if n % i == 0:
            delitele_list.append(i)
    return delitele_list


def kresli_rozklad(n: int, sirka: int, x: int, y: int):
    canvas.delete("all")
    s = [(n, sirka, x, y)]

    while s:
        cislo, sirka, x, y = s.pop()
        if je_prvocislo(cislo):
            canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="lightblue")
            canvas.create_text(x, y, text=str(cislo))
        else:
            d = delitele(cislo)
            # print("Delitele cisla", cislo, ":", d)
            n1 = choice(d)
            n2 = cislo // n1
            s.append((n1, sirka/2, x - sirka / 2, y + 40))
            s.append((n2, sirka/2, x + sirka / 2, y + 40))
            canvas.create_line(x, y, x - sirka / 2, y + 40)
            canvas.create_line(x, y, x + sirka / 2, y + 40)
            canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="lightblue")
            canvas.create_text(x, y, text=str(cislo))

tk.mainloop()