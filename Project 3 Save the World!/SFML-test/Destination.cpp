#include <SFML/Graphics.hpp>
#include <SFML/Audio.hpp>
#include <string>
#include <iostream>
#include "Destination.h"

// default constructor
destination::destination()
{
	sf::SoundBuffer SoundBuffer;
	if (!SoundBuffer.loadFromFile("resources/foom.wav")) {
		std::cout << "cannot open audio";
		sf::sleep(sf::seconds(5));
	}
	sf::Sound Sound(SoundBuffer);

	itemCount = 0;
}

// overloaded constructor
destination::destination(int x, int y, int xLimit, int yLimit, std::string spriteFile, EntityType type)
{
	if (!texture.loadFromFile(spriteFile)) {
		cout << "Error loading " << spriteFile << endl;
	}
	sprite = sf::Sprite(texture);

	if (!SoundBuffer.loadFromFile("resources/foom.wav")) {
		std::cout << "cannot open audio";
		sf::sleep(sf::seconds(5));
	}
	Sound = sf::Sound(SoundBuffer);

	this->x = x;
	this->y = y;
	this->xLimit = xLimit;
	this->yLimit = yLimit;
	this->spriteFile = spriteFile;
	this->type = type;
	itemCount = 0;
}

// plays entity sound and updates message board
string destination::say()
{
	Sound.play();
	message = "Message: You place the item in the bin.";
	return message;
}