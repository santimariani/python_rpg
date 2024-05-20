import random
import time

import entities

from classEngine import Engine
from classCharacter import Hero, Opponent
from classDay import Day
from classTournament import Tournament
from classItem import Item
from classFight import Fight
from tools import slow_print
                
run_game = Engine()
run_game.begin_game()

start_day = Day()
start_day.run_day()

fight = Fight()

