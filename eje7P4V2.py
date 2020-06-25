import PySimpleGUI as sg

import csv
dic={}
dic2={}
nombre=''
# lis=['hhhh','hhhhhhhjj','qqqqqq']

# for i in lis:
	# if i in dic:
		# print('repetida')
	# else:
		# dic[i]={'cont':0}
# print(dic)
#nombre=''

def añadirL(listBox,listaDatos):
	#listBox.update(map(lambda x: '{}:{}'.format(x[0],x[1]),listaDatos))
	listBox.update(listaDatos)


def ordenar(nombre):
	

	T1=True

	archivo= open(nombre,encoding='utf-8')
	csvreader=csv.reader(archivo)
	for fila in csvreader:
		cont=0
		if T1:
			T1=False
		else:
			if fila[2] in dic:
				cont = cont + (0 if fila[10]=='' else int(fila[10]))
				num=dic[fila[2]]['cant']
				num=num+cont
				dic[fila[2]]={'cant':num}
			
			
	
			else:
				cont = cont + (0 if fila[10]=='' else int(fila[10]))
				dic[fila[2]]={'cant':cont}
	
	dic2=sorted(dic.items(),key =lambda d:d[1]['cant'])
	dic2=dic2[::-1]
	dic2=dict(dic2) 
	return dic2
	#print(dic2)
	#return dic2
# for fila in csvreader:
	# if (fila[2] in dic) and T1 :
		# print('re')
	# else:
		# dic[fila[2]]={'cant':fila[11]}


#print(dic)
#print(dic.items())
#print('*'*100)
# dic2=sorted(dic.items(),key =lambda d:d[1]['cant'])
# dic2=dic2[::-1]
#print(dic2[::-1])



#print(dic.keys())
lista=list(dic.keys())

#lista=['xxx','yyy','aaaa']
layout = [
         [sg.Text('File 1', size=(8, 1)), sg.Input(), sg.FileBrowse(key='direccion'),sg.Button('ok')],
          [sg.Text('Click a Theme color to see demo window')],
          [sg.Listbox(lista,key='datos',background_color='green' ,size=(60, 20))],
          [sg.Button('Exit')],[sg.Button('Mostrar')],
           [ sg.ReadButton('Ordenar', key='boton_ordenar', disabled=True) ]]

window = sg.Window('Theme Browser', layout)

lei_archivo=False
while True:  # Event Loop
    Button, values = window.read()
    if Button in ('Exit'):
        break
    if Button == 'ok':
		     nombre=values['direccion']
		     window.FindElement('boton_ordenar').Update(disabled=False)
		     lei_archivo=True
		
#if event == 'boton_ordenar' and lei_archivo:		
		
    if Button == 'boton_ordenar' and lei_archivo:
		    #print('bien')
		    #print(values)
		    #nombre=values['direccion']
		    #print(nombre)
		    dic2=ordenar(nombre)
		    listaDatos=list(dic2.keys())
		    #print(dic2)
		    #listaDatos=dic2
		    añadirL(window.FindElement('datos'),listaDatos)
		   # print(values[1][0])
    #print(values)
    

    

window.close()





# import PySimpleGUI as sg

# sg.theme('Light Blue 2')

# layout = [[sg.Text('Enter 2 files to comare')],
          # [sg.Text('File 1', size=(8, 1)), sg.Input(), sg.FileBrowse()],
          # [sg.Text('File 2', size=(8, 1)), sg.Input(), sg.FileBrowse()],
          # [sg.Submit(), sg.Cancel()]]

# window = sg.Window('File Compare', layout)

# event, values = window.read()
# window.close()
# print(f'You clicked {event}')
# print(f'You chose filenames {values[0]} and {values[1]}')


#C:\Users\crist\Desktop\repasoP4Python/texto.txt

# archivos = open('C:/Users/crist/Desktop/repasoP4Python/texto.txt','r')
# print(archivos.read())
