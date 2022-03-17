/****************************************************************
File:			Entity.cpp
Description:	Member function definitions for class Entity
Author:
Class:			CSCI 120
Date:
I hereby certify that this program is entirely my own work.
*****************************************************************/

#include <SFML/Graphics.hpp>
#include <SFML/Audio.hpp>
#include <string>
#include <iostream>
#include "Entity.h"

using namespace std;

// Entity constructor
Entity::Entity() {
	x = 0;
	y = 0;
	xLimit = 0;
	yLimit = 0;
	type = DEFAULT;
	recyclableItem = 0;
	trashItem = 0;
}

//overloaded entity constructor
Entity::Entity(int x, int y, int xLimit, int yLimit, std::string spriteFile, EntityType type) {
	if (!texture.loadFromFile(spriteFile)) {
		cout << "Error loading " << spriteFile << endl;
	}

	sprite = sf::Sprite(texture);

	this->x = x;
	this->y = y;
	this->xLimit = xLimit;
	this->yLimit = yLimit;
	this->spriteFile = spriteFile;
	this->type = type;
	recyclableItem = 0;
	trashItem = 0;
}
	
int Entity::getX() {
	return x;
}
	
int Entity::getY() {
	return y;
}

void Entity::moveUp() {
	if (y > 0)
		y--;
}

void Entity::moveDown() {
	if (y < yLimit)
		y++;
}

void Entity::moveLeft() {
	if (x > 0)
		x--;
}

void Entity::moveRight() {
	if (x < xLimit)
		x++;
}

sf::Sprite Entity::getSprite() {
	return sprite;
}

EntityType Entity::getType() {
	return type;
}

int Entity::getScoreUpdate(int timeDelay)
{
	return 0;
}

// entity say function
string Entity::say()
{
	return message;
}

// check if entity has item
bool Entity::hasRecyclableItem()
{
	if (recyclableItem = 1)
		return true;

	else
		return false;
}

bool Entity::hasTrashItem()
{
	if (trashItem = 1)
		return true;

	else
		return false;
}

void Entity::setRecyclableItem(int num)
{
	recyclableItem = num;
}

void Entity::setTrashItem(int num)
{
	trashItem = num;
}

void Entity::setType(EntityType type)
{
	this->type = type;
}