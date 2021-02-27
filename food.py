from turtle import Turtle
import random

HALF_SCREEN_SIZE = 400


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
        # 20 * 20 = 400
        # Tamaño de la pantalla: 800 x 800
        # Las coordenadas van de -400 a 400 en ambos ejes
        # Para no generar comida justo en el borde de la pantalla, 20 - 1 = 98
        # Esto va a generar comida en cualquier múltiplo de 20 entre -380 y 380 para ambos ejes
        random_x = random.randint(-int(HALF_SCREEN_SIZE / 20 - 1), int(HALF_SCREEN_SIZE / 20 - 1)) * 20
        random_y = random.randint(-int(HALF_SCREEN_SIZE / 20 - 1), int(HALF_SCREEN_SIZE / 20 - 1)) * 20
        self.goto(random_x, random_y)
