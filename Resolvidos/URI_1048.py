class aumentosalario1048:
	
	sal = float(input())
	
	por = 0
	aum = 0
	n_sal = 0
	
	if(sal>=0 and sal<=400.00):
		por = '15 %'
		aum =  sal*0.15
		n_sal = sal+aum
	elif(sal>=400.01 and sal<=800.00):
		por = '12 %'
		aum =  sal*0.12
		n_sal = sal+aum
	elif(sal>=800.01 and sal<=1200.00):
		por = '10 %'
		aum =  sal*0.10
		n_sal = sal+aum
	elif(sal>=1200.01 and sal<=2000.00):
		por = '7 %'
		aum =  sal*0.07
		n_sal = sal+aum
	elif(sal>2000.00):
		por = '4 %'
		aum =  sal*0.04
		n_sal = sal+aum
		
	print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {}'.format(n_sal, aum, por))
