print("Examen 1043")
class zapateria1043:
    id_proveedor=0
    nombre=""
    contacto=""
    telefono=""
    direccion=""
    ciudad=""
    def  mostrardatos(self):
        print(f"ID del proveedor: {self.id_proveedor}")
        print(f"Nombre : {self.nombre}")
        print(f"Contactos : {self.contacto}")
        print(f"Telefono : {self.telefono}")
        print(f"Direccion : {self.direccion}")
        print(f"Ciudad : {self.ciudad}")
    def listar_nombres(self):
        print("Nombres de proveedores")
        lista=["Calzado Express","Zapatos del mundo","Calzado Premium","Calzado Elegante","Calzado Estilo"]
        for x in lista:
            print(x)
    def tupla_Telefono(self):
        print("Telefono de proveedores")
        tupla=("614-123-3647","656-456-8643","656-873-4578","656-445-7564","639-756-4756")
        for x in tupla:
            print(x)
    def diccionario_direccion(self):
        print("direcciones de proveedores")
        diccionario={
            "Calle" : "Mora",
            "Calle" : "Sol",
            "Calle" : "Los lobos",
            "Calle" : "Ejercito nacional",
            "Calle" : "Durazno",
        }
        for x,y in diccionario.items():
            print(x,y)
    def mensaje(self):
        print("datos de provedores")
proveedor=zapateria1043()
proveedor.id_proveedor="4355"
proveedor.nombre="Calzado Express"
proveedor.telefono="614-123-3647"
proveedor.contacto="764"
proveedor.direccion="Calle Mora"
proveedor.ciudad="Chihuahua"
print("")
print(f"id proveedor: {proveedor.id_proveedor}")
print("")
print(f"nombre: {proveedor.nombre}")
print("")
print(f"contactos: {proveedor.contacto}")
print("")
print(f"telefonos: {proveedor.telefono}")
print("")
print(f"direccion: {proveedor.direccion}")
print("")
print(f"ciudad: {proveedor.ciudad}")
print("")
proveedor.mensaje()
print("Funciones")
print("")
print("Lista")
proveedor.listar_nombres()
print("Tupla")
proveedor.tupla_Telefono()
print("Diccionario")
proveedor.diccionario_direccion()
