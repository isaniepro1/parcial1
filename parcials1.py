class Mascota:
    def __init__(self,nombre,edad,color,raza,):
        self.nombre=nombre
        self.edad=edad
        self.color=color
        self.raza=raza
bruno=Mascota("Bruno","8 años","negro","pincher")
peluche=Mascota("Peluche","1 años","blanco","freshpoodle")
print(type(bruno))
print(f"{bruno.nombre}\n{bruno.edad}\n{bruno.color}\n{bruno.raza}")

print(type(peluche))
print(f"{peluche.nombre}\n{peluche.edad}\n{peluche.color}\n{peluche.raza}")
