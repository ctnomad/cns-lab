from random import randint
from math import gcd

def primitiveRoots(modulo):
    roots = []
    #Find co-primes between 1 and the number n i.e., gcd between n and co-prime is 1
    coprime_set = set(num for num in range (1, modulo) if gcd(num, modulo) == 1)

    # for a number g, g^i%n should be same as coprime set of n
    for g in range(1, modulo):
        actual_set = set(pow(g, powers, modulo) for powers in range (1, modulo))
        if coprime_set == actual_set:
            roots.append(g)           
    return min(roots)

if __name__ == '__main__':

	# Both the persons will be agreed upon the
	# public keys G and P
	# A prime number P is taken
	P = int(input("Enter a prime number "))
	
	# A primitive root for P, G is taken
	G = primitiveRoots(P)
	
	print('The Value of P is : ', P)
	print('The Value of G is : ', G)
	
	# Alice will choose the private key a
	a = randint(0, 10)
	print('The Private Key a for Alice is : ', a)
	
	# gets the generated key
	x = int(pow(G,a,P))
	
	# Bob will choose the private key b
	b = randint(0, 10)
	print('The Private Key b for Bob is : ', b)
	
	# gets the generated key
	y = int(pow(G,b,P))
	
	# Secret key for Alice
	ka = int(pow(y,a,P))
	
	# Secret key for Bob
	kb = int(pow(x,b,P))
	
	print('Secret key for the Alice is : ', ka)
	print('Secret Key for the Bob is : ', kb)
