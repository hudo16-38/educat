from random import randint
from math import gcd
from dataclasses import dataclass

@dataclass
class Zlomok:
    citatel:int
    menovatel:int

    def __repr__(self):
        return f"{self.citatel}/{self.menovatel}"
    __str__ = __repr__

@dataclass
class Dvojica:
    z1:Zlomok
    z2:Zlomok

    def ries(self) -> str:
        
        c1, m1 = self.z1.citatel, self.z1.menovatel
        c2, m2 = self.z2.citatel, self.z2.menovatel
        deli = gcd(c1*m2 + c2*m1, m1*m2)

        return f"""({self.z1}) + ({self.z2}) = (({c1}*{m2}) + ({c2}*{m1}))/{m1}*{m2} = (({c1*m2}) + ({c2*m1}))/{m1*m2} = {c1*m2 + c2*m1}/{m1*m2} = {(c1*m2 + c2*m1)//deli}/{m1*m2//deli}"""
        
    def zadanie(self) -> str:
        return f"({self.z1}) + ({self.z2}) = "
    

def generuj_zlomky(n:int, rozsah:int=20) -> list[Dvojica]:
    vysl = []
    for _ in range(n):
        z1 = Zlomok(randint(-rozsah, rozsah), randint(2, rozsah))
        z2 = Zlomok(randint(-rozsah, rozsah), randint(2, rozsah))
        vysl.append(Dvojica(z1, z2))
        
    return vysl

def zapis_riesenia(zlomky:list[Dvojica], subor:str) -> None:
    with open(subor, "w") as s:
        for d in zlomky:
            print(d.ries(), file=s)
            
def zapis_zadania(zlomky:list[Dvojica], subor:str) -> None:
    with open(subor, "w") as s:
        for d in zlomky:
            print(d.zadanie(), file=s)

if __name__ == "__main__":
    #z1 = Zlomok(1, 2)
    #z2 = Zlomok(1, 3)
    #d = Dvojica(z1, z2)
    #print(d.ries())
    N = 50    
    FILE1 = "zlomky_zadania.txt"
    FILE2 = "zlomky_riesenia.txt"
    zlomky = generuj_zlomky(N)
    zapis_zadania(zlomky, FILE1)
    zapis_riesenia(zlomky, FILE2)
