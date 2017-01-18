# martiantrail
A game where you go to Mars.  Ha!


/**********************************
* Welcome to the Trail to Mars (v1.0.0)
* The game has two phases: travel to Mars and construction of a permanent colony.
* Unlike the Oregon Trail, you can launch un-manned supply missions, prior to departing on a manned mission with your intended colonists.
* Score is determined by whether you survive the journey and the success of your Martian colony. *******/
 
* I've ganked some of my inspiration/approach to thinking this out from Doug Sandford via this Khan Academy tutorial.  Specifically, there may be some leftover verbiage in the part below: https://www.khanacademy.org/computer-programming/oregon-trail/4534161028153344 

* Once you start, I recommend you buy things at the shop. They have:
* Saturn Rockets - for launching your ships. // if I try to make this more SLS-themed, they would be called "SLS Boosters" I guess.  I don't know if we've named them yet.
* Food - to eat! If you don't have this, you may die. // Not sure if there needs to be a food-production mechanism in the game.  
* Spacesuits - to facilitate extra-vehicular maneuvers (collecting energy & minerals). // this is my assumed analog to ammunition
* Spare parts and tools - to fix your ship. // maybe?
* Then, you will have to avoid asteroids.  Unfortunately, any deviations to avoid asteroids will take you off your plotted course.  You need to remember and reaim your trajectory. // my intended game mechanics require you to choose an appropriate launch date and trajectory.  This shouldn't be difficult, and is affected heavily by RNG, but is the major 'learning point' of the game.  To educate about launch windows to Mars, and perhaps a little bit about gravitational mechanics.
* Once you finish (dead or not) you can post your score in the comments and see if you are worthy of the Martian Top Ten.
 
 
 **Some Random Stuff About Getting to Mars**
* In theory, the closest that Earth and Mars would approach each other would be when Mars is at its closest point to the sun (perihelion) and Earth is at its farthest (aphelion). This would put the planets only 33.9 million miles (54.6 million kilometers) apart. However, this has never happened in recorded history. The closest approach of the two planets occurred in 2003, when they were only 34.8 million miles (56 million km) apart.
* The two planets are farthest apart when they are both at their farthest from the sun, on opposite sides of the star. At this point, they can be 250 million miles (401 million km) apart.
* The average distance between the two planets is 140 million miles (225 million km).
* Light travels at approximately 186,282 miles per second (299,792 km per second). Therefore, a light shining from the surface of Mars would take the following amount of time to reach Earth (or vice versa):
* *Closest approach: 182 seconds, or just over 3 minutes
* *Farthest approach: 1,342 seconds, or just over 22 minutes
* *On average: 751 seconds, or just over 12.5 minutes
* The fastest spacecraft launched from Earth was NASA's New Horizons mission, which is en route to Pluto. In January 2006, the probe left Earth at 36,000 mph (58,000 kph). The time it would take such a probe to get to Mars would be:
* * Closest approach: 942 hours (39 days)
* * Farthest approach: 6,944 hours (289 days)
* * On average: 3,888 hours (162 days)
* Here is a list of how long it took several historical missions to reach the red planet. Their launch dates are included for perspective.
* *Mariner 4, the first spacecraft to go to Mars (1964 flyby): 228 days
* *Mariner 6 (1969 flyby): 155 days
* *Mariner 7 (1969 flyby): 128 days
* *Mariner 9, the first spacecraft to orbit Mars (1971): 168 days
* *Viking 1, the first U.S. craft to land on Mars (1975): 304 days
* *Viking 2 Orbiter/Lander (1975): 333 days
* *Mars Global Surveyor (1996): 308 days
* *Mars Pathfinder (1996): 212 days
* *Mars Odyssey (2001):  200 days
* *Mars Express Orbiter (2003): 201 days
* *Mars Reconnaissance Orbiter (2005): 210 days
* *Mars Science Laboratory (2011): 254 days
 
 
**Assumed Game Stuff**
* Language: Python
* Features: Browser-based, no login, 
* Game style: Text-based adventure + 2d minigame + illustrations
* The player can decide these starting conditions: 
* * When to launch (player is expected to choose the optimal launch date based on the shortest distance to Mars - a fact they may have to research outside of the game).
* * How many supply missions to send
* * How much fuel in each mission (both the manned and unmanned missions - a figure that the player will need to calculate - however, the fuel capacity, economy and distance are provided - along with a simple calculator)
* * What supplies to take? (Similar to the original Oregon Trail game, the player must choose the amount and variety of items to purchase - it is entirely possible for the player to choose badly and depart without a required item.  However, it's not a particularly difficult calculation to make - some items cannot be sourced en route (food, spacesuits), and some can (water, helium, hydrogen).
* * How many crew members to take?
 
* I suppose that there could be two development milestones within this game - the first could be the initial journey to Mars and the second could be the colonization phase.  Perhaps there is no point to making the colonization phase - although, unlike the Oregon Trail, you can't just say "congrats you're at the Willamette Valley, go make a farm."  To have arrived is hardly enough.  Maybe it would be better if you can decide to either colonize or set up a research station.  Perhaps those two outcomes provide different scores (with the goal to get a high score).
 


**Game Screens**
* Title Screen
* Instructions yes/no
* Introduction
* Choose your supply ship plan
* Choose your trajectory
* Purchase supplies
* Choose launch date


**Some variables that I assume will be needed**
* var score = 0;
* var health = "Good";
* var deathcause = "asphyxiation";
* var rockets = 0;
* var spacesuits = 0;
* var oxygen = 0;
* var water = 0;
* var hydrogen = 0;
* var helium = 0;
* var tools = 0;
* var distanceleft = 0;
* var trajectory = "optimal";
* var money = 1000000000; // One billion dollars to start.
