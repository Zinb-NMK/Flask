let canvas = document.getElementById('game-board');
let ctx = canvas.getContext('2d');  // Get the 2D context of the canvas
let snake = [{ x: 10, y: 10 }];  // Initial snake position (on grid 10, 10)
let direction = 'right';  // Snake's current direction
let food = {};  // Object to store food position
let gameInterval;
let isPlaying = true;

// Draw the snake on the board
function drawSnake() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);  // Clear the canvas each frame

    ctx.fillStyle = 'green';
    snake.forEach(segment => {
        ctx.fillRect(segment.x * 20, segment.y * 20, 20, 20);  // Draw snake segments as 20x20 boxes
    });
}

// Draw food on the board
function drawFood() {
    ctx.fillStyle = 'red';
    ctx.fillRect(food.x * 20, food.y * 20, 20, 20);  // Draw food as a red square
}

// Draw the grid
function drawGrid() {
    ctx.strokeStyle = '#ccc';  // Set grid color
    ctx.lineWidth = 0.5;  // Line width for grid
    for (let i = 0; i <= canvas.width / 20; i++) {
        // Vertical lines
        ctx.beginPath();
        ctx.moveTo(i * 20, 0);
        ctx.lineTo(i * 20, canvas.height);
        ctx.stroke();
    }
    for (let i = 0; i <= canvas.height / 20; i++) {
        // Horizontal lines
        ctx.beginPath();
        ctx.moveTo(0, i * 20);
        ctx.lineTo(canvas.width, i * 20);
        ctx.stroke();
    }
}

// Update game (move snake, check for collisions, etc.)
function updateGame() {
    let head = { ...snake[0] };

    // Move snake head in the current direction
    if (direction === 'up') head.y--;
    if (direction === 'down') head.y++;
    if (direction === 'left') head.x--;
    if (direction === 'right') head.x++;

    // Check if snake eats food
    if (head.x === food.x && head.y === food.y) {
        snake.unshift(food);  // Add food to snake (grows the snake)
        spawnFood();  // Generate new food
    } else {
        snake.unshift(head);  // Add the new head
        snake.pop();  // Remove the last segment (tail)
    }

    // Collision detection (snake hitting walls or itself)
    if (head.x < 0 || head.x >= 20 || head.y < 0 || head.y >= 20 || isCollision(head)) {
        stopGame();
        alert('Game Over!');
    }

    drawGrid();  // Draw grid on each update
    drawSnake();
    drawFood();
}

// Generate random food position
function spawnFood() {
    food = {
        x: Math.floor(Math.random() * 20),  // Random x (grid size: 20x20)
        y: Math.floor(Math.random() * 20),  // Random y
    };
}

// Check if snake collides with itself
function isCollision(head) {
    return snake.some((segment, index) => index !== 0 && segment.x === head.x && segment.y === head.y);
}

// Handle key events for controlling the snake
document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowUp' && direction !== 'down') direction = 'up';
    if (e.key === 'ArrowDown' && direction !== 'up') direction = 'down';
    if (e.key === 'ArrowLeft' && direction !== 'right') direction = 'left';
    if (e.key === 'ArrowRight' && direction !== 'left') direction = 'right';
});

// Start game
function startGame() {
    snake = [{ x: 10, y: 10 }];  // Reset snake to starting position
    direction = 'right';  // Reset direction
    spawnFood();  // Place food at random position
    gameInterval = setInterval(updateGame, 100);  // Update game every 100ms
}

// Stop game
function stopGame() {
    clearInterval(gameInterval);
}

// Button click listeners
document.getElementById('pause').addEventListener('click', stopGame);
document.getElementById('play').addEventListener('click', startGame);
document.getElementById('continue').addEventListener('click', startGame);

// Start the game automatically when the page loads
startGame();
