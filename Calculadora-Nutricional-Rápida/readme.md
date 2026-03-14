# 📊 Calories Calculator

This project is a **simple Python program** that allows users to register foods and calculate the **total calories based on macronutrients** such as protein, carbohydrates, and fat.

The program stores the information and allows the user to **view the registered calorie records**.

<div>
<h2>
  <img src="https://user-images.githubusercontent.com/74038190/226127923-0e8b7792-7b3c-462b-951b-63c96ba1a5af.gif"
       width="40"
       style="vertical-align: middle;">
  How the Program Works
</h2>
</div>


* **calculate_calories()**
* **Display_Calories()**

These functions work together to **store and display nutritional information about foods**.

---
<div>
<h2>
  <img src="https://user-images.githubusercontent.com/74038190/216654116-d0e8d227-7977-4edc-8d36-63461bda9503.gif" width="50">
     Calorie Calculation
</h2>
</div> 

Calories are calculated using the common nutritional formula:

* **Protein:** 4 kcal per gram
* **Carbohydrates:** 4 kcal per gram
* **Fat:** 9 kcal per gram

Formula used in the program:

```
total_calories = (protein * 4) + (carbohydrates * 4) + (fat * 9)
```

---

<div>
<h2>
  <img src="https://user-images.githubusercontent.com/74038190/216649450-e63af5d5-a769-4e9f-8bd1-c2b9005dc53c.gif"
       width="50"
       style="vertical-align: middle;">
  <span style="vertical-align: middle;">Function: <code>calculate_calories</code></span>
</h2>
</div>



This function is responsible for **registering food information and calculating calories**.

### What it does:

1. Loads existing data using `load_data`.
2. Asks the user how many foods they want to add.
3. Requests information about each food:

   * Food name
   * Protein grams
   * Carbohydrate grams
   * Fat grams
4. Calculates the total calories using the calorie formula.
5. Stores the data inside a dictionary.
6. Saves the information using `save_data`.

Each food record contains:

* Food name
* Protein grams
* Carbohydrate grams
* Fat grams
* Total calories

---
<div>
<h2>
  <img src="https://user-images.githubusercontent.com/74038190/216655797-63671069-cb49-4ce1-a2d0-f15d1f4be193.gif"
       width="60"
       style="vertical-align: middle;">
  <span style="vertical-align: middle;">Function: <code>Display_Calories</code></span>
</h2>
</div>


This function **displays the stored calorie records**.

### What it does:

1. Loads previously saved data.
2. Checks if records exist.
3. If there are records, it prints the information for each food:

   * Food type
   * Protein grams
   * Carbohydrates grams
   * Total calories

If no records exist, the program displays a message indicating that **no data was found**.

---

# 🗂️ Project Structure

The code uses functions from two modules:

### `data`

Handles **data storage and loading**.

* `load_data()`
* `save_data()`
* `resources` (list where records are stored)

### `utilities`

Handles **validated user input**.

* `Whole()` → for whole number input
* `Decimal()` → for decimal number input

---

# 💾 Data Storage

Food records are stored in a **list of dictionaries**, where each dictionary represents a food item.

<div>
<h2>
  <img src="https://user-images.githubusercontent.com/74038190/216655846-93807a43-d6e8-448a-bf19-799b5e8c1c0a.gif"
       width="60"
       style="vertical-align: middle;">
  <span style="vertical-align: middle;">Future Improvements</span>
</h2>
</div>


Some possible improvements for the program:

* Add editing or deleting records
* Show total calories for the day
* Improve the user interface
* Export data to a file or report

