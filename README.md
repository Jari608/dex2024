## Introduction
This is Mike 🧑🏼‍🎓, Mike likes to cook and lives together with four students. Every weekend, Mike decides what he wants to cook the next week and creates a groceries list.
Before getting the groceries Mike decided what meal to prepare for every weekday and asks his roommates when they will attend dinner. 

## Objective
implement a function that generates a grocery list for the week based on required ingredients and desired servings, applying the Red-Green-Refactor cycle.

- RED: Create the test, we will provide you with the fixtures:
  - The resulting shopping list
  - The recipes
  - The meal plan for next week


- GREEN: implement the function to make the test pass. The function should calculate the total amount of each ingredient based on the servings per day.

- REFACTOR: refactor the code. Possible improvements:
  - Add validation to ensure the input list is valid (e.g., contains positive integers).
  - Break the logic into smaller, more maintainable functions (e.g., calculating total servings and generating the list in separate functions).

## Bonus
Add Ingredient Shortage Handling: 
- Extend the function to check if the ingredients are available in the pantry and return the remaining items that need to be bought.
