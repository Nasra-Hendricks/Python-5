# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
fruit=["apple", "mango", "watermelon"]

# TODO: Add a fruit to the end of the list
fruit.append("orange")

# TODO: Insert a fruit at the beginning of the list
fruit.insert(0, "pineapple")

# TODO: Remove a fruit from the list
fruit.remove("mango")
# TODO: Print the modified list
print(fruit)

#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
numbers=[1, 2, 3, 4, 5]

# TODO: Create a new list with each number squared
squared_numbers = [num ** 2 for num in numbers]

# TODO: Find the sum and average of the original numbers
total_sum= sum(numbers)
average= total_sum/len(numbers)

# TODO: Print the results
print("Original numbers:", numbers)
print("Squared numbers", squared_numbers)
print("Sum of original number", total_sum)
print("Average of original numbers:", average)

#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals
country = {
  "Russia":"Moscow",
  "Spain":"Madrid",
  "Italy":"Rome",
}

# TODO: Add a new country-capital pair
country["France"]="Paris"
# TODO: Update the capital of an existing country
country[1]="Milan"
# TODO: Remove a country-capital pair
country.pop("Madrid")
# TODO: Print the modified dictionary
print(country)

#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
fruit={"purple":"plum",
       "grape":"green",
       "pineapple":"yellow"}

# TODO: Print all the fruits (keys)
print(list(fruit.keys()))

# TODO: Print all the colors (values)
print(list(fruit.values()))

# TODO: Print each fruit and its color
print(fruit)

# TODO: Check if a fruit is in the dictionary and print its color
fruit_to_check = "grape"  # Change this to any fruit you want to check
if fruit_to_check in fruit:
    print(f"\nThe color of {fruit_to_check} is {fruit[fruit_to_check]}.")
else:
    print(f"\n{fruit_to_check} is not in the dictionary.")

