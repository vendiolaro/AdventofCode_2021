#ifndef ITEM_H
#define ITEM_H

#include <SFML/Graphics.hpp>
#include <SFML/Audio.hpp>
#include <string>
#include <iostream>
#include "Entity.h"	

// Prize Entity for Prize Objects
class itemClass : public Entity
{
public:
	itemClass(); // Default Constructor
	itemClass(int x, int y, int xLimit, int yLimit, std::string spriteFile, EntityType type); // Overloaded constructor
	int getScoreUpdate(int timeDelay); //overrided getScoreUpdate function
	string say(); //overrided say function
private:
	int itemReward = 10; // prizeLevel variable
};


#endif