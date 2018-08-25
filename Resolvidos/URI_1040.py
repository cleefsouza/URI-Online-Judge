class media31040:
	linha = input().split(' ')
	
	n1, n2, n3, n4 = float(linha[0]), float(linha[1]), float(linha[2]), float(linha[3])
	
	media = ((n1*2)+(n2*3)+(n3*4)+(n4*1))/10
	
	print('Media: {:.1f}'.format(media))
	
	if(media>=7):
		print('Aluno aprovado.')
	elif(media<5):
		print('Aluno reprovado.')
	elif(media>=5 and media<7):
		print('Aluno em exame.')
		exame = float(input())
		print('Nota do exame: {:.1f}'.format(exame))
		
		media_exame = (exame+media)/2
		if(media_exame>=5):
			print('Aluno aprovado.')
		else:
			print('Aluno reprovado.')
		
		print('Media final: {:.1f}'.format(media_exame))
