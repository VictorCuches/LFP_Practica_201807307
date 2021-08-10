import tkinter as tk
from tkinter import filedialog 
import webbrowser


def salir(): #opcion de salir, muestos mis datos y sale al dal enter
    print("\n\nLenguajes Formales y de Programacion B-")
    print("Nombre: Victor Alejandro Cuches de León")
    print("Carnet: 201807307")
    print("Correo: vcuches55@gmail.com")
    input("adios...")

def order(oFile, indiO, report): #funcion para ordenamiento de los numeros
    count = 0 #contador para hacer una cadena con los numeros ordenados
    count2 = 0 #contador para hacer una cadena y guardarlo en una lista (html)
    limit = indiO -1 #defino el limite para que el for ordene los numeros
    listaTemp = list(oFile) #esta lista es para no alterar la principal y el BUSCAR salga bien

    for g in range(1, indiO): #para mostrar contenido de la lista (html)
        if (count2==0):
            srLista = str(oFile[g])
            count2=1
        else: 
            srLista = srLista +", " +str(oFile[g])

    for i in range(1, limit): #usando metodo de burbuja
        for j in range(1, limit): #empieza en 1 para no tomar el nombre de la lista
            if (int(listaTemp[j])>int(listaTemp[j+1])):
                buble = listaTemp[j]
                listaTemp[j] = listaTemp[j+1]
                listaTemp[j+1] = buble

    for k in range(1, indiO): #guardo los numeros ordenados para imprimir el resultado
            if (count==0):
                cadena = str(listaTemp[k])
                count=1
            else: 
                cadena = cadena +", " +str(listaTemp[k])
    #print(str(listaTemp[0]),": ORDENADOS = ", cadena)

    if (report!=4): #si selecciono opcion 2 o 3
        print(str(listaTemp[0]),":",str(srLista)," | ORDENADOS =", cadena)

    if (report==4): #guardo este contenido para luego usarlo en el html
        text = str(listaTemp[0])+": "+str(srLista)
        textt = "ORDENADOS = "+ cadena
        allFile.append(text)
        allFuncs.append(textt) 

def find(fFile, indiB, report):
    cadena=""
    count = 0 #contador guardar contenido 
    count2 = 0 #contador html
    
    if(str(fFile[indiB-1]).upper()=="ORDENAR"): #verifico si el BUSCAR va antes de un ORDENAR, para definir el limite del for de busqueda
        limit = len(fFile) -3 
    else:
        limit = len(fFile) -2

    for g in range(1, limit): #guardo el contenido de la lista para usarlo en la lista que usare en el html
        if (count2==0):
            srLista2 = str(fFile[g])
            count2=1
        else: 
            srLista2 = srLista2 +", " +str(fFile[g])

    for i in range(1, limit): #metodo para buscar el numero que quiero
        if str(fFile[i])==str(fFile[indiB+1]):
            if (count==0):
                cadena = str(i) #guardo la posicion
                count=1
            else: 
                cadena = cadena +", " +str(i) 

    if (cadena!="" and report!=4): #para opcion 2 y 3
        print(fFile[0],":",str(srLista2)," | VALOR A BUSCAR: ",str(fFile[indiB+1])," | POSICION =", cadena)

    if (cadena=="" and report!=4): #para opcion 2 y 3
        print(fFile[0],":",str(srLista2)," | VALOR A BUSCAR: ",str(fFile[indiB+1])," | POSICION = NO ENCONTRADA")
    
    #guardo en la lista que usare para el html
    if (report==4 and cadena!=""):
        text1 = fFile[0]+": "+str(srLista2)
        text2 = "VALOR A BUSCAR: "+str(fFile[indiB+1])+" | POSICION = "+cadena
        allFile.append(text1)
        allFuncs.append(text2)
    if (report==4 and cadena==""):
        text3 = fFile[0]+": "+str(srLista2)
        text4 = "VALOR A BUSCAR: "+str(fFile[indiB+1])+" | POSICION = NO ENCONTRADA"
        allFile.append(text3)
        allFuncs.append(text4)

#lo use como un centro donde verifica que funcion quiere y lo envia ahi, evito hacer la verificacion y envio en cada opcion seleccionada
def funcs(liFile,liFile_B, fun): #ubico la funcion que se pide y mando la informacion para realizar cada instruccion 
                 #este liFile_B es lo mismo que liFile lo use para prevenir, no cambia nada
    for i in range(len(liFile)):
        for j in range(len(liFile[i])):     
                 
            if (fun==1 or fun==3 or fun==4):
                if(liFile[i][j].upper()=="ORDENAR"):
                    indO = j #guardo la posicion de ORDENAR para tener el limite para las demas funciones
                    order(liFile[i], indO, fun) 
            if (fun==2 or fun==3 or fun==4):
                if(liFile_B[i][j].upper()=="BUSCAR"):
                    indB = j #guardo la posicion de BUSCAR para tener el limite para las demas funciones
                    find(liFile_B[i], indB, fun)
    
