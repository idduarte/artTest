

from datetime import datetime
import random


class random_integer_1to5:
    random.seed(datetime.now())
    values = [1, 2, 3, 4, 5]

    def get_next_integer(self):
        return random.choice(self.values)
    
    def get_size(self):
        return len(self.values)

class random_integer_1to7:
    generator = random_integer_1to5()
    def get_next_integer(self):
        return int(7 * (self.generator.get_next_integer()/self.generator.get_size()))

if __name__ == "__main__":
    r = random_integer_1to7()
    for i in range(100):
        print(r.get_next_integer())