# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from enum import Enum, auto
from collections import namedtuple

# Объявляем наименованный кортеж для свойств персонажа
CharacterBase = namedtuple('CharacterBase', ['CharacterClass', 'CharacterRace'])


class CharacterClass(Enum):
    WARRIOR = auto()
    MAGICIAN = auto()


class CharacterRace(Enum):
    ELF = auto()
    ORC = auto()
    HUMAN = auto()


class CharacterAge(Enum):
    YOUNG = auto()
    ADULT = auto()
    OLD = auto()


class CharacterAbilities(Enum):
    PUNCH = auto()
    FIREBALL = auto()
    TELEPORTATION = auto()
    MINDCONTROL = auto()
    HEALING = auto()
    ROAR = auto()


# Класс компануемого персонажа


class Character:
    def __init__(self, name):
        self.name = name
        self.class_race = None
        self.age = None
        self.abilities = []
        self.years_old = None

    def __str__(self):
        info: str = f'Character name: {self.name} \n ' \
                    f'Character Class and Race: {self.class_race.CharacterClass.name} & ' \
                    f'{self.class_race.CharacterRace.name} \n' \
                    f'Age: {self.age} \n' \
                    f'Character Abilities: {[it.name for it in self.abilities]} \n' \
                    f'{self.years_old} years'
        return info


# Абстрактный класс задающий интерфейс строителя


class Builder(ABC):

    @abstractmethod
    def select_class_race(self) -> None: pass

    @abstractmethod
    def select_age(self) -> None: pass

    @abstractmethod
    def select_abilities(self) -> None: pass

    @abstractmethod
    def create_character(self) -> Character: pass


# Реализация конкретных строителей


class ElfMagicianBuilder(Builder):

    def __init__(self):
        self.character = Character("Eldur")
        self.character.years_old = 365

    def select_class_race(self) -> None:
        self.character.class_race = CharacterBase(CharacterClass.MAGICIAN, CharacterRace.ELF)

    def select_age(self):
        self.character.age = CharacterAge.ADULT

    def select_abilities(self) -> None:
        self.character.abilities.extend(
            [
                it for it in (CharacterAbilities.FIREBALL,
                              CharacterAbilities.TELEPORTATION,
                              CharacterAbilities.HEALING,
                              )
            ]
        )

    def create_character(self) -> Character:
        return self.character


class OrcWarriorBuilder(Builder):

    def __init__(self):
        self.character = Character("Baldur")
        self.character.years_old = 48

    def select_class_race(self) -> None:
        self.character.class_race = CharacterBase(CharacterClass.WARRIOR, CharacterRace.ORC)

    def select_age(self):
        self.character.age = CharacterAge.YOUNG

    def select_abilities(self) -> None:
        self.character.abilities.extend(
            [
                it for it in (CharacterAbilities.PUNCH,
                              CharacterAbilities.MINDCONTROL,
                              CharacterAbilities.ROAR,
                              )
            ]
        )

    def create_character(self) -> Character:
        return self.character


# Класс Director, Отвечающий за поэтапное создание персонажа

class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder: Builder):
        self.builder = builder

    def create_character(self):
        if not self.builder:
            raise ValueError("Builder didn't set")
        self.builder.select_class_race()
        self.builder.select_age()
        self.builder.select_abilities()


if __name__ == '__main__':
    director = Director()
    for it in (ElfMagicianBuilder, OrcWarriorBuilder):
        builder = it()
        director.set_builder(builder)
        director.create_character()
        character = builder.create_character()
        print(character)
        print('______________________________')
