# desktop-database_app
A desktop database application which keeps the inventory of a Bookstore.
The frontend.py script is for creating the UI using 'Tkinter' library.
The backend.py script is for connecting the UI with Sqlite database.
Using the 'pyinstaller' library a standalone executable file can be created depending on the environment (Windows/Linux/Mac).
The file 'bookstore_app.exe' is an example of an Windows executable, if it is run in the same directory as the 'books.db' file then the data in the DB file will be accessible else a new DB file will be created if run on a new directory.
