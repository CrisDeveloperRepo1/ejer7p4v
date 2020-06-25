import csv
dic={}
# lis=['hhhh','hhhhhhhjj','qqqqqq']

# for i in lis:
	# if i in dic:
		# print('repetida')
	# else:
		# dic[i]={'cont':0}
# print(dic)

T1=True

archivo= open('mujeresEncarrera.csv',encoding='utf-8')
csvreader=csv.reader(archivo)
for fila in csvreader:
	cont=0
	if T1:
		T1=False
	else:
		if fila[2] in dic:
			#print('re')
			cont = cont + (0 if fila[10]=='' else int(fila[10]))
			num=dic[fila[2]]['cant']
			num=num+cont
			dic[fila[2]]={'cant':num}
			
			
	
		else:
			cont = cont + (0 if fila[10]=='' else int(fila[10]))
			dic[fila[2]]={'cant':cont}
	
# for fila in csvreader:
	# if (fila[2] in dic) and T1 :
		# print('re')
	# else:
		# dic[fila[2]]={'cant':fila[11]}


#print(dic)
#print(dic.items())
print(dic)
print('*'*100)

dic2=sorted(dic.items(),key =lambda d:d[1]['cant'])

dic2=dict(dic2[::-1])
print(dic2)
#dd=list(dd.keys())
#print(dic2)
#print(dic.keys())
#lista=list(dic.keys())
#dic2=','.join(dic)
valores = {5:20000, 3:10000, 4:15000} 
valores_ord = dict(sorted(valores.items()))


#print(dic2[::-1])
