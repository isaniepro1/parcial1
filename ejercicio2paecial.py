class Felino:
    def __init__(self,nombre,color,especie,edad,sexo):
        self.nombre=nombre
        self.color=color
        self.especie=especie
        self.edad=edad
        self.sexo=sexo
lulu=Felino("lulu","Amarillo con manchas negras","Leopardo", "2 años","femenino")
simba=Felino("simba","naranjo amarillento","Leon","5 años","masculino")
print(type(lulu))
print(f"{lulu.nombre}\n{lulu.color}\n{lulu.especie}\n{lulu.edad}`\n{lulu.sexo}")

print(type(simba))
print(f"{simba.nombre}\n{simba.color}\n{simba.edad}\n{simba.sexo}")


        