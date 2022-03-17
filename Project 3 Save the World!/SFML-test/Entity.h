/****************************************************************
File:			Entity.h
Description:	Class and enumeration declaration related to game entities 
Author:
Class:			CSCI 120
Date:
I hereby certify that this program is entirely my own work.
*****************************************************************/

#ifndef ENTITY_H
#define ENTITY_H

#include <SFML/Graphics.hpp>
#include <SFML/Audio.hpp>
#include <string>
#include <iostream>

using namespace std;

// type of game entities
enum EntityType { UNKNOWN, PLAYER, RECYCLABLE, WALL, TRASH, RCAN, TCAN, DEFAULT };

// Class representing a game entity 
class Entity {
public:
	/*
	 * Initializes the object to default values
	 */
	Entity();

	/*
	 * Initializes the object based on parameter values
	 * @param x x-coordinate
	 * @param y y-coordinate
	 * @param xLimit maximum value of x-coordinate
	 * @param yLimit maximum value of y-coordinate
	 * @param spriteFile path to sprite file
	 * @param type entity type
	 */
	Entity(int x, int y, int xLimit, int yLimit, std::string spriteFile, EntityType type);

	/*
	 * Returns x-coordinate of entity
	 * @return x-coordinate
	 */
	int getX();

	/*
	* Returns y-coordinate of entity
	* @return y-coordinate
	*/
	int getY();

	/*
	* Moves entity up by one unit by updating y-coordinate as appropriate
	*/
	void moveUp();

	/*
	* Moves entity down by one unit by updating y-coordinate as appropriate
	*/
	void moveDown();

	/*
	* Moves entity left by one unit by updating x-coordinate as appropriate
	*/
	void moveLeft();

	/*
	* Moves entity right by one unit by updating x-coordinate as appropriate
	*/
	void moveRight();

	/*
	 * Returns sprite object belonging to the entity
	 * @return sprite
	 */
	sf::Sprite getSprite();

	/*
	 * Returns the entity type of the entity
	 * @return type
	 */
	EntityType getType();

	virtual int getScoreUpdate(int timeDelay); // to be overrided in derived classes
	virtual string say(); // to be overrided in derived classes
	bool hasRecyclableItem(); // check if entity has item
	bool hasTrashItem();
	void setRecyclableItem(int num);
	void setTrashItem(int num);
	void setType(EntityType type);

protected:
	int x;	// x-coordinate of location (lowest value is 0)
	int y;	// y-coordinate of location (lowest value is 0)
	int xLimit; // highest value of x-coordinate
	int yLimit; // highest value of y-coordinate
	std::string spriteFile; // path to sprite image
	sf::Sprite sprite;	// Sprite object
	sf::Texture texture; // texture for sprite
	sf::Sound Sound; // sound for entity
	sf::SoundBuffer SoundBuffer; // Sound buffer for entity
	EntityType type; // type of entity
	std::string name; // name of entity
	std::string message; // message for message board
	int recyclableItem;
	int trashItem ;

};

#endif
