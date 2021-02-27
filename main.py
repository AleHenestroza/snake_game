# Juego Snake clásico, utilizando la biblioteca Turtle de Python
# Creado por Alejandro Henestroza
# Todos los componentes de este programa pueden ser copiados, reutilizados y redistribuidos

from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

# Setup de la ventana
screen = Screen()
screen.setup(width=600, height=600, startx=600, starty=200)
screen.bgcolor("black")
screen.title("A Snake Game - by AleHenestroza")
screen.tracer(0)  # No se van a renderizar los cambios en la pantalla hasta que se actualice manualmente

# Setup de los objetos
snake = Snake()
food = Food()
score = Score()

# Listeners
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Loop principal
running = True
while running:
    screen.update()  # Actualización de la pantalla
    time.sleep(0.1)  # Delay de la actualización de la pantalla
    # Con este delay, se puede controlar la velocidad de actualización de la ventana, efectivamente controlando
    # la velocidad del juego.
    snake.move()
    score.write_score()

    # Detección de la colisión con la comida
    if snake.head.distance(food) < 15:
        food.refresh()
        score.add_score()

screen.exitonclick()
