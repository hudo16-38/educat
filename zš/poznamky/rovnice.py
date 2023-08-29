from dataclasses import dataclass
from random import randint

@dataclass
class Zlomok:
    citatel: int
    menovatel: int

    def __repr__(self):
        return "\\frac{"+str(self.citatel)+"}{"+str(self.menovatel)+"}"
    __str__ = __repr__

@dataclass
class Rovnica:
    lava_strana: tuple[Zlomok]
    prava_strana: tuple[Zlomok]

    def __repr__(self):
        z1, z2 = self.lava_strana
        z3, z4 = self.prava_strana

        return f"{z1}x + {z2} = {z3}x + {z4}"
    __str__ = __repr__


def generuj_rovnice(pocet=5):
    zoz = []

    for _ in range(pocet):
        c1 = randint(-20,20)
        c2 = randint(1, 50)
        c3 = randint(-20,20)
        c4 = randint(1, 50)
        c5 = randint(-20,20)
        c6 = randint(1, 50)
        c7 = randint(-20,20)
        c8 = randint(1, 50)

        z1 = Zlomok(c1, c2)
        z2 = Zlomok(c3, c4)
        z3 = Zlomok(c5, c6)
        z4 = Zlomok(c7, c8)
        
        rovnica = Rovnica( (z1, z2), (z3, z4) )
        zoz.append(rovnica)

    return zoz


def zapis_rovnice(rovnice, subor):
    with open(subor, "w") as s:
        s.write("\\documentclass[12pt]{article}\n")
        s.write("\\linespread{1.25}\n\n")
        s.write("\\begin{document}\n\n")
        
        for r in rovnice:
            s.write(f"${r}$")
            s.write("\\\\")
            s.write("\n")
        s.write("\n\\end{document}")


if __name__ == "__main__":
    subor = "rovnice.tex"
    rovnice = generuj_rovnice(20)
    zapis_rovnice(rovnice, subor)
    
