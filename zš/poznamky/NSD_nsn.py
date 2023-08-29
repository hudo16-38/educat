from pandas import DataFrame
from random import randint


def generuj_cisla(pocet=10):
    z1, z2, z3 = [], [], []

    for _ in range(pocet):
        z1.append(randint(1, 100))
        z2.append(randint(1, 100))
        z3.append(randint(1, 100))

    
    df = DataFrame({"a":z1,
                    "b":z2,
                    "c":z3,
                    "NSD(a,b,c)":[""]*pocet,
                    "nsn(a,b,c)":[""]*pocet})
    return df

if __name__ == "__main__":
    n = 25
    df = generuj_cisla(n)
    print(df.to_latex(index=False))
