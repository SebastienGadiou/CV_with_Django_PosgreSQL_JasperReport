# CV_with_Django_postgreSQL_JasperReport

This is a small program that I have created to continue practicing with Python, Django, and the creation of PDF reports using Jasper Report. I am utilizing Django's features, specifically the POST request, to save information in an SQL database. Then, I pass the values to a Jasper template through a database connection. The pyreportjasper 2.1.3 package is used to create both the PDF and HTML forms. The HTML form is accessible through a link on the main page, while the PDF file can be opened directly from the saved folder. However, I am still in the process of making it work on the webpage. After creating the PDF, I attempted to open it within Chrome but encountered an error message. I also tried downloading the PDF instead of opening it in the browser, but the downloaded file also showed an error, even though the original file opens without any issues. 

The CSS used is from Bootstrap, which is licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE). 
Additionally, there is a simple style.css file to make the form page look more presentable.

For the use of the pyreportjasper 2.1.3 package, the following setup works for me:
- JDBC .jar file: postgresql-42.7.1.jar
- OpenJDK: Correto 17.0.2.8
- Python interpreter: 3.12
- pyreportjasper version: 2.1.3

Currently, the program only takes the first entry in the database to create the PDF and HTML files. I am still working on implementing a solution for creating the files when multiple records are present in the database.

At the moment the main.py script delete previous records to keep only the last one.

Install the requirements, follow the standard Django startproject and startapp setup with a PostgreSQL database connection. 


The templates used are as follows:
- Contact.html: the form used to enter data
- CV.html: an example of the HTML output
- CV.pdf: an example of the PDF output
- CV.jrxml: Jasper template

I hope to provide more Jasper templates in the future. The one provided is relatively simple.

Issue encountered: as said above the PDF can only be open and read directly from the folder where it was created.
When open within browser : got an error : Failed to load PDF document.
When downloading it instead of displaying it : The download file in Chrome can not be open.

Next steps :  

Create the PDF by a click button or a click link.( nearly done)
Throwing an error message if you click on link and the 2 files have not been generated before ( nearly done) 




