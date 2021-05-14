""" A garden simulator for growing plants """

import time as t
import pandas as pd

class Plant:
    """Plants grown in the garden simulation
    
    Attributes:
        current_HP (int): updated health points of a plant
        plants (dataframe): dataframe of plant data CSV
    """
     
    def __init__(self, filepath, starting_HP=0):
        """Initializes plant name and health.
        
        Args: 
            filepath(str): reads file on plant information
            name (str): name of plant
            starting_HP (int): initializes health of plant to zero
        """
        self.plants = pd.read_csv(filepath)
        self.current_HP = starting_HP
        
    def phase(self, name, current_HP):    
        """Identifies the phase of growth the plant is in based on health points
        
        Args:
            name(str): plant name
            current_HP(int): updated health points 
        
        Returns:
            stage(int): Stage of life of plant  
        """
        nameinfo = self.plants[self.plants["name"== name]]
        stage = 0
        # Seed/Germination stage
        if (self.current_HP == 0):
            stage = 1
            return stage
        # Seedling stage
        elif (0 < self.current_HP < 5):
            stage = 2
            return stage
        # Vegetative stage
        elif  (5 < self.current_HP < 15 ):
            stage = 3
            return stage
        # Bud stage
        elif (15 < self.current_HP < 30): 
            stage = 4
            return stage
        # Flowering stage
        elif (30 < self.current_HP < 70 ):
            if name == "strawberry":
                stage = 6
            else:
                stage = 5
            return stage
        # Ripening stage
        elif (70 < self.current_HP < 100) or (self.current_HP == int(nameinfo["max_HP"].iloc[0])):
            stage = 6
            return stage

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
        
        
    def season(self, name, ):
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
    #look at aardvark
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

def garden(name):
    """Grow plants in a garden that can hold up to 5 plants.
    
    Args:
        name(str): plant name
        
    Returns:
        garden_list(list): list of plants in garden    
        err_msg (str): if too many plants, user is prompted to wait until opening in garden
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
    Plant.
    name = input("Please choose from the following plants: sunflower, potato, cactus, hibiscus, bamboo, strawberry\n")
    
      
if __name__ == "__main__":
    """Calls main function
    """
main(name, max_HP)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          