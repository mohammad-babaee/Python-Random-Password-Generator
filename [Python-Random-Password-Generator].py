import random
from symtable import Symbol
from random_word import RandomWords
from random_word import Wordnik

x_word = random.randrange(369 , 9876543210)

r = RandomWords()

wordnik_service = Wordnik()

exit_node = r.get_random_word()

candy = wordnik_service.get_random_word()

Symbols1 = "_"

Symbols2 = "$"

print ("Python Secure Password Generator")
print ("---------")
print("Your Password Is : " + str(exit_node) + str(Symbols2) + str(x_word) + str(Symbols1) + str(candy) )
print ("---------")
print("Developer : Mohammad Babaee")