#ifndef DESTINATION_H
#define DESTINATION_H

#include <SFML/Graphics.hpp>
#include <SFML/Audio.hpp>
#include <string>
#include <iostream>
#include "Entity.h"	

// Prize Entity for Prize Objects
class destination : public Entity
{
public:
	destination(); // Default Constructor
	destination(int x, int y, int xLimit, int yLimit, std::string spriteFile, EntityType type); // Overloaded constructor
	string say(); //overrided say function
private:
	int itemCount; // prizeLevel variable
};


#endif