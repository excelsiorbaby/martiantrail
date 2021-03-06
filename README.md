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
* * Closest approach: 182 seconds, or just over 3 minutes
* * Farthest approach: 1,342 seconds, or just over 22 minutes
* * On average: 751 seconds, or just over 12.5 minutes
* The fastest spacecraft launched from Earth was NASA's New Horizons mission, which is en route to Pluto. In January 2006, the probe left Earth at 36,000 mph (58,000 kph). The time it would take such a probe to get to Mars would be:
* * Closest approach: 942 hours (39 days)
* * Farthest approach: 6,944 hours (289 days)
* * On average: 3,888 hours (162 days)
* Here is a list of how long it took several historical missions to reach the red planet. Their launch dates are included for perspective.
* * Mariner 4, the first spacecraft to go to Mars (1964 flyby): 228 days
* * Mariner 6 (1969 flyby): 155 days
* * Mariner 7 (1969 flyby): 128 days
* * Mariner 9, the first spacecraft to orbit Mars (1971): 168 days
* * Viking 1, the first U.S. craft to land on Mars (1975): 304 days
* * Viking 2 Orbiter/Lander (1975): 333 days
* * Mars Global Surveyor (1996): 308 days
* * Mars Pathfinder (1996): 212 days
* * Mars Odyssey (2001):  200 days
* * Mars Express Orbiter (2003): 201 days
* * Mars Reconnaissance Orbiter (2005): 210 days
* * Mars Science Laboratory (2011): 254 days
 
 
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


**Score**
// The player's score begins at 0 and cannot go less than 0.  Points are scored by arriving on Mars with crew and supplies.  Certain combinations of supplies may trigger bonus conditions, such as setting up a research lab, hydroponics bay, crew quarters, etc.  Crew deaths or illness count as negative points.

**Health**
// Health reflects the overall condition of the surviving crew.  Individual crew members may have unique conditions, based on RNG or player actions.  For example, the pilot may have hypothermia from staying out on a spacewalk too long.  Or, the crew may have forgotten citrus fruit and each one contracted scurvy.  The health of each crew member is a score from 0-5 where 0 is dead and 5 is excellent.  The crew member health scores are averaged, excluding any dead crew members (deaths result in points being lost and then do not affect the game play from there on out).

**Death**
// Crew members are affected by RNG-events and player actions.  Each event may add or subtract 1 or 2 health points, but the crew member cannot go below 0 or above 5.  If a crew member goes from any number of points to 0, they die immediately.  They cannot be resurrected.  Some causes of death may include: asphyxiation (no oxygen), dehydration (no water), starvation (no food), hypothermia (too cold), scurvy (RNG event based on low food stocks), boneitis (RNG event based on low food stocks), asteroid collision (RNG event based on player's chosen trajectory), floating away (RNG event during mining minigame), radiation (too much time spent in the minigame), or hyperthermia (RNG event where the ship catches fire).
// So, there are event-based and choice-based causes of death.  
// Ideally, a badly-plotted trajectory will leave the player floating in space, unable to replinish their supplies.  However, careful mineral collection may allow the player to gather fuel and resume course with a controlled burn.  Or, we just say you're off course and kill the attempt.  The controlled burn could up the chance of a RNG event occurring...
// There is a definite random aspect to death that is intended here.  If a player made 'perfect' choices, they will not always win.

**Mining Minigame**
// In the original Oregon Trail, the player used ammunition to go out and shoot animals for food.  Based on their location on the map, the food was plentiful or scare, and the selection of animals changed occasionally.  In this game, we're going to analog that to the collection raw minerals using a harpoon-like space gun.  I'll need to do some research on what may actually be found on asteroids, but assumedly, asteroids will glide by with crystals of water, hydrogen, helium, oxygen, etc. attached to the asteroid.  Harpooning a loaded asteroid will yeild a quantity of mineral energy.  We'll assume that the crew turns hydrogen and oxygen and water into food or something like that.  Ideally, this process is simplified for the player - they harpoon three waters and 2 oxygens, so the game says "You collected 5 energy.  The replicator machine created 8 food rations." or something to that effect.
// In order to go out harpooning, you need spacesuits and/or harpoons.  Not sure I'm sold on having 'harpoons' as a consumable item, but I'll have to give that some thought.


**Trajectories**
// There is, of course, an ideal trajectory between Earth and Mars.  There is a point when they are closest together and that date occurs every two years.  There's also the moon in the way.  And perhaps some other asteroids of note, if some research could pull together a list.  Now, obviously orbital mechanics are a bit much for a game, so we need to dumb this down into something fun, calculable, and strategic.
// You could choose between a collection of launch sites and landing sites.  
// Some additional complexity/scoring could be introduced if you land your supply missions at a different location than the crew mission.  You'd have to bring a dune buggy to be able to score the supply drops.  This sounds too complex.
// You could choose from a variety of pre-set trajectories, similar to choosing whether to go to Chimney Rock or continue through the mountain pass.  That's a little boring, but true to the original game.
// I can picture an interface where you adjust the calendar by clicking up/down and with each changed day, you see a minor change to the trajectory, where at the extreme ends, you miss Mars entirely.  While the interface seems simple, the strategic value of this is like nothing and it sounds like busy work finding the right day on the calendar.
// Compounding on that boring idea, you could display the relative fuel requirements of each launch date/trajectory and let the player make a choice.
// Even further, there could be a minimum amount of time between launches, say 2 weeks between.  There may be a 3-month window of time to launch at each parahelion - so the player would have to carefully time it to get 5 launches in there (still kind of boring).  The trick could be that the moon gets in the way at certain dates - although I think the moon moves faster than that and it would get complex too fast.  It doesn't have to be 100% realistic, but we're going for high 90% at least.
// All that said, the idea behind trajectories is to instill in the player that there is a short period of time in which Earth and Mars are closest together.  It's an educational game, after all.  The player's simple calculcations to find the ideal trajectory should inform them on the basic mission plan for SLS.

