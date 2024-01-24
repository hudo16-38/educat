from random import randint
import tkinter as tk
from math import ceil
from fractions import Fraction
import numpy as np

class App:
    def __init__(self) -> None:
        self.beg = 20
        self.canvas = tk.Canvas(height=300, width=600)
        self.canvas.pack()
        self.text_label = None
        self.show_button = tk.Button(text="Ukáž výsledok", command=self.show_fraction, background="gray")
        self.show_button.place(x=140, y=140)
        self.canvas.bind("<ButtonPress-1>", self.show_click)
        
        self.generate_random_fraction()
        tk.mainloop()
        
    
    def generate_random_fraction(self) -> None:
        while 1:
            fraction = Fraction(
            randint(1, 20),
            randint(2, 10)
            )

            if fraction.denominator != 1:
                break

        self.fraction = fraction
        num, den = fraction.numerator, fraction.denominator
        n = num//den
        if num % den != 0:
            n += 1
        self.n = n
        self.num_ticks = n*den
        self.step = 400/n

        if self.text_label is None:
            self.text_label = tk.Label(text=f"Zobraz zlomok {self.fraction}.", font=("Helvetica", 14))
            self.text_label.place(x=20, y=100)
        else:
            self.text_label.config(text=f"Zobraz zlomok {self.fraction}.", font=("Helvetica", 14))

        self.generate_button = tk.Button(text="Vygeneruj zlomok", command=self.generate_random_fraction, background="lightblue")
        self.generate_button.place(x=20, y=140)

        self.create_axis()

    def create_axis(self) -> None:
        self.canvas.delete("all")
        self.canvas.create_line(self.beg, 50, 400+self.beg, 50)

        for index in range(self.n+1):
            x = index*self.step + self.beg
            self.canvas.create_line(x, 30, x, 70)
            self.canvas.create_text(x, 80, text=str(index))

            ticks = np.linspace(x, x+self.step, self.fraction.denominator, endpoint=False)

            if index == self.n:
                break

            for tick in ticks:
                self.canvas.create_line(tick, 40, tick, 60)

    def show_fraction(self) -> None:
        decimal = float(self.fraction)
        pos = self.step*decimal + self.beg
        self.canvas.create_oval(pos-5, 45, pos+5, 55, fill="red")

    def show_click(self, event: tk.Event) -> None:
        self.canvas.delete("my_click")
        x, y = event.x, event.y

        self.canvas.create_oval(x-5, 50-5, x+5, 50+5, tags="my_click", fill="green")

        

if __name__ == "__main__":
    app = App()