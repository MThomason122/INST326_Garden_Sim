""" A garden simulator for growing plants """

# PLANT = {name, water, season, environment, sunlight, ph, phase} 
  # sunflower, daisy, potato
plant = {}

class Plant:
    """Plants grown in the garden simulation
    
    Attributes:
        filepath(str): reads file on plant information
        plant (dict): plant name, water, season, environment, minimum and
        maximum sunlight, minimum and maximum ph and maximum health
        starting_HP (int): initializes health of plant to zero
    """
     
    def __init__(self, filepath, plant, starting_hp=0):
        """Initializes plant name and health.
        
        Args: 
            filepath(str): reads file on plant information
            plant (dict): plant name, water, season, environment, minimum and
            maximum sunlight, minimum and maximum ph and maximum health
            starting_HP (int): initializes health of plant to zero
        """
        with open(filepath, "r", encoding = "utf-8") as f:
            for x in f.readlines():
                line = x.split()
                self.plant = {"name": line[0],
                        "water": line[1],
                        "season": line[2],
                        "environment": line[3],
                        "min_sunlight": line[4],
                        "max_sunlight": line[5],
                        "min_ph": line[6],
                        "max_ph": line[7],
                        "max_HP": line[8]}
        self.starting_hp = starting_hp
 
            
    def phase(self, plant, starting_HP):    
        """Identifies the phase of growth the plant is in based on health points
        
        Args:
            name(str): plant name
            starting_HP(int): initial health points 
        
        Returns:
            stage(int): Stage of life of plant  
        """
        stage = 0
        for plant["name"] in self.plant:
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
            

            
    def water(self, plant):
        """Waters plant according to data in file of plant information and adds 
        points to health bar.
        
        Args: 
            name(str): plant name
            plant(dict): dictionary containing amount of water needed 
        
        Side effects:
            prints a string stating the amount plant is watered by
        
        Returns:
            starting_HP(int): updated health points
        """
        for plant["name"] in plant:
            self.starting_HP += 10
            plant_water_amount = self.plant["water"]
            print(f"Watering {plant_water_amount} amount of water to {self.plant}.")
            return self.starting_HP
        
        
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
    
    def sunlight(self):
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
        if (ph < self.plant["min_ph"]):
            self.starting_HP = self.starting_HP - 10
        elif (ph > self.plant["max_ph"]):
            self.starting_HP = self.starting_HP - 10
        else:
            self.starting_HP = self.starting_HP + 10
        return self.starting_HP
        
      
def garden(name):
    """Grow plants in a garden that can hold up to 5 plants.
    
    Args:
        name(str): plant name
        
    Returns:
        garden_list(list): list of plants in garden    
        err_msg (str): if too many plants, user is prompted to wait until opening in 
        garden
    """    
    # global plant_list
    plant_list = []
    err_msg = "Too many plants in garden, wait until one is harvested."
    if len(plant_list) < 5:
        plant_list.append(Plant.plant["name"])
        return plant_list
    else:
        return err_msg   
    
def harvest(name, starting_HP):
    """Harvests plant when plant reaches maximum health (maturity)
    
    Args:
        name(str): plant name
        starting_HP(int): plant lifecycle where certain levels indicate phase of 
        growth
    
    Side effect:
        Removes plant from garden when health points reach maximum
    """

def main(plant): 
    """Allows users to choose plants to grow in garden. 
  
    Args: 
      name(str): plant name
      max_HP (int): health at which plant is most mature
    
    Side effects:
      Writes to stdout
    """
    user = input("Enter 1: sunflower, potato, cactus, hibiscus, bamboo, strawberry \n")
    p_name = plant["name"]
    Plant.water(p_name)
    Plant.garden(p_name)
    

if __name__ == "__main__":
    """Calls main function
    """
    main(plant)

