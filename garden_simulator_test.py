import pytest
import builtins
from unittest import mock
import garden_simulator
from garden_simulator import Plant
from time import strftime


def test_season():
    """Does season() return the message confirming the current and ideal season?"""
    plant = Plant("plants.csv", 30)
    month = strftime("%B")
    month_season = {"January": "winter",
                    "February": "winter",
                    "March": "spring",
                    "April": "spring",
                    "May": "spring",
                    "June": "summer",
                    "July": "summer",
                    "August": "summer",
                    "September": "fall",
                    "October": "fall",
                    "November": "fall",
                    "December": "winter"}
    if month_season[month] == "spring":
        assert plant.season("sunflower") == "The ideal season for a sunflower is spring. The current season is spring. You can plant a sunflower!"
        assert plant.season("cactus") == "The ideal season for a cactus is summer. The current season is spring. You cannot plant a cactus. :/"
    elif month_season[month] == "summer":
        assert plant.season("cactus") == "The ideal season for a cactus is summer. The current season is summer. You can plant a cactus!"
        assert plant.season("sunflower") == "The ideal season for a sunflower is spring. The current season is summer. You cannot plant a sunflower. :/"
        
def test_water():
    """Does water() return the correct message and add HP to the current_HP"""
    name = self.plants['name']
    waterinfo = self.plants[self.plants['water'] == water]
    watering = self.current_HP + 10
    if water >= 2:
        assert plant.water("sunflower") == "Watering 2 liters of water to sunflower daily" 
        assert plant.water("potato")  == "Watering 5 liters of water to potato daily"
    elif water <2
        assert plant.water('catus') == "Watering 0.5 liter of water to potato daily"
    return watering

def test_ph():
    name = plants["name"]
    max_ph = plant.max_ph
    min_ph = plant.min_ph
    if max_ph >= plants["max_ph"]:
        assert plant.max_ph("sunflower") == "the maximum ph level for sunflower is 7.5"
    if min_ph <= plants["min_ph"]:
        assert plant.min_ph("sunflower") == "the minimum ph level for sunflower is 6"
        
def test_garden1():
    """Does the garden() method work?"""
    plantTest = Plant()
    plantTest.garden('potato')
    plantTest.garden('sunflower')
    plantTest.garden('cactus')
    plantTest.garden('hibiscus')
    plantTest.garden('bamboo')
    plantTest.garden('strawberry')
    
    assert len(plantTest.plant_list) == 5
    
def test_garden2():
    plantTest2 = Plnat()
    plantTest.garden('potato')
    plantTest.garden('sunflower')
    plantTest.garden('cactus')
    plantTest.garden('bamboo')
    
    assert len(plantTest2.plant_list) == 4
    
def test_harvest1():
    """Does harvest() actually harvest"""
    plantTest3 = Plant()
    plantTest.garden('potato')
    plantTest.garden('sunflower')
    plantTest.garden('cactus')
    plantTest.garden('hibiscus')
    plantTest.garden('bamboo')
    plantTest.garden('strawberry')
    plantTest3.harvest('strawberry', 100)
    assert len(plantTest.plant_list) == 4
    
def test_harvest2():    
    plantTest4 = Plant()
    plantTest.garden('potato')
    plantTest.garden('sunflower')
    plantTest.garden('cactus')
    plantTest.garden('bamboo')
    plantTest4.harvest('bamboo', 50)
    assert len(plantTest4.plant_list) == 4
    
   
