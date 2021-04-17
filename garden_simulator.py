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
    
    def water(self, name):
        """Waters plant according to data in file of plant information and adds 
        points to health bar.
        
        Args: 
            name(str): plant name
        
        Returns:
            health(int): updated health points
        """
        
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
        """
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




def main(filepath, start_date=None, end_date=None):
    """Read events from a file and print out a timeline of events from
    start_date to end_date.
    
    Args:
        filepath (str): path to a tab-delimited file where each line consists
            of a date, a tab, and a description of an event.
        start_date (Event, str, tuple, or None): the earliest date of interest
            (if None, include dates as far back as possible).
        end_date (Event, str, tuple, or None): the latest date of interest (if
            None, include dates as far forward as possible).
    
    Side effects:
        Writes to stdout.
    """
    
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.event_file, start_date=args.startdate, end_date=args.enddate)


#trying push