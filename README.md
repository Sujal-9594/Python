Task 1: Read a File and Handle Errors**

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

