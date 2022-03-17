/****************************************************************
File:			main.cpp
Description:
Author:
Class:			CSCI 120
Date:
I hereby certify that this program is entirely my own work.
*****************************************************************/

#include <SFML/Graphics.hpp>
#include <SFML/Audio.hpp>
#include <time.h>
#include <vector>
#include "Entity.h"
#include "Item.h"
#include "Destination.h"

using namespace std;

const int NUM_HORIZONTAL = 15;	// number of adventure game sprites horizontally tiled
const int NUM_VERTICAL = 10;	// number of adventure game sprites vertically tiled
const int SIZE_SPRITE = 48;		// size of a sprite (square)
const int WIDTH = SIZE_SPRITE * NUM_HORIZONTAL;	// width of the game window
const int HEIGHT = SIZE_SPRITE * (NUM_VERTICAL + 2);	// height of the game window (including score and message board)
int timeDelay = 0, endTimer = 0, endTimer1 = 0, score = 0;
bool gameOver = false, updated = false, lastOne = false;

enum Direction {NONE, UP, DOWN, LEFT, RIGHT};

/*
 * Determines and returns the type of collision between a player and another entity 
 * in a given vector. The location is based on the current position of the player 
 * moving towards the given direction of movement. In the case of colliding with 
 * a prize entity, the entity is removed from the vector.
 * @param entityPtrVector vector containing pointers to entities in the game
 * @param x x-coordinate of the current player location 
 * @param y y-coordinate of the current player location
 * @param dir direction of the player movement
 */

EntityType checkCollision(Entity* entityPtrGrid[NUM_HORIZONTAL][NUM_VERTICAL], int x, int y, Direction dir, bool recyclable, bool trash) {
	if (dir == UP) {
		y--;
	}
	else if (dir == DOWN) {
		y++;
	}
	else if (dir == LEFT) {
		x--;
	}
	else if (dir == RIGHT) {
		x++;
	}
	if (x >= 0 && y >= 0 && x < NUM_HORIZONTAL && y < NUM_VERTICAL && entityPtrGrid[x][y] != NULL) 
	{	
		Entity* entity = entityPtrGrid[x][y];
		cout << "In check collision function" << endl; // FIXME
			if (entity->getType() == RECYCLABLE) 
			{		
				cout << "in recyclable check collision" << endl;
					delete entity;
					entityPtrGrid[x][y] = NULL;
					return RECYCLABLE;
			}

			else if (entity->getType() == TRASH)
			{
				cout << "in trash check collision" << endl;
					delete entity;
					entityPtrGrid[x][y] = NULL;
					return TRASH;
			}

			else
				return entityPtrGrid[x][y]->getType();
		}

	return UNKNOWN;
}

