from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# Initial snake and food
snake = [(5, 5), (4, 5), (3, 5)]  # Snake body coordinates (list of tuples)
direction = "right"  # Initial direction of movement
food = (7, 7)  # Initial food position

# Game state
game_over = False

# Constants
WIDTH = 20
HEIGHT = 20


# API Route: Start new game
@app.route('/start_game', methods=['GET'])
def start_game():
    global snake, direction, food, game_over
    snake = [(5, 5), (4, 5), (3, 5)]
    direction = "right"
    food = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
    game_over = False
    return jsonify({'snake': snake, 'food': food, 'game_over': game_over})


# API Route: Move snake
@app.route('/move_snake', methods=['POST'])
def move_snake():
    global snake, direction, food, game_over

    # Get the direction from the request
    data = request.json
    direction = data['direction']

    # Get the head position
    head_x, head_y = snake[0]

    # Update the head position based on the direction
    if direction == "up":
        head_y -= 1
    elif direction == "down":
        head_y += 1
    elif direction == "left":
        head_x -= 1
    elif direction == "right":
        head_x += 1

    # Check for wall collision
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        game_over = True
        return jsonify({'game_over': game_over})

    # Check for self-collision (if the snake runs into itself)
    if (head_x, head_y) in snake:
        game_over = True
        return jsonify({'game_over': game_over})

    # Add new head to the snake
    snake = [(head_x, head_y)] + snake

    # Check if the snake ate the food
    if (head_x, head_y) == food:
        # Generate new food at a random location
        food = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
    else:
        # Remove the last part of the snake (tail)
        snake.pop()

    return jsonify({'snake': snake, 'food': food, 'game_over': game_over})


# Route for the main game page
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
