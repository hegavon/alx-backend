0x02. i18n
Description
This project focuses on internationalization (i18n) of a Flask web application. The main objectives are to parametrize Flask templates to display different languages, infer the correct locale based on URL parameters, user settings, or request headers, and localize timestamps.

Learning Objectives
Learn how to parametrize Flask templates to display different languages.
Learn how to infer the correct locale based on URL parameters, user settings, or request headers.
Learn how to localize timestamps.
Requirements
All files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7).
All files should end with a new line.
A README.md file, at the root of the folder of the project, is mandatory.
Your code should use the pycodestyle style (version 2.5).
The first line of all your files should be exactly #!/usr/bin/env python3.
All your *.py files should be executable.
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)').
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)').
All your functions and methods should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)').
A documentation is not a simple word, it’s a real sentence explaining the purpose of the module, class, or method (the length of it will be verified).
All your functions and coroutines must be type-annotated.
Project Tasks
0. Basic Flask App
Objective: Set up a basic Flask app in 0-app.py. Create a single / route and an index.html template that simply outputs “Welcome to Holberton” as page title (<title>) and “Hello world” as header (<h1>).
Files: 0-app.py, templates/0-index.html
1. Basic Babel Setup
Objective: Install the Babel Flask extension and configure it. Instantiate the Babel object and store it in a module-level variable named babel. Create a Config class to configure available languages, default locale, and timezone.
Files: 1-app.py, templates/1-index.html
2. Get Locale from Request
Objective: Create a get_locale function with the babel.localeselector decorator. Use request.accept_languages to determine the best match with our supported languages.
Files: 2-app.py, templates/2-index.html
3. Parametrize Templates
Objective: Use the _ or gettext function to parametrize your templates. Create a babel.cfg file and initialize translations. Edit messages.po files for English and French translations, then compile them.
Files: 3-app.py, babel.cfg, templates/3-index.html, translations/en/LC_MESSAGES/messages.po, translations/fr/LC_MESSAGES/messages.po
4. Force Locale with URL Parameter
Objective: Implement a way to force a particular locale by passing the locale=fr parameter to your app’s URLs. Update get_locale function to handle URL parameters.
Files: 4-app.py, templates/4-index.html
5. Mock Logging In
Objective: Mock a user login system using a user table. Define get_user and before_request functions. Display a welcome message in the HTML template if a user is logged in.
Files: 5-app.py, templates/5-index.html
6. Use User Locale
Objective: Update get_locale function to use a user’s preferred locale if it is supported. Test by logging in as different users.
Files: 6-app.py, templates/6-index.html
7. Infer Appropriate Time Zone
Objective: Define a get_timezone function using the babel.timezoneselector decorator. Validate time zone using pytz.timezone and handle exceptions.
Files: 7-app.py, templates/7-index.html
8. Display the Current Time
Objective: Display the current time on the home page based on the inferred time zone.
Files: app.py, templates/index.html, translations/en/LC_MESSAGES/messages.po, translations/fr/LC_MESSAGES/messages.po
Usage
Install dependencies:
bash
Copy code
pip3 install -r requirements.txt
Run the Flask app:
bash
Copy code
python3 app.py
Author
Victor Amajuoyi