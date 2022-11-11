from datetime import datetime
import random


class random_integer_1to5:
    random.seed(datetime.now())
    values = [1, 2, 3, 4, 5]

    def get_next_integer(self):
        return random.choice(self.values)

class random_integer_1to7:
    ## Articulo base para el algoritmo
    ## https://es.wikipedia.org/wiki/Generador_de_n%C3%BAmeros_aleatorios

    ##  X_(n + 1) = ( a*X_n + c ) (mod m)
    """
    El standard POSIX C define para la función de generación de números 
    seudoaleatorios los valores de c = 12345, m = 32768  y a = 1103515245. 
    """
    a = 1103515245
    c = 12345
    m = 32768
    
    def __init__(self, seed) -> None:
        self.seed = seed

    def get_next_integer(self):
        xn1 = ((self.a * self.seed) + self.c) % self.m
        self.seed = xn1
        return (1 + int(7 * (xn1 / self.m)))

if __name__ == "__main__":
    r5 = random_integer_1to5()
    seed = r5.get_next_integer()
    r7 = random_integer_1to7(seed)
    with open('data.txt', 'w') as f:
        for i in range(32768):
            f.write(str(r7.get_next_integer())+"\n")
            # print(r7.get_next_integer())
        
