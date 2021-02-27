from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__("circle")
        # self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        # 15 * 20 = 300
        # Tamaño de la pantalla: 600 x 600
        # Las coordenadas van de -300 a 300 en ambos ejes
        # Para no generar comida justo en el borde de la pantalla, 15 - 1 = 14
        # Esto va a generar comida en cualquier múltiplo de 20 entre -280 y 280 para ambos ejes
        random_x = random.randint(-14, 14) * 20
        random_y = random.randint(-14, 14) * 20
        self.goto(random_x, random_y)
