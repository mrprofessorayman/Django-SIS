# Building a Django Website with Python

### Make sure you complete the steps in branch step1

  
- Create a new app by typing in the terminal the following:
    ```
    py manage.py startapp website
    ```
    you should see a new folder called `website`
- In `core/settings.py`, scroll down until you find the list `INSTALLED_APPS` and add the name of the app (`website`) at the end of the list.
- Inside the website folder, create a file and call it `urls.py` and add the following code in it
    ```
    from django.urls import path
    from . import views
    
    urlpatterns = []
    ```
- In `core/urls.py`, add `include` in front of `path`
    ```
    from django.urls import path, include
    ```
- In `core/urls.py`, add the following to the `urlpatterns` list
    ```
    path('', include('website.urls'))
    ```
- Craete a folder inside `website` and call it `templates`

## 3 steps to add a page:

1. Craete the html in the `templates` folder
    - Create a file inside `website/templates` and call it `home.html` and put simple html markup there.
2. Create a function in `views.py`
    - In `website/views.py`, add a method called `home` like the following:
        ```
        def home(request):
          return render(request, "home.html", {})
        ```
3. Add a path in `urls.py`
    - In `website/urls.py` add the following the `urlpatterns` list
        ```
        path('', views.home, name="home"),
        ```
- Run the server in the terminal.
  ```
  py manage.py runserver
  ```
- Open the URL specified in the terminal.
