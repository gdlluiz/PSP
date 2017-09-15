#Programa: Contador de lineas de codigo
#Autor: Jose Luis Vazquez Corona
#PSP01
'''
'Cuenta clases, funciones, lines de codigo
'''
#Part
class ContadorLineas:
#Item
    def leerArchivo(self):
        file = open('Contador.py', 'r')
        return file
#Item
    def cuentaCodigo(self):
        datos = self.leerArchivo()
        parts = 0
        items = 0
        loc = 0
        for line in datos.readlines():
            line = line.strip()
            if line[:1] != "#" and line != "" and line != "'" and line != '\n':
                loc = loc + 1
            if line[:5] == '#Part':
                parts = parts + 1
                loc = loc -1
            if line[:5] == '#Item':
                items = items + 1
                loc = loc - 1
        print('Lineas de Codigo: ', loc)
        print('Clases: ', parts)
        print('Funciones: ', items)
objeto = ContadorLineas()
objeto.cuentaCodigo()