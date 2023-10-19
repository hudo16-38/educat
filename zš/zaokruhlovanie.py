from tkinter import Canvas, Button, Entry, mainloop, Label, END
from tkinter.messagebox import showwarning, showinfo
from random import uniform, choice

desatinne_miesta = {
    "tisícky":-3,
    "stovky":-2,
    "desiatky":-1,
    "jednotky":0,
    "desatiny":1,
    "stotiny":2,
    "tisíciny":3

}

class App:

    def __init__(self, a:float, b:float):
        self.canvas = Canvas(width=700)

        self.button1 = Button(text="Generuj číslo!", command=self.generate_number)
        self.button1.grid(column=0, row=0)

        self.entry = Entry()
        self.entry.grid(column=0, row=1)

        self.button2 = Button(text="Vyhodnoť!", command=self.eval)
        self.button2.grid(column=1, row=0, pady=10)

        self.text_label = Label()
        self.text_label.grid(column=0, row=2, padx=10, pady=10, columnspan=2)

        self.num_label = Label()
        self.num_label.grid(column=1, row=1, padx=10, pady=10)

        self.a, self.b = a, b
        self.num, self.pos = self.generate_number()

        mainloop()
        


    def generate_number(self) -> float:
        
        num = uniform(self.a, self.b)
        pos = choice(list(desatinne_miesta))

        self.num_label.configure(text=str(num))

        text = f"Zakrúhli dané číslo na {pos}."
        self.text_label.configure(text=text)

        return num, pos
    
    def eval(self) -> None:

        if self.entry.get() == "":
            showwarning(message="Nezadal/a si číslo!")
        elif float(self.entry.get()) == round(self.num, desatinne_miesta[self.pos]):
            showinfo(message="Správne!")
            self.entry.delete(0, END)
            self.num, self.pos = self.generate_number()
        else:
            showinfo(message=f"Nesprávne! Správna odpoveď je {round(self.num, desatinne_miesta[self.pos])}.")
            self.entry.delete(0, END)
            self.num, self.pos = self.generate_number()



if __name__ == "__main__":
    app = App(0, 3250)



    




