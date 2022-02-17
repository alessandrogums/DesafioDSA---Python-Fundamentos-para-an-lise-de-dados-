
#Solução análoga ao desafio num 36 do repositório de soluções do codewars 

import math

class Primes:
    
    lista_primos=[2]
    num=3
    
    @classmethod 
    def first(cls,numero):
        while len(cls.lista_primos) < numero:
            valida_primo=True
            raiz_num=int(math.sqrt(cls.num))+1
            for k in range(2,raiz_num):
                if cls.num % k == 0 :
                    valida_primo=False 
                    break
            if valida_primo:
                cls.lista_primos.append(cls.num)
            cls.num+=2
        return cls.lista_primos[:numero]
