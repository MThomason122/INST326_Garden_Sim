""" A garden simulator for growing plants """

from time import strftime
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
        nameinfo = self.plants[self.plants["name"]== name]
        stage = 0
        # Seed/Germination stage
        if (self.current_HP == 0):
            stage = 1
        # Seedling stage
        elif (0 < self.current_HP < 5):
            stage = 2
        # Vegetative stage
        elif  (5 < self.current_HP < 15 ):
            stage = 3
        # Bud stage
        elif (15 < self.current_HP < 30): 
            stage = 4
        # Flowering stage
        elif (30 < self.current_HP < 70 ):
            if name == "strawberry":
                stage = 6
            else:
                stage = 5
        # Ripening stage
        elif (70 < self.current_HP < 100) or (self.current_HP == int(nameinfo["max_HP"].iloc[0])):
            stage = 6
        return stage
        
    def season(self, name):
        """Checks if plant is okay to grow in the current season and lets you 
        know which season is ideal
        
        Args:
            name(str): name of plant
        
        Returns:
            Message(str): message stating the current season and the ideal 
            season is for growth of plant chosen
        """   
        infoname = self.plants[self.plants["name"]== name]
        month = strftime("%B")
        month_season = {"January": "winter",
                        "February": "winter",
                        "March": "spring",
                        "April": "spring",
                        "May": "spring",
                        "June": "summer",
                        "July": "summer",
                        "August": "summer",
                        "September": "summer",
                        "October": "fall",
                        "November": "fall",
                        "December": "winter"}
        if infoname.season.values[0] == month_season[month]:
            statement = f"The current season is {month_season[month]}. You can plant a {name}!"
        else:
            statement = f"The current season is {month_season[month]}. You cannot plant a {name}. :/"
        return (f"The ideal season for a {name} is {infoname.season.values[0]}."
                f" {statement}")
        
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
    
def harvest(name, current_HP):
    """Harvests plant when plant reaches maximum health (maturity)
    
    Args:
        name(str): plant name
        health(int): plant lifecycle where certain levels indicate phase of 
        growth
    
    Side effect:
        Removes plant from garden when health points reach maximum
    """
    if current_HP == 100:
        plant_list.remove(name)
        print(f'{name} has been harvested!')
    else:
        print(f'I''m sorry, but {name} is not ready for harvest')
    
    
def main(filepath, starting_HP=0): #unsure on how to write this code
    """Allows users to choose plants to grow in garden. 
  
    Args: 
                
    
    Side effects:
        Writes to stdout
    """
    plant = Plant(filepath, starting_HP)
    name = input("Please choose from the following plants: sunflower, potato, cactus, hibiscus, bamboo, strawberry\n")
    print(plant.season(name))
    
if __name__ == "__main__":
    """Calls main function
    """
    main("plants.csv", 30)
    
    
    