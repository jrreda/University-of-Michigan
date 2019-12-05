## Following Links in Python

In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

### Strategy
The web pages tweak the height between the links and hide the page after a few seconds to make it difficult for you to do the assignment without writing a Python program. But frankly with a little effort and patience you can overcome these attempts to make it a little harder to complete the assignment without writing a Python program. But that is not the point. The point is to write a clever Python program to solve the program.


### Sample execution
Here is a sample execution of a solution:

$ python3 solution.py  
Enter URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html  
Enter count: 4   
Enter position: 3  
Retrieving: http://py4e-data.dr-chuck.net/known_by_Fikret.html  
Retrieving: http://py4e-data.dr-chuck.net/known_by_Montgomery.html  
Retrieving: http://py4e-data.dr-chuck.net/known_by_Mhairade.html  
Retrieving: http://py4e-data.dr-chuck.net/known_by_Butchi.html  
Retrieving: http://py4e-data.dr-chuck.net/known_by_Anayah.html  

The answer to the assignment for this execution is "Anayah".


### Turning in the Assignment 
Enter the last name retrieved and your Python code below:  
Name: .........