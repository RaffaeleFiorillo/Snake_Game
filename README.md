# Snake_Game
Simple python implementation of the classic Snake Game in under 100 lines of code.

## Printscreen of the game:
![snake gameplay print](https://user-images.githubusercontent.com/75253335/140090755-c37a3d47-4c11-43f5-b0ea-a222a417f737.png)

## Imported Libraries:
 - random;
 - pygame;

## Main Goal:
 Eat as much food as possible.
 
## Dying Condition:
 The head of the snake must touch any other part of the snake's body.
 
## Score:
 The score can be seen in the top left corner of the window, in red numbers. It represents the size of the snake (or how much food has been eaten).

## Description:
 - The snake moves in the same direction until one of the arrows is pressed;
 - There is "food" in the game (yellow square) which the snake can eat;
 - Every time the food is eaten (head of the snake and food are in the same position) the snake grows;
 - The snake "dies" (Game Over) when it touches itself;
 - If the snake goes beyond the game's window it appears in the opposite side of the window;
