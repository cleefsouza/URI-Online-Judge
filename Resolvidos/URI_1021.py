class notasmoedas1021:
	
	n100 = 0
	n50 = 0
	n20 = 0
	n10 = 0
	n5 = 0
	n2 = 0
	n1 = 0
	n050 = 0
	n025 = 0
	n010 = 0
	n005 = 0
	n001 = 0
    
	n = float(input())
    
	if(n>=0 and n<1000000):
		while(True):
			if(n>=100):
				n100=n100+1
				n=n-100
			elif(n>=50):
				n50=n50+1
				n=n-50
			elif(n>=20):
				n20=n20+1
				n=n-20
			elif(n>=10):
				n10=n10+1
				n=n-10
			elif(n>=5):
				n5=n5+1
				n=n-5
			elif(n>=2):
				n2=n2+1
				n=n-2
			elif(n>=1):
				n1=n1+1
				n=n-1
			elif(n>=0.5):
				n050=n050+1
				n=n-0.5
			elif(n>=0.25):
				n025=n025+1
				n=n-0.25
			elif(n>=0.10):
				n010=n010+1
				n=n-0.10
			elif(n>=0.05):
				n005=n005+1
				n=n-0.05
			elif(n>=0.01 or n>=0.00999999999999):
				n001 += 1
				n -= 0.01 or 0.00999999999999
			else:
				break
	        
		print('NOTAS:')
		print(n100,'nota(s) de R$ 100.00')
		print(n50,'nota(s) de R$ 50.00')
		print(n20,'nota(s) de R$ 20.00')
		print(n10,'nota(s) de R$ 10.00')
		print(n5,'nota(s) de R$ 5.00')
		print(n2,'nota(s) de R$ 2.00')
		print('MOEDAS:')
		print(n1,'moeda(s) de R$ 1.00')
		print(n050,'moeda(s) de R$ 0.50')
		print(n025,'moeda(s) de R$ 0.25')
		print(n010,'moeda(s) de R$ 0.10')
		print(n005,'moeda(s) de R$ 0.05')
		print(n001,'moeda(s) de R$ 0.01')
