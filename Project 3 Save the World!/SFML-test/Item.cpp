#include <SFML/Graphics.hpp>
#include <SFML/Audio.hpp>
#include <string>
#include <iostream>
#include "Item.h"

// default constructor
itemClass::itemClass()
{
	sf::SoundBuffer SoundBuffer;
	if (!SoundBuffer.loadFromFile("resources/Cha_Ching.wav")) {
		std::cout << "cannot open audio";
		sf::sleep(sf::seconds(5));
	}
	sf::Sound Sound(SoundBuffer);

	itemReward = 5;
}

// overloaded constructor
itemClass::itemClass(int x, int y, int xLimit, int yLimit, std::string spriteFile, EntityType type)
{
	if (!texture.loadFromFile(spriteFile)) {
		cout << "Error loading " << spriteFile << endl;
	}
	sprite = sf::Sprite(texture);

	if (!SoundBuffer.loadFromFile("resources/Cha_Ching.wav")) {
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
	itemReward = 10;
}

// takes time and returns a score that gets smaller as the game progresses
int itemClass::getScoreUpdate(int timeDelay)
{
	return (itemReward);
}

// plays entity sound and updates message board
string itemClass::say()
{
	Sound.play();
	message = "Message: You pick up the item.";
	return message;
}

