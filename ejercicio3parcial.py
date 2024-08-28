class Accesorios:
    def __init__(self,objeto,color,marca,material):
        self.objeto=objeto
        self.color=color
        self.marca=marca
        self.material=material
mibolso=Accesorios("bolso","gris","active","sintetico")
print(type(mibolso))
print(f"{mibolso.objeto}\n{mibolso.color}\n{mibolso.marca}\n{mibolso.material}")
