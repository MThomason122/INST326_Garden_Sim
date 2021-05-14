""" A garden simulator for growing plants """

import time as t
import pandas as pd

class Plant:
    """Plants grown in the garden simulation
    
    Attributes:
        filepath(str): reads file on plant information
        name (str): plant name
        season (str): ideal season for plant growth
        environment (str): ideal weather and environment conditions for 
        plant growth 
        min_sunlight (int): minimum amount of sunlight for plant growth
        max_sunlight (int): maximum amount of sunlight for plant growth
        min_ph (float): minimum amount of ph in soil for plant growth
        max_ph (float): maximum amount of ph in soil for plant growth
        max_HP (int): maturest lifecycle of plant, ready for harvest
        starting_HP (int): initializes health of plant to zero
    """
     
    def __init__(self, filepath, name, starting_HP=0):
        """Initializes plant name and health.
        
        Args: 
            filepath(str): reads file on plant information
            name (str): name of plant
            starting_HP (int): initializes health of plant to zero
        """
        plants = pd.read_csv(filepath)
        
        self.name = plants[plants["name"]== name]["name"]
        self.season = plants[plants["name"]== name]["season"]
        self.environment = plants[plants["name"]== name]["environment"]
        self.min_sunlight = plants[plants["name"]== name]["min_sunlight"].astype("int")
        self.max_sunlight = plants[plants["name"]== name]["max_sunlight"].astype("int")
        self.min_ph = plants[plants["name"]== name]["min_ph"].astype("float")
        self.max_ph = plants[plants["name"]== name]["max_ph"].astype("float")
        self.max_HP = plants[plants["name"]== name]["max_HP"].astype("float")
        self.water = plants[plants["name"]== name]["water"].astype("float")
        self.starting_HP = starting_HP
        
    def phase(self, name, starting_HP):    
        """Identifies the phase of growth the plant is in based on health points
        
        Args:
            name(str): plant name
            starting_HP(int): initial health points 
        
        Returns:
            stage(int): Stage of life of plant  
        """
        stage = 0
        
    # different variable for changing hp? so instead of starting_HP, jsut straight up hp
        for plant[self.name] in plant:
            # Seed/Germination stage
            if (plant[self.starting_HP] == 0):
                return stage == 1
            # Seedling stage
            elif (0 < plant[self.starting_HP] < 5):
                return stage == 2
            # Vegetative stage
            elif  (5 < plant[self.starting_HP] < 15 ):
                return stage == 3
            # Bud stage
            elif (15 < plant[self.starting_HP] < 30): 
                return stage == 4
            # Flowering stage
            elif (30 < plant[self.starting_HP] < 70 ):
                return stage == 5
            # Ripening stage
            elif (70 < plant[self.starting_HP] < 100) or (self.starting_HP == self.max_HP):
                return stage == 6

    def updatehp(self):
        write to txt
                    
    def water(self, name, water):
        """Waters plant according to data in file of plant information and adds 
        points to health bar.
        
        Args: 
            name(str): plant name
            water(str): a desc of how much water needed
        
        Returns:
            starting_HP(int): updated health points
        """
        watering = self.starting_HP + 10
        print(f"Watering {self.water} amount of water to {self.name}.")
        return watering
        
        
    def season(self, name):
        """Checks if plant is okay to grow in the current season and lets you 
        know which season is ideal
        
        Args:
            name(str): name of plant
        
        Returns:
            Message(str): message about which season is best to plant
        """   
        for plant["season"]  "spring":
            if 
            
    def environment(self, name):
        """Checks the habitat requirements of the plant and 
        
        Returns:
            health(int): updated health points
        """
    
    def sunlight():
        """Checks the suitable amount of sunlight required
        for plants to grow
        
        Returns:
            health(int): updated health points
        """
    
    def ph(self, ph):
        """Determine health points gained or lost according to ph of soil.
        
        Args:
            ph (int): the ph level a plant receives.
        
        Returns:
            health(int): updated health points        
        """
        if (ph < self.min_ph):
            self.starting_HP = self.starting_HP - 10
        elif (ph > self.max_ph):
            self.starting_HP = self.starting_HP - 10
        else:
            self.starting_HP = self.starting_HP + 10
        return starting_HP
        
      
def garden(name):
    """Grow plants in a garden that can hold up to 5 plants.
    
    Args:
        name(str): plant name
        
    Returns:
        garden_list(list): list of plants in garden    
        err_msg (str): if too many plants, user is prompted to wait until opening in 
        garden
    """    
    global plant_list
    plant_list = []
    err_msg = "Too many plants in garden, wait until one is harvested."
    if len(plant_list) < 5:
        plant_list.append(name)
        return plant_list
    else:
        return err_msg   
    
def harvest(name, health):
    """Harvests plant when plant reaches maximum health (maturity)
    
    Args:
        name(str): plant name
        health(int): plant lifecycle where certain levels indicate phase of 
        growth
    
    Side effect:
        Removes plant from garden when health points reach maximum
    """

def main(name, max_HP): #unsure on how to write this code
    """Allows users to choose plants to grow in garden. 
  
    Args: 
      name(str): plant name
      max_HP (int): helath at which plant is most mature
    
    Side effects:
      Writes to stdout
    """
    plantA = Plant()
    plantA.__init__(name, max_HP)
      
if __name__ == "__main__":
    """Calls main function
    """
main(name, max_HP)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          