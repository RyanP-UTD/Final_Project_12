# BUG SWATTER

## Demo
Demo Video: [<URL>](https://youtu.be/bTtmLko0rWk)

## GitHub Repository
GitHub Repo: [<URL>](https://github.com/RyanP-UTD/Final_Project_12.git)

## Description
This game is called Bug Swatter, its a simple game that does is to click the bug and destory. That is all. 

I have made my own png image of a housefly in which would make it appealing for players to visually see. 
Note that I will be using Red box instead of bug or housefly for more readabilty and to avoid confusion when reading this description. 
I made two classes that are Red_box Mechanices and Animation classes. And in main class, I added the texts like Scores, Clicks, and Levels for 
players to know the information. 

Lets talk about what does the Red_box_Mechanic class function do:

The red_box (it invisible because it set to alpha 0) acts as a guide to understand how its being implmented. For example, dectection
collision that once the mouse clicks on the red box, it set to inactive and the time of being inactive resets after it meets the condtion.
and set the red_box to alpha for a invisibilty. overall, its function is to act the guide for understanding. As well as the function of collision on mouse click


What does Animation Mechanics class do: (The hard one, but my favorite feature)

As for the Animation Mechanics class, it got the teleportation that teleport to the new location after the red_box becomes inactive. Once it set active, it will 
render in a new location. And there is a smaller version of teleportation in which I call it as fly, It makes it feels more natural to move as a bug (the housefly) 
to move in a small range around 45-50px. Also it got the rotation that the image of a bug (the housefly) rotates for every 10 degrees in a complete rotation. Therefore
it would make it bit more natural to move. 

Finally the main class, is used for the graphics such as adding the border, name of the title, Adding the png file into the red_box
having a functionable of Clicks, Scores, Levels that interacts on mouse button. 

Lastly

So far this is the explaination of how it done and set up, It only requires pygame that is a third party libraries. Other than that, its all builtin. 

## Future improvements
So far, I needed to add lots of different types of bugs (not the computer bug) and add it to the game that once it swatted on the bug, a new type bug will pop up, 

Next is to improve the level indicator that for every level 10, one extra red_boxes will be added on to the game. Similarily of catching a number of fishes in one pond. 


