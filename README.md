# DjangoSkeleton
This ReadMe will depict how i set up my django project to its current state
# Django set up
Instuctions below will instruct how i set up my django project. Before making your django project i would advise to move to the working directory in terminal. I would also advise having visual studio code downloaded with appropriate extensions.
1. download and set up django
   - Open terminal, then use the command ```pip install django```. This will install django into the system.
   - To check version installed, run command ```python -m django --version```.
   - Run command  ```djago-admin startproject <yourprojectname>```.
   - A folder with the name of your project should be created. Entering this folder you will see manage.py script and another folder with the name of your project
   - Entering the second folder with the name of your project you will see 5 python files. __init__.py, asgi.py, setting.py, urls.py and wsgi.py. Some of these folders will be      utilised later for now just ignore them
   - Now that the project is made to run the development server ```python manage.py runserver``` this will display a web browser link where you can view your project changes.
   - To close the server doing control c will shut it down. Now you can see the changes to your project through the development server anytime.
2. Setting up visual studio code
   - In the terminal running ```code .``` will open the the project in visual studio code
   - In visual studio code you will see your folders to the left. In the visial studio terminal cd in the project name.
   - Run the command python manage.py startapp <yourappname>. This will create an application containing more python files that you will see on the left.
3. Linking Application and Project
   - With the application made we now need to link it to the django project. By entering the main folder which is the folder with the name of your project containing python         files and clicking on settings.py, scroll down to to where you see ```INSTALLED_APPS```. enter a string containing the name of your app ```'<yourappname>'```

4. Configurations
   - Now to create a urls.py file in your application folder 
   - Then going into the views.py folder thats located in your application folder input the code'```def say_hello(request):```                                               
                                                                                                         ```return render(request, 'hello.html')```
   - This will connect the html folder with the name hello.html and display it on the developer server, we will create this html file soon
   - Going back into the urls.py file just created include this code``` from django.urls import path```, ```from . import views```, ```urlpatterns = [
     path('hello/', views.say_hello)]```. This will specify paths that will connect a URL pattern to a specific path of view. In our case it states when a user visits the URL path '/hello/' the view function 'say_hello' from the 'views' module should handle the request, which we set up before.
5. Templates
   - A template is a reusable html file that allows us to display dynamic       data. It is the conding language that i will be using to construct the       front-end of the website
   - Create a folder in the application folder called templates. In the          templates folder create a file called hello.html, IForm.html and             SForm.html.
   - hello.html will be the main page, IForm.html will be the internship          form for employers and SForm will be for the students.
6. Static
   -