def openR(contenido, funciones): #escribir y abrir automaticamente el html con todos los datos a desplegar
    html = open('practica1.html','w')
    
    inicio ="""
    <html>
    <head>
    
    <title>Practica #1</title>
    </head>
    <style type="text/css">
    table {
        width: 90%;
        background-color: white;
        text-align: left;
        border-collapse: collapse;
    }
    th, td{
        padding: 15px;
    }
    body{
        background-color: #58D68D;
        font-family: Arial;
    }
    thead{
        background-color: #246355;
        color: white;
        border-bottom: solid 5px #0F362D;
    }
    tr:nth-child(even){
        background-color: #ddd ;
    }
    tr:hover td{
        background-color: #369681;
        color: white;
    }
    div{
        background-color: #1D8348;
        font-family: Arial;
        width: 100%;
    }
    *{
        margin: 0px;
        padding: 0px;
    }
    </style>
    
    <body>
    <center>
    <div>
    <br>
    <br>
    <h1>Lenguajes Formales y de Programación</h1>
    <h3>Victor Alejandro Cuches de León   201807307</h3>
    <h3>Grupo B</h3>
    <br>
    <br>
    </div>
    <br>
   
    
    <table >
       <thead>
        <tr>
            <th>No.</th>
            <th>Lista</th>
            <th>Resultado</th>
        </tr>

       </thead> 
       
    """
    final="""
    <br>
    </table>
    </center>
    </body>
    </html>
    """
    html.write(inicio)
    for i in range(len(contenido)):
        no = i+1
        html.write("<tr>")
        html.write("<td>"+str(no)+"</td>")
        html.write("<td>"+str(contenido[i])+"</td>")
        html.write("<td>"+str(funciones[i])+"</td>")
        html.write("</tr>")
    html.write(final)
    html.close()
    webbrowser.open_new_tab('practica1.html')#Abrir automaticamente el html con los datos
    

opc = 0
lines_B = []
allFile=[] #lista para llenar con las salidas y luego poner en el html
allFuncs=[]
while(opc!=1): #Tiene que cargar primero un archivo, se repetira hasta que lo haga
    print("========== BIENVENIDO ==========") #Menu principal 
    print("Menu principal")
    print("1. Cargar archivo de entrada")
    print("2. Desplegar listas ordenadas")
    print("3. Desplegar busquedas")
    print("4. Desplegar todas")
    print("5. Desplegar todas a archivo")
    print("6. Salir")
    opc = int(input("Seleccione una opcion: "))
    print("")
    if(opc!=1): #Aviso de que tiene que cargar archivo
        print("¡La opcion seleccionada es incorrecta")
        print("debe cargar un archivo para empezar!\n")

    if(opc == 6): #despedida 
        salir()        
        break #Para que no continue en el while

    if(opc==1):
        print("--- CARGANDO ARCHIVO ---")
        nameFile = filedialog.askopenfilename(title = "Seleccione archivo", filetypes = (("archivos de texto", "*.txt"),))
        txt_file = open(nameFile, "r")
        with txt_file as fil: #para leer linea por linea del archivo
            lines = fil.readlines()
    
        for i in range(len(lines)): #para hacer las funciones mas faciles quito los signos y saltos innecesarios...
            lines[i] = lines[i].replace("\n", "") #me quedo solo con nombre de la lista, contenido e instrucciones que pide
            lines[i] = lines[i].replace(",", " ")
            lines[i] = lines[i].replace("=", " ")
            lines[i] = lines[i].split() #hago el split para obtener una lista con cada linea del archivo txt

        print("¡Se ha cargado el archivo con exito!")
        lines_B = list(lines)

        #despligue de opciones para realizar con el menu
        opc2 = 1
        while(opc2!=6): #para que siga apareciendo el menu cada vez que termine de realizar una opcion
            print("\n====== MENU 2 ====== ")
            print("1. Cargar archivo de entrada")
            print("2. Desplegar listas ordenadas")
            print("3. Desplegar busquedas")
            print("4. Desplegar todas")
            print("5. Desplegar todas a archivo")
            print("6. Salir")
            opc2 = int(input("Escoja una opcion: ")) #Segundo menu para realizar funciones con el archivo cargado
            print("")
            if(opc2<0 or opc>6):
                print("¡Seleccione una opcion correcta!\n")

            if(opc2==2): 
                noFu = 1 #guardo este numero de funcion para poder identificarla mas facilmente en la funcion funcs()
                print("========= L I S T A S  O R D E N A D A S =========")
                funcs(lines,lines_B, noFu)
            elif(opc2==1):
                print("Ya se ha cargado un archivo")  

            elif(opc2==3):
                noFu = 2 #guardo este numero de funcion para poder identificarla mas facilmente en la funcion funcs()
                
       
                print("========= B  U  S  Q  U  E  D  A  S =========")
                funcs(lines,lines_B, noFu) #lines y noFu son los importantes, lines_B lo puse para prevenir no tiene utilidad
            elif(opc2==4):
                noFu = 3 #guardo este numero de funcion para poder identificarla mas facilmente en la funcion funcs()
                print("========= O R D E N A R  &  B U S C A R =========")
                funcs(lines,lines_B, noFu)
            elif(opc2==5):
                noFu = 4 #guardo este numero de funcion para poder identificarla mas facilmente en la funcion funcs()
                print("----- ABRIENDO ARCHIVO HTML -----")
                funcs(lines,lines_B, noFu) #para obtener los datos en la lista allFile 
                openR(allFile, allFuncs) #escribir y abrir el html

            elif(opc2==6):
                salir()
            
                break 
                


            

        










