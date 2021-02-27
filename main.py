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
screen.setup(width=800, height=800, startx=600, starty=200)
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
    time.sleep(0.085)  # Delay de la actualización de la pantalla
    # Con este delay, se puede controlar la velocidad de actualización de la ventana, efectivamente controlando
    # la velocidad del juego.
    snake.move()

    # Detección de la colisión con la comida
    # El número de la distancia no importa en tanto sea menor al tamaño de los objetos
    if snake.head.distance(food) < 15:
        food.refresh()
        score.add_score()
        snake.extend()

    # Detección de la colisión con la pared
    if snake.head.xcor() > 390 or snake.head.xcor() < -390 or snake.head.ycor() > 390 or snake.head.ycor() < -390:
        running = False
        score.game_over()

    # Detección de la colisión con la cola de la serpiente
    # El número de la distancia no importa en tanto sea menor al tamaño de los objetos
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            running = False
            score.game_over()


# Salida del programa
screen.exitonclick()
