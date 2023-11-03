class Monitor:
    def __init__(self, marca, tamanho):
        self.marca = marca
        self.tamanho = tamanho

class Computador:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.monitor = None 

    def conectar_monitor(self, monitor):
       
        self.monitor = monitor

    def desconectar_monitor(self):
      
        self.monitor = None

monitor1 = Monitor("Dell", 24)
computador1 = Computador("HP", "Pavilion")


computador1.conectar_monitor(monitor1)


if computador1.monitor:
    print(f"Computador {computador1.marca} possui um monitor {computador1.monitor.marca} de {computador1.monitor.tamanho} polegadas.")
else:
    print(f"Computador {computador1.marca} não possui um monitor.")


computador1.desconectar_monitor()


if computador1.monitor:
    print(f"Computador {computador1.marca} possui um monitor {computador1.monitor.marca} de {computador1.monitor.tamanho} polegadas.")
else:
    print(f"Computador {computador1.marca} não possui um monitor.")

