class imposto1051:
	
	salario = float(input())
	
	if(salario>=0 and salario<=2000.00):
		print('Isento')
	elif(salario>=2000.01 and salario<=3000.00):
		resto = salario - 2000
		resul = resto*0.08
		print('R$ {:.2f}'.format(resul))
	elif(salario>=3000.01 and salario<=4500.00):
		resto = salario - 3000
		resul = (resto*0.18)+(1000*0.08)
		print('R$ {:.2f}'.format(resul))
	elif(salario>4500.00):
		resto = salario - 4500
		resul = (resto*0.28)+(1500*0.18)+(1000*0.08)
		print('R$ {:.2f}'.format(resul))
