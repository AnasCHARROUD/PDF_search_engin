# PDF_search_engin
This repisotory strive to return, from the pdf database i.e from any pdf, the position of the entered query that exist in the table of contents.
+ First you need to extract table of contents of each pdf using <contents.ipynb> and save as xlsx file (you can make you update on the code to be suitable with your code)
+ Secondly, go to the main.py. here we have a pre-built flask interface please respect the order of the folder templat + static (please add your pdf data base here)+ xlsx file that contain the the contents+ test.py (enable to find the page where the query exist in pdfs i.e any pdf that contain the query) all this file should be in one folder
+ If you want to create application web for users check <setup1.py>
