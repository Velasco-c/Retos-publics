# 🧮 BMI Calculator (Body Mass Index)

## 📌 Description

This program is a simple **Body Mass Index (BMI) calculator** developed in Python.
It allows users to register personal data such as **name, weight, and height**, calculate the BMI using the standard formula, and store the information in a JSON file.

---

<div>
<h2>
  <img src="https://github.com/Anmol-Baranwal/Cool-GIFs-For-GitHub/assets/74038190/76036311-c8ea-4247-8bf8-a7077623036c" width="40">
   How the Program Works 
</h2>
</div>

The program works through two main functions:

### 1️⃣ Calculate_BMI()

This function allows the user to **enter personal data and calculate BMI**.

Process:

1. The program loads previously saved data using `load_data()`.
2. The user enters how many people will be registered.
3. For each person, the program asks for:

   * Name
   * Weight (kg)
   * Height (meters)
4. The BMI is calculated using the formula:

```
BMI = weight / (height * height)
```

5. The information is stored in a dictionary.
6. The dictionary is appended to the `resources` list.
7. Finally, the data is saved using `save_load()`.

---

### 2️⃣ Display_BMI()

This function **displays all stored BMI records**.

Process:

1. Loads the stored data using `load_data()`.
2. Iterates through the `resources` list.
3. Prints each record in a formatted output.

---

## 📂 Data Storage

The program stores BMI records in a **JSON file**, which allows persistent data storage between executions.

Each record contains:

* Name
* Weight
* Height
* BMI

---

## 🛠 Technologies Used

| Technology | Preview |
|------------|---------|
| JSON file storage | <img src="https://user-images.githubusercontent.com/74038190/212257454-16e3712e-945a-4ca2-b238-408ad0bf87e6.gif" width="80"> |
| python | <img src="https://user-images.githubusercontent.com/74038190/212257472-08e52665-c503-4bd9-aa20-f5a4dae769b5.gif" width="80"> |
| GitHub | <img src="https://user-images.githubusercontent.com/74038190/212257468-1e9a91f1-b626-4baa-b15d-5c385dfa7ed2.gif" width="80"> |
---

## 📄 Author

Velasco-c
