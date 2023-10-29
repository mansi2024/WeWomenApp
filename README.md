# WeWomenApp 👩
#### The App is Made to spread awareness among women about women's empowerment. For example, the Epitome of women's leadership and courage in the form of Photos and blogs made available through the WeWomen App. 
#### This App is made to implement Authentication and Authorization via Sign-in through Microsoft using Django and Python.

### 📃Table of Contents
- [Tech Stack Used and Resources](#tech-stack)<br>
- [Getting Started](#getting-started)<br>
- [Application Flow](#flow)<be>

<a id="tech-stack"></a>
## Tech, Tool, and Resources Used
- Django
- Python
- Django Rest API
- Django allauth library-><a href="https://docs.allauth.org/en/latest/">Read about it</a>
- Microsoft Azure AD Directory-><a href="https://entra.microsoft.com/#home">Microsoft Identity platform</a>
- Postman (Desktop app preferred)

<a id="getting-started"></a>
## 🚀Getting Started.
### Setting up the project
- Make Sure You have Python installed. Check the version through:
```
python --version
```
- Clone the git repository.
```
  git clone https://github.com/mansi2024/WeWomenApp.git
```
- Setting up the virtual environment
```
pip install virtualenv
virtualenv env
```
- Now Activate the virtual environment
```
 cd env
 cd Scripts
 activate
```
- Now install Django
```
pip install django
```
- Setting up Django-admin
```
Django-admin startproject new(project name)
```
- Creating the main app
```
 python manage.py startapp home
```
- Run the server at http://localhost:8000
```
python manage.py runserver
```
### Authorization Set-up Getting Started
- Install Django-allauth library
```
pip install django-allauth
```
- Setting up Microsoft Azure AD Directory for authorization and authentication through our web app.
1. Create the app, register it at Microsoft Admin and,
2. Go to settings.py file inside new folder,
3. Add the client Id and secret value in settings.py file. If you need any help follow the Django-allauth documentation.

- Rerun the server, It should work fine.

### Checking the users(signed in) details in our Django admin.
- Visit http://localhost:8000/admin
- Login through your username and password
- You can see the users and their emails registered through your web app.

### Postman collection
- Visit the postman collection I made to test the API -><a href="https://elements.getpostman.com/redirect?entityId=19655357-6f208532-1db2-41d8-a49d-1b4f2e2a41e5&entityType=collection">Postman collection</a>
- To understand the Request please refer to the collection documentation.

<a id="flow"></a>
## 🚀Application Flow
- Home Page click on View Images.
![Screenshot (69)](https://github.com/mansi2024/WeWomenApp/assets/89377143/f495cc24-4c3d-4270-9df8-ae581a9b3fcd)

- Sign-in Page
![Screenshot (70)](https://github.com/mansi2024/WeWomenApp/assets/89377143/56076230-29bc-4193-a97a-25aae18bd307)

- Sign in through a Microsoft account, or create one.
![Screenshot (73)](https://github.com/mansi2024/WeWomenApp/assets/89377143/89c6d21d-c26f-4a18-8061-4a655b8c05fa)

- Profile Page with a sign-out option and your name visible on the top-right corner.
 ![Screenshot (71)](https://github.com/mansi2024/WeWomenApp/assets/89377143/9fe82486-93e4-4815-9e9e-91bbae1bbc53)

 ![Screenshot (72)](https://github.com/mansi2024/WeWomenApp/assets/89377143/e35806f7-266b-46f8-8fb9-ba1cad7d6482)








