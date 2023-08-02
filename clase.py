class vehiculo:
    
    def __init__(self, color, placa, traccion) -> None:
        from datetime import datetime
        fecha_actual = datetime.now()
        self.dia = fecha_actual.weekday()
        self.llegada = fecha_actual.hour
        print(f"creando un vehiculo: {color}, {placa}, {traccion}, {self.llegada}")
        self.color = color
        self.placa = placa
        self.traccion = traccion
    def PicoPlaca(self):
        placa = int(self.placa[-1])
        if self.dia % 2 == 0:
            if placa % 2 == 0:
                return True
            else:
                return False
        else:
            if placa % 2 == 0:
                return False
            else:
                return True
    def pagar(self,precio):
        from datetime import datetime
        fecha_actual = datetime.now()
        actual = fecha_actual.hour
        actual += 1
        pagar = actual - self.llegada
        valor = precio * pagar
        print(f"el valor a pagar es: {valor}")
    def lugar(self, plazas):
        if plazas > 0:
            plazas -= 1
            print(f"vehiculo ingresado, {plazas} libres")
        else:
            print("no se encuentran lugares disponibles")
        
        return plazas
x = vehiculo("blanco", "cvb457", 4)
op = 1
plazas = 10
while op > 0 and op < 4:
    op = int(input("ingrese una opcion. \n 1-pico y placa \n 2-pagar \n 3-lugar \n"))
    if op == 1:
        if x.PicoPlaca():
            print("el vehiculo tiene pico y placa.")
        else:
            print("el vehiculo no tiene pico y placa")
    elif op == 2:
        x.pagar(2500)
    elif op == 3:
        plazas = x.lugar(plazas)
    elif op < 1 or op > 3:
        print("adios")