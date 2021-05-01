""" A garden simulator for growing plants """

PLANT = {name, water, season, environment, sunlight, ph, phase} 
  # sunflower, daisy, potato

class Plant:
    """Plants grown in the garden simulation
    
    Attributes:
        name (str): plant name 
        health (int): plant lifecycle where certain levels indicate phase of 
        growth
    """

    
    def __init__(self, name, filepath, health=0):
        """Initializes plant name and health.
        
        Args: 
            name (str): plant name
            filepath(str): reads file on plant information
            health (int): plant lifecycle where certain levels indicate phase of 
            growth; initializes health of plant to zero
        """
    
    def phase(self, name, health):    
        """Identifies the phase of growth the plant is in based on health points
        
        Args:
            name(str): plant name
            health(int): plant lifecycle where certain levels indicate phase of 
            growth
        
        Returns:
            stage(int): Stage of life of plant  
        """
        stage = 0
        for name in PLANT:
            # Seed/Germination stage
            if (health == 0):
                return stage == 1
            # Seedling stage
            elif (0 < health < 5):
                return stage == 2
            # Vegetative stage
            elif  (5 < health < 15 ):
                return stage == 3
            # Bud stage
            elif (15 < health < 30): 
                return stage == 4
            # Flowering stage
            elif (30 < health < 70 ):
                return stage == 5
            # Ripening stage
            elif (70 < health < 100):
                return stage == 6
            
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
        print(f"Watering {PLANT[1]} amount of water to {PLANT[0]}.")
        return watering
        
        
    def season(self, name):
        """Checks if plant is okay to grow in the current season and lets you 
        know which season is ideal
        
        Args:
            name(str): name of plant
        
        Returns:
            Message(str): message about which season is best to plant
        """   
    
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
    
    def ph():
        """Determine health points gained or lost according to ph of soil.
        
        Returns:
            health(int): updated health points        
        """
        
      
def garden(name):
    """Grow plants in a garden that can hold up to 5 plants.
    
    Args:
        name(str): plant name
        
    Returns:
        garden_list(list): list of plants in garden    
        str: if too many plants, user is prompted to wait until opening in 
        garden
    """    
    
def harvest(name, health):
    """Harvests plant when plant reaches maximum health (maturity)
    
    Args:
        name(str): plant name
        health(int): plant lifecycle where certain levels indicate phase of 
        growth
    
    Side effect:
        Removes plant from garden when health points reach maximum
    """

def main():
    """Allows users to choose plants to grow in garden. 
  
    Args: 
      name(str): plant name
    
    Side effects:
      Writes to stdout
    """
    
    harvest()
      
if __name__ == "__main__":
    """Calls main function
    """