**Distance**
// As each supply mission departs on its trajectory, there will be a countdown showing the time and number of miles (kilometers?  nautical miles?) remaining on the journey.  Supply missions are not piloted by the player, but are affected by the RNG.
// A possible minigame could mimic the journey down the Snake River, where the player must pilot the ship between asteroids using the directional pad.  I find the asteroid stuff a bit cliche, so i'm not stuck on this, but otherwise the game is probably a bit dull.
// I'm more interested in a slightly more complex trajectory planning minigame, where the player must remember and adjust to any modifications to the trajectory.  However, I don't want to get into Kerbal territory, or anything that requires more than a directional pad or point-and-shoot interface.
// It occurs to me that one of the scoring aspects could be "soonest to step foot on Mars" which would incentivize careful fuel/trajectory choices.

**Colonization**
// The intended end of the game involves landing on Mars and setting up a colony.  
// In my mind, this is an entire phase, where you watch the crew land and begin combining your resources into colony parts.  I don't foresee it being a particularly interactive phase, more of a 'see what grows' thing. 
// For example, if you brought 2 hydroponics labs and 3 incinerators, you might come up with some sort of carbon-nanotube production.  I don't know.  That seems way too complex.  I was thinking more like recipes -- '1 habitat' '1 humidifier' and '2 conveyor belts' becomes a tomato factory.  But that seems blah.  
// Perhaps we lose the second 'phase' aspect to the game and score based on the supplies that make it to Mars.  There should be a difference between arriving with 800 rations and arriving with 200 rations and a food production unit.  I don't want it to be ridiculously complex though.  There's also the affects of the RNG on the supply missions - if your dune buggy was on a failed mission - then you can't go get the supply drop that fell on the south pole.  etc.

**Player Console**
// During the game, the player will need to see certain information.
* Solar System Map (zoomed) - shows the player the relative position of their ships, Earth, Mars, the Moon, perhaps some of the asteroids, space station? - but most importantly, it will display their chosen trajectory and the position of the manned ship along it.  Of course, all this stuff is moving throughout the journey.  Finding a way to accurately, understandably display the information will be key.  Perhaps, a grid-based system.
* Supply Mission statuses - each supply ship will have departed on its trajectory and needs to display its fuel level, days remaining, miles remaining, and health.
* Crew statuses - each crew member has its own health counter, and may have accumulated bonus/negative effects.  There are also multiple roles.  Dead crew members should still be displayed - although as a skull.
* Ship status - the crew ship will have an overall health rating and gauges for the supplies on board.
* Control buttons - the player needs a button to click to go gather minerals, or repair the ship, or conduct experiments.  If we go with the possibility of a 'bad trajectory' there may be a 'controlled burn' button to put the ship back on course.  There might also be some fun in having an 'eject' button that jettisons the crew in an escape pod.  It might be NASA-thematic, but certainly kind of hard to gamify.
* Score - I guess the player might want to see their score throughout.  And if they click it, they could see a log of the scored events.

**Milestones**
// In the original Oregon Trail, the player periodically would encounter towns, forts, rivers and landmarks.  There's not a lot of those in space.  All of the analogs I've imagined so far involve asteroids or planetlets.  Comets wouldn't really be all that realistic, although space junk might be - or perhaps some easter eggs like an ancient chinese rocket-chair. lol.  I think a lot of the magic will be in coming up with a list of 15-20 milestones/landmarks that are each unique, interesting, but realistic to the game.  Another point to think about is that the original game followed a linear path and hit all the same landmarks -- the trajectory-based approach would logically miss some landmarks or perhaps hit them in a different order.  That might mean that we need more landmarks, or a grid-based approach, or a scoring system that incentivizes the player to hit as many landmarks as possible.
// This approach leans heavily towards letting the player choose an initial macro trajectory before launch and then adjust the trajectory throughout the game.  THey could think that they are going to hit the "abandoned soviet moon probe" to pick up some extra spacesuits, but as they get closer, it would become apparent that they need to adjust course on the micro level.  HMMM.
// Part of the problem here is that the landmarks, decisions and choices in the original game comprise a small set that is memorable and iconic.  The addition of a 3-dimensional space and changing trajectory eliminate the linear nature of the original game.  I think that careful design can mimic this feeling and charm, but still seem realistic.

**Landing Minigame**
// There seems like ample opporutnity to create a fun lander minigame.  The ship will need to land on Mars, so giving the player the opporutnity to screw it all up at the last minute sounds fun - and faithful to the original game.