int main()
{
	Entity* entityPtrGrid[NUM_HORIZONTAL][NUM_VERTICAL]; // vector containing all game entities (player, prizes, walls)
	
	for (int i = 0; i < NUM_HORIZONTAL; ++i)
		for (int j = 0; j < NUM_VERTICAL; ++j)
			entityPtrGrid[i][j] = NULL;

	srand((unsigned int)time(0));

	sf::RenderWindow window(sf::VideoMode(WIDTH, HEIGHT), "CSCI 120 - Maze Adventure Project");

	// create player entity
	Entity player(0, 0, NUM_HORIZONTAL - 1, NUM_VERTICAL - 1, "resources/alice.png", PLAYER);
	entityPtrGrid[0][0] = &player;
	Entity player1 = player;

	// Location variables
	int x = rand() % NUM_HORIZONTAL;
	int y = rand() % NUM_VERTICAL;

	// create a recyclable entity, check for overlap ---->>>> with WHILE loop
	int recyclableEntities = 0;
	while (recyclableEntities < 5)
	{
		x = rand() % NUM_HORIZONTAL;
		y = rand() % NUM_VERTICAL;
		if (entityPtrGrid[x][y] == NULL)
		{
			entityPtrGrid[x][y] = new itemClass(x, y, NUM_HORIZONTAL - 1, NUM_VERTICAL - 1, "resources/recyclable.jpg", RECYCLABLE);
			recyclableEntities++;
		}
	}

	// Trash entities, check for overlap
	int TrashEntities = 0;
	while (TrashEntities < 5)
	{
		x = rand() % NUM_HORIZONTAL;
		y = rand() % NUM_VERTICAL;
		if (entityPtrGrid[x][y] == NULL)
		{
			entityPtrGrid[x][y] = new itemClass(x, y, NUM_HORIZONTAL - 1, NUM_VERTICAL - 1, "resources/banana.jpg", TRASH);
			TrashEntities++;
		}
	}

	// Recycling Can Entity
	int recyclingCanEntities = 0;
	while (recyclingCanEntities < 1)
	{
		x = rand() % NUM_HORIZONTAL;
		y = rand() % NUM_VERTICAL;
		if (entityPtrGrid[x][y] == NULL)
		{
			entityPtrGrid[x][y] = new destination(x, y, NUM_HORIZONTAL - 1, NUM_VERTICAL - 1, "resources/RecyclingBin.png", RCAN);
			recyclingCanEntities++;
		}
	}

	// Trash Can Entity
	int trashCanEntities = 0;
	while (trashCanEntities < 1)
	{
		x = rand() % NUM_HORIZONTAL;
		y = rand() % NUM_VERTICAL;
		if (entityPtrGrid[x][y] == NULL)
		{
			entityPtrGrid[x][y] = new destination(x, y, NUM_HORIZONTAL - 1, NUM_VERTICAL - 1, "resources/TrashBin.jpg", TCAN);
			trashCanEntities++;
		}
	}

	// create tree entities, check for overlap
	int treeEntities = 0;
	while (treeEntities < 20)
	{
		x = rand() % NUM_HORIZONTAL;
		y = rand() % NUM_VERTICAL;
		if (entityPtrGrid[x][y] == NULL && (entityPtrGrid[1][0] == NULL || entityPtrGrid[0][1] == NULL || entityPtrGrid[1][1] == NULL))
		{
			entityPtrGrid[x][y] = new Entity(x, y, NUM_HORIZONTAL - 1, NUM_VERTICAL - 1, "resources/Tree.jpg", WALL);
			treeEntities++;
		}
	}

	// load background sprite
	sf::Texture texture;
	if (!texture.loadFromFile("resources/background1.jpg"))
	{
		cout << "Error loading background";
		return EXIT_FAILURE;
	}
	sf::Sprite backgroundSprite;
	backgroundSprite.setTexture(texture);
	
	// load the text font
	sf::Font font;
	if (!font.loadFromFile("resources/Quicksand-Regular.otf")) {
		cout << "cannot open font";
		sf::sleep(sf::seconds(5));
		return EXIT_FAILURE;
	}

	// initialize the score board
	sf::Text scoreBoard;
	scoreBoard.setFont(font);
	scoreBoard.setCharacterSize(25);
	scoreBoard.setPosition(10.f, (NUM_VERTICAL + 1) * SIZE_SPRITE); // at the bottom of the window
	scoreBoard.setFillColor(sf::Color::Black);
	scoreBoard.setString("Score: 0");
	
	// initialize message board
	sf::Text messageBoard;
	messageBoard.setFont(font);
	messageBoard.setCharacterSize(25);
	messageBoard.setPosition(10.f, NUM_VERTICAL * SIZE_SPRITE); // at the bottom of the window
	messageBoard.setFillColor(sf::Color::Blue);
	messageBoard.setString("Message: none");

	// load the sound used in the game
	sf::SoundBuffer backgroundSoundBuffer;
	if (!backgroundSoundBuffer.loadFromFile("resources/awesomeness.wav")) {
		std::cout << "cannot open audio";
		sf::sleep(sf::seconds(5));
		return EXIT_FAILURE;
	}
	sf::Sound backgroundSound(backgroundSoundBuffer);
	backgroundSound.play(); // play background music	

	// timer for time delays
	sf::Clock clock;
	float timer = 0, delay = 0.2;

	Direction dir = NONE; // direction of player move

	// main game loop
	while (window.isOpen())
	{
		float time = clock.getElapsedTime().asSeconds();
		clock.restart();
		timer += time;


		sf::Event e;
		while (window.pollEvent(e))
		{
			if (e.type == sf::Event::Closed) // close button
				window.close();
		}

		if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left)) { // left key
			dir = LEFT;
		}
		else if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right)) { // right key
			dir = RIGHT;
		}
		else if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up)) { // up key
			dir = UP;
		}
		else if (sf::Keyboard::isKeyPressed(sf::Keyboard::Down)) { // down key
			dir = DOWN;
		}

		if (timer > delay) { // time delay to accomodate user key input 
			timer = 0; 

			// check for collision
			EntityType collisionType = checkCollision(entityPtrGrid, player.getX(), player.getY(), dir, player.hasRecyclableItem(), player.hasTrashItem());

			// If collision with Recyclable Item
			if (collisionType == RECYCLABLE && player.hasRecyclableItem() != true)
			{
				for (int i = 0; i < NUM_HORIZONTAL; ++i)
				{
					for (int j = 0; j < NUM_VERTICAL; ++j)
					{	
						itemClass *test = dynamic_cast<itemClass*> (entityPtrGrid[i][j]);
						
						// updated to prevent for loop from executing multiple times for one collision
						if (test != NULL && updated != true)
						{
							cout << "in recyclable item code" << endl;
							messageBoard.setString(test->say());
							score += test->getScoreUpdate(timeDelay);
							scoreBoard.setString("Score: " + to_string(score));
							updated = true;
							player.setRecyclableItem(1);
						}
					}
				}
				updated = false;
			}



			// If collision with trash item
			if (collisionType == TRASH)
			{
				for (int i = 0; i < NUM_HORIZONTAL; ++i)
				{
					for (int j = 0; j < NUM_VERTICAL; ++j)
					{
						itemClass *test1 = dynamic_cast<itemClass*> (entityPtrGrid[i][j]);

						// updated to prevent for loop from executing multiple times for one collision
						if (test1 != NULL && updated != true)
						{
							cout << " in trash item code" << endl;
							messageBoard.setString(test1->say());
							score += test1->getScoreUpdate(timeDelay);
							scoreBoard.setString("Score: " + to_string(score));
							updated = true;
							player.setTrashItem(1);
						}
					}
				}
				updated = false;
			}

			// If collision with trash can
			if (collisionType == TCAN)
			{
				for (int i = 0; i < NUM_HORIZONTAL; ++i)
				{
					for (int j = 0; j < NUM_VERTICAL; ++j)
					{
						destination *test2 = dynamic_cast<destination*> (entityPtrGrid[i][j]);

						if (test2 != NULL)
						{
							messageBoard.setString("Message: Congratulations! You Won!");

						}
					}
				}
			}

			// If collision with recycable can
			if (collisionType == RCAN)
			{
				for (int i = 0; i < NUM_HORIZONTAL; ++i)
				{
					for (int j = 0; j < NUM_VERTICAL; ++j)
					{
						destination *test3 = dynamic_cast<destination*> (entityPtrGrid[i][j]);

						if (test3 != NULL)
						{
							messageBoard.setString("Message: Congratulations! You Won!");
						}
					}
				}
			}


			// update player position based on direction
			if (collisionType != WALL) { 
				entityPtrGrid[player.getX()][player.getY()] = NULL;
				if (dir == UP) {
					player.moveUp();
				}
				else if (dir == DOWN) {
					player.moveDown();
				}
				else if (dir == LEFT) {
					player.moveLeft();
				}
				else if (dir == RIGHT) {
					player.moveRight();
				}
				entityPtrGrid[player.getX()][player.getY()] = &player;
				dir = NONE;
			}
		}

		// draw game interface
		window.clear();
		window.draw(backgroundSprite); // display background
		window.draw(scoreBoard); // display score board
		window.draw(messageBoard); // display message board

		// draw all adventure game sprites
		for (int i = 0; i < NUM_HORIZONTAL; ++i) 
			for (int j = 0; j < NUM_VERTICAL; ++j)
		{
			Entity* entity = entityPtrGrid[i][j];
			if (entity != NULL) 
			{
				sf::Sprite sprite = entity->getSprite();
				sprite.setPosition(i * SIZE_SPRITE, j * SIZE_SPRITE);
				window.draw(sprite);
			}
		
		}
		window.display();
	}

	return 0;
}
