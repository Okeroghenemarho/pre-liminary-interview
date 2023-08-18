import random
import string

random_number ="".join(random.choices(["0","1"], k=4))
print(random_number)
random_number_in_base_10 = int(random_number,2)
print(random_number_in_base_10)
