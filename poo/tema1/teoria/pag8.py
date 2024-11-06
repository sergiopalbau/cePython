class OperaCadena():

    @staticmethod
    def primera_letra(cadena):
        return (cadena[0])
    
    @staticmethod
    def cadena_mayuscula (cadena):
        return cadena.upper()
    

print (OperaCadena.cadena_mayuscula("hola mundo"))
