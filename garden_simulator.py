""" A garden simulator for growing plants """

# PLANT = {name, water, season, environment, sunlight, ph, phase} 
  # sunflower, daisy, potato
class Plant:
    """Plants grown in the garden simulation
    
    Attributes:
        name (str): plant name 
        health (int): plant lifecycle where certain levels indicate phase of 
        growth
    """
    
   def __init__(self, filepath, name, min_sunlight, max_sunlight, min_ph, 
                max_ph,  max_HP, water, starting_HP=0):
        """Initializes plant name and health.
        
        Args: 
            name (str): plant name
            filepath(str): reads file on plant information
            health (int): plant lifecycle where certain levels indicate phase of 
            growth; initializes health of plant to zero
        """
        self.name = name
        self.min_sunlight = min_sunlight
        self.max_sunlight = max_sunlight
        self.min_ph = min_ph
        self.max_ph = max_ph
        self.max_HP = max_HP
        self.water = water
        self.starting_HP = starting_HP
        plant = {}
        with open(filepath, "r", encoding = "utf-8") as f:
            for x in f.readlines():
                line = line.split()
                plant = {name: line[0],
                         water: line[1],
                         season: line[2],
                         environment: line[3],
                         min_sunlight: line[4],
                         max_sunlight: line[5],
                         min_ph: line[6],
                         max_ph: line[7],
                         max_HP: line[8]} 
    
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
            if (self.starting_HP == 0):
                return stage == 1
            # Seedling stage
            elif (0 < self.starting_HP < 5):
                return stage == 2
            # Vegetative stage
            elif  (5 < self.starting_HP < 15 ):
                return stage == 3
            # Bud stage
            elif (15 < self.starting_HP < 30): 
                return stage == 4
            # Flowering stage
            elif (30 < self.starting_HP < 70 ):
                return stage == 5
            # Ripening stage
            elif (70 < self.starting_HP < 100):
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
        if (self.ph < PLANT[6]):
            self.starting_HP = self.starting_HP - 10
        elif (self.ph > PLANT[7]):
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

def main(plant, max_HP): #unsure on how to write this code
    """Allows users to choose plants to grow in garden. 
  
    Args: 
      name(str): plant name
    
    Side effects:
      Writes to stdout
    """
    plantA = Plant()
    plantA.__init__(plant, max_HP)
      
if __name__ == "__main__":
    """Calls main function
    """
main(sunflower, 89)
