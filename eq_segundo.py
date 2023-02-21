#a² +b²+ c = 0
#Delta b²-4ac
#Bascara (-b +/- raiz delta)/2a

import math
import time

a=int(input('Qual o valor de a: '))
b=int(input('Qual o valor de b: '))
c=int(input('Qual o valor de c: '))


tempb = math.pow (b,2)

delta = (tempb-(4*a*c))
print ('O valor de delta é: ', delta)
print ()                               #pula linha

if delta > 0 :
	 
	raizdelta = math.sqrt(delta)
	print (raizdelta)
	print ()                               #pula linha

	basc1 = (-b + raizdelta)/(2*a)

	basc2 = (-b - raizdelta)/(2*a)

	print ('Raiz 1 é: ',basc1)
	print ('Raiz 2 é: ',basc2)
	print ()                               #pula linha

else :
	print ('Delta negativo impossível continuar')

time.sleep(10) #espera pra fechar 30 segundos
