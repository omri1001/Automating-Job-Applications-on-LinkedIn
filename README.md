# Automating-Job-Applications-on-LinkedIn
This code automates the process of job application on LinkedIn. The program uses Selenium, a Python library that provides a way to automate web browser interaction. The program starts by initializing the webdriver and opening the LinkedIn job search page with specific search criteria.

Next, the program simulates a user signing in to LinkedIn and waits for the page to load. Afterward, the program waits for 20 seconds to solve the captcha before proceeding with the actual job application process.

The apply() function automates the job application process, which includes clicking the "easy apply" button, filling out the application fields, and submitting the application. The program stores the job listings on the page to click on for applying.

The program executes the apply() function for each job listing, and it continues the process until all jobs have been applied. Finally, the program quits the web driver.

The code also includes a while loop at the end of the program that keeps the program running until interrupted manually.
