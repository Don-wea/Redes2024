import json
import string
import random


# --- ~~ ~~ __Private methods ~~ ~~ --- 

# Function to generate a random string
def _CrearStringAleatorio(length):
    letters = string.ascii_letters  # Contains both uppercase and lowercase letters
    return ''.join(random.choice(letters) for _ in range(length))


# Function to create a "persona" dictionary
def _crearPersonaAleatoria():
    persona = {
        'nombre': _CrearStringAleatorio(random.randint(3, 15)),
        'edad': str(random.randint(18, 25)),
        'carrera': _CrearStringAleatorio(random.randint(10, 26)),
        'semestre': str(random.randint(1, 14))
    }
    return persona

# Function to create a list of personas
def _crearListaZero(filename,elements):
    lista = []

    for _ in range(elements):
        lista.append(_crearPersonaAleatoria())  # Call the function with parentheses

    # Writing the list to a JSON file
    with open(filename, 'w') as json_file:
        json.dump(lista, json_file, indent=4)  # indent=4 makes the JSON more readable

    return filename

# funcion para encontrar entradas aleatorias
def _definirEntradasAleatorias(percentageToModify,amountToModify):

    cantidadAModificar= int((percentageToModify * amountToModify) / 100)
    if cantidadAModificar > amountToModify:
        print("error, elements to modify are way more than the ones available!")
        return

    randomSelection = []

    for j in range(cantidadAModificar):

        num=random.randint(1,amountToModify)

        if randomSelection.count(j)>0:
            j-=1
        else:
            randomSelection.append(num)

    return randomSelection

def _copiarLista(filenameModified,filenameToSend):


    with open(filenameModified, 'r') as json_file:
        data = json.load(json_file)
           

    with open(filenameToSend, 'w') as json_file:
        json.dump(data,json_file,indent=4)


def _modificarListaZero(filenameOriginal,filenameModified,percentageToModify,numElements):

    errorCharacters = ['!','@','#','$','%','&']

    # seleccionar numeros aleatorios para modificar
    listaNumerosSeleccionados = _definirEntradasAleatorias(percentageToModify,numElements)

    with open(filenameOriginal, 'r') as json_file:
        data = json.load(json_file)

    for  i in range(numElements):
        
        if i in listaNumerosSeleccionados:
            # modify element
            errorCharacterToAdd = errorCharacters[random.randint(0,5)]
            valueToModify = random.randint(1,4)
            if valueToModify ==1 :
                data[i]['nombre']+=errorCharacterToAdd
            elif valueToModify == 2:
                data[i]['edad']+=errorCharacterToAdd
            elif valueToModify ==3:
                data[i]['carrera']+=errorCharacterToAdd
            else :
                data[i]['semestre']+=errorCharacterToAdd

            

    with open(filenameModified, 'w') as json_file:
        json.dump(data,json_file,indent=4)

def _corregirDatosNoValidos(diccionario):
    errorCharacters = ['!', '@', '#', '$', '%', '&']
    
    for entry in diccionario:
        fields_to_check = ['nombre', 'edad', 'carrera', 'semestre']
        
        for field in fields_to_check:
            if field in entry and len(entry[field]) > 0:
                # Remove all instances of the error characters
                entry[field] = ''.join([char for char in entry[field] if char not in errorCharacters])



def _compareAndFix(miLista, suLista):

    to_remove = []

    # Compare, print, and mark for removal
    for i in miLista:
        if i not in suLista:
            print(i)
            to_remove.append(i)  
        else:
            _corregirDatosNoValidos([i])  

    # Now remove the marked items
    for item in to_remove:
        miLista.remove(item)
        #miLista.pop(item)




# --- ~~ ~~ PUBLIC EVENTS ~~ ~~ --- 

def eventCreation():
    print(" -   -   - ~event Creation~")

    numElements =100
    filenameOriginal ='PersonasOriginal.json'
    filenameModified ='PersonasModifiedZero.json'
    filenameToSend ='PersonasModified.json'
    percentageToModify = 15


    # crear la lista de 100 personas
    pathToJsonFile = _crearListaZero(filenameOriginal,numElements)
    print(" 1. lista creada")
    

    # modificar el 15% de la lista con caracteres no permitidos
    pathToJsonFile = _modificarListaZero(filenameOriginal,filenameModified,percentageToModify,numElements)
    print(" 2. lista modificada con caracteres no validos")

    _copiarLista(filenameModified,filenameToSend)

    return '0'


def eventConnectionOpen():

    return '0'

def eventStep(message='0'):

    if not message:
        print("no message received")
        return "100"
    if isinstance(message,str) and message =="100":
        print("exhange  finished")
        return "100"

    filenameToSend ='PersonasModified.json'
    filenameReceived = 'receivedData.json'

    

    with open(filenameReceived,"w") as json_file:
        json_file.write(message)
    
    with open(filenameReceived,"r") as json_file:
        receivedMessage=json.load(json_file)

    with open(filenameToSend,"r") as json_file:
        miLista=json.load(json_file)
    #miLista = open(filenameToSend,'r')
    # response =''
    
    # first fiel to be sent 
    if message == '0': 
        print("     - json file to be sent...")
        #send the data to the server for the first time
        
        return filenameToSend
    else:   
    
        #compare the data and correct invalid characters
        #suLista = open(receivedMessage,'r')
        suLista=receivedMessage
        _compareAndFix(miLista,suLista)

        # save corrected json file
        with open(filenameToSend, 'w') as json_file:
            json.dump(miLista,json_file,indent=4)

        return filenameToSend


def eventConnectionClose():
    return '0'



# --- ~~ ~~ TEST MAIN ~~ ~~ --- 
if __name__ == "__main__":
    eventConnectionOpen("testing")