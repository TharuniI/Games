//---------------------------Constant------------------------------//
/*Constants for main page*/
var blueRect;
var purpRect;
var RADIUS = 28;
var title = new Text("Brick Breaker Remake", "27pt Kristen ITC");
var play = new Text("Play", "40pt Arial Rounded MT Bold");
/* Constants for bricks */
var NUM_ROWS = 8;
var BRICK_TOP_OFFSET = 10;
var BRICK_SPACING = 2;
var NUM_BRICKS_PER_ROW = 10;
var BRICK_HEIGHT = 10;
var SPACE_FOR_BRICKS = getWidth() - (NUM_BRICKS_PER_ROW + 1) * BRICK_SPACING;
var BRICK_WIDTH = SPACE_FOR_BRICKS / NUM_BRICKS_PER_ROW;
var rect;
var top = BRICK_TOP_OFFSET;
var left = BRICK_SPACING;
var totalBricks = NUM_ROWS * NUM_BRICKS_PER_ROW;

/* Constants for ball */
var BALL_RADIUS = 15;
var ball;
var dx = -2;
var dy = 4;

/* Constants for paddle */
var pad;
var PADDLE_WIDTH = 80;
var PADDLE_HEIGHT = 15;
var PADDLE_OFFSET = 10;
var posY = getHeight() - PADDLE_HEIGHT*2;
//-------------------------------Main Page-----------------------------------//
//Start Function for Main Page//
function start(){
    mainpage();
}
//Main Page//
function mainpage(){
    var backRect = new Rectangle(getWidth(), getHeight());
    backRect.setPosition(0, 0);
    var backColor = new Color(240, 248, 255);
    backRect.setColor(backColor);
    add(backRect);
    
    title.setPosition(getWidth()/2 - title.getWidth()/2, getHeight()/2 - 50);
    setTimer(changeColor, 250);
    
    blueRect = new Rectangle(200,80);
    blueRect.setPosition(getWidth()/2 - blueRect.getWidth()/2, getHeight()/2);
    blueRect.setColor(Color.blue);
    add(blueRect);
    
    purpRect = new Rectangle(182,62);
    purpRect.setColor(Color.purple);
    purpRect.setPosition(getWidth()/2 - purpRect.getWidth()/2, getHeight()/2 + purpRect.getHeight()/8);
    add(purpRect);
    
    play.setPosition(getWidth()/2 - play.getWidth()/2, getHeight()/2 + play.getHeight());
    play.setColor(Color.white);
    add(play);
    
    mouseClickMethod(startGame);

}
//Color Change Function for Play Button//
function changeColor(){
    var randCol = Randomizer.nextColor();
    title.setColor(randCol);
    add(title);
}
//--------------------------------Game Page-----------------------------------//
//Start function for game page//
function startGame(){
    //Remove everthing from main screen
    remove(blueRect);
    remove(purpRect);
    stopTimer(changeColor);
    remove(title);
    remove(play);
    
    //Wall
	drawWall();

	//Ball
	drawBall();
	setTimer(moveBall, 5);

	//Paddle
	drawPaddle();
	mouseMoveMethod(movePad);
}

//Wall Functions//
function drawWall(){
    drawRow(Color.RED);
    drawRow(Color.RED);
    drawRow(Color.ORANGE);
    drawRow(Color.ORANGE);
    drawRow(Color.GREEN);
    drawRow(Color.GREEN);
    drawRow(Color.BLUE);
    drawRow(Color.BLUE);
}
//Function for each row of bricks 
function drawRow(color){
    for (var i = 0; i < NUM_BRICKS_PER_ROW; ++i){
        rect = new Rectangle(BRICK_WIDTH, BRICK_HEIGHT);
        rect.setColor(color);
        rect.setPosition(left, top);
        add(rect);

        left += (BRICK_SPACING + BRICK_WIDTH);
    }

    left = BRICK_SPACING;
    top += (BRICK_TOP_OFFSET + BRICK_SPACING);
}

//Ball Functions//
function drawBall(){
    ball = new Circle(BALL_RADIUS);
	ball.setPosition(getWidth()/2, getHeight()/2);
	add(ball);
}
//Check if the ball has reached a wall.
//Then move the ball in the correct direction.
function moveBall(){
	checkWalls();
	ball.move(dx, dy);
}

function checkWalls(){
    //Bounce of top of wall
    if (ball.getY() + ball.getRadius() < 0){
        dy = -dy;
    }
	// Bounce off right wall
	if(ball.getX() + ball.getRadius() > getWidth()){
		dx = -dx;
	}

	// Bounce off left wall
	if(ball.getX() - ball.getRadius() < 0){
		dx = -dx;
	}

	//Bounce if touches paddle
	if ((ball.getY() + ball.getRadius()) > (pad.getY())   &&   ((ball.getX() >= pad.getX()) && (ball.getX() <= pad.getX()+pad.getWidth()))){
	    dy = -dy;
	}

	// Break if it touches bottom of screen
	if(ball.getY() + ball.getRadius() > getHeight()){
	    ball.setPosition(getWidth()/2, getHeight()/2);
		stopTimer(moveBall);
		mouseClickMethod(restartBall);
	}

	//Remove Bricks
	var elem = getElementAt(ball.getX(), ball.getY() - ball.getRadius());
	if ((elem != null) && (elem.getColor() != Color.Black)){
	    remove(elem);
	    dy = -dy;
	    totalBricks -= 1;
	    
	    if (totalBricks < 0){
	        var winner = new Text("You Win!", "27pt Kristen ITC");
	        winner.setPosition(getWidth()/2 - title.getWidth()/2, getHeight()/2 - 50);
	        winner.setColor(Color.blue);
	        add(title);
	    }
	}
}
//Function for when the ball goes off screen and needs to restart
function restartBall(e){
    setTimer(moveBall, 20);
}

//---------------------Paddle Functions----------------------------//
function drawPaddle(){
    pad = new Rectangle(PADDLE_WIDTH, PADDLE_HEIGHT);
    pad.setPosition(getWidth()/2 - PADDLE_WIDTH/2, posY);
    add(pad);
}

function movePad(e){
    pad.setPosition(e.getX(), posY);
    add(pad);
}
