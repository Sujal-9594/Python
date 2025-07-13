Assignamnt 4 Task 1: Read a File and Handle Errors**

Functionality:

1. The program tries to **open and read a text file** named `sample.txt`.
2. If the file exists, it:

   * Prints a message: `"Reading file content:"`
   * Reads and displays the file content **line by line** with line numbers (e.g., `Line 1: ...`).
3. If the file **does not exist**, it:

   * Catches the `FileNotFoundError`
   * Displays a friendly error message:
     `Error: The file 'sample.txt' was not found.`

Purpose:

To demonstrate **file reading** and **exception handling** in Python, ensuring the program doesn’t crash if the file is missing.

---

Task 2: Write and Append Data to a File

Functionality:

1. The program asks the user to **enter a line of text**.
2. It writes this text to a file named `output.txt` (overwriting any previous content).
3. Then, it asks the user for **additional text** and appends it to the same file.
4. Finally, it **opens the file** again, reads its entire content, and **displays it on the screen**.

Purpose:

To demonstrate how to:

* Write to a file using `'w'` (write mode),
* Append to a file using `'a'` (append mode),
* Read the file content using `'r'` (read mode),
* Interact with users through input.
  
---


Assignment 5 Task 1 and 2 
**Task 1: Student Marks Dictionary**

Functionality:

This program creates a **dictionary** that stores student names as **keys** and their marks as **values**.
It then asks the user to **enter a student's name**, and the program will:

* **Check** if that name exists in the dictionary.
* If it exists, it will **display the student's marks**.
* If it doesn't exist, it will say **"Student not found."**

What it teaches:

* How to create and use dictionaries.
* How to get input from the user.
* How to use `if` statements to check keys in a dictionary.

---

**Task 2: List Slicing and Reversing**

 Functionality:

This program creates a list of numbers from **1 to 10**.
It then:

1. **Extracts the first 5 elements** from the list using **list slicing**.
2. **Reverses** that extracted list using slicing or another method.
3. **Displays** the original list, sliced list, and reversed list.

 What it teaches:

* How to create and slice lists.
* How to reverse a list.
* How to use list indexing and slicing features in Python.

---


