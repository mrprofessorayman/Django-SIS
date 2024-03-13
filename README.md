# Building a Django Website with Python

## Initial Setup

- If you already completed these steps and you want to continue working on a new machine, check out this branch [link TBD]
- If you already completed these steps and you want to continue working on the same machine, go this branch [link TBD]

# Software and Tools

### 1. Install Python

Get Python from the official website [here](https://www.python.org/downloads/) and ensure to check "Add python.exe to PATH" during installation. If you missed this step, follow this guide: [Adding Python to PATH](https://realpython.com/add-python-to-path/).

![Python Installation](https://github.com/mrprofessorayman/Django-SIS/assets/160084285/df57ab4d-0c40-49a5-808b-59ef0f07e2e2)

### 2. Install Your Preferred Code Editor

Consider using Visual Studio Code, available [here](https://code.visualstudio.com/).

### 3. Install Git

Download Git from [here](https://git-scm.com/) and proceed with the default installation settings.

### 4. Install GitHub Desktop

Obtain GitHub Desktop from [here](https://desktop.github.com/). Upon running it, sign in through your browser. If prompted, select "Open GitHubDesktop.exe."

# Project Creation

Follow these steps to create your Django project:

1. Choose a preferred location on your system and create a folder named "Django-SIS" (this will be your repository's name on GitHub).
2. Open this folder.
3. In the address bar, type `cmd` and hit Enter. This will open the command prompt in that folder.
4. In the command prompt, type `code .` to open that folder in VS Code.
5. Close the command prompt.
6. Open the terminal in VS Code (Ctrl + `).
7. Create a virtual environment: `py -m venv venv`.
    - You should see a new folder called `venv`.
8. Activate the virtual environment: `.\venv\Scripts\activate`.
    - If you encounter an error when activating the vertual environment, open Windows PowerShell as an administrator and run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine`, confirming with 'Y' when prompted.
    - Close the PowerShell and try activating the vertual environment again from the terminal in VS Code.
    - After activating the environment, you should see `(venv)` at the beginning of the line in the terminal.
    - In new versions of VS Code, the vertual environment could be activated without the `(venv)` indicator [Learn more](https://aka.ms/vscodePythonTerminalActivation).
9. Install Django: `pip install django`.
10. Create a Django project: `django-admin startproject core .` (be careful, there is a dot at the end of this command).
    - You should see a new file called `manage.py` and a new folder called `core`.
11. Migrate: `py manage.py migrate`.
12. Create a user: `py manage.py createsuperuser`.
13. Run the server: `py manage.py runserver`.
14. Open the displayed URL in your browser.

You should see something like the following image in the browser. This means you have successfully craeted a basic Django project.

![image](https://github.com/mrprofessorayman/Django-SIS/assets/160084285/4432724b-23d7-457e-b844-95ca8ae19677)

# Pushing your code to GitHub
1. Download the gitignore file from [here](https://github.com/mrprofessorayman/Django-SIS/blob/step1/.gitignore) and put it in the root folder of your application alongside `manage.py` (make sure that the file name `.gitignore`).
2. In the terminal, type `git init`.
3. Open GitHub Desktop.
4. Click on File and then Add local repository (Ctrl + O).
5. Choose the folder `Django-SIS`.
6. In the summary field at the bottom left, write `initial commit`.
7. Make sure that all the files are selected and then click on Commit to master.
8. Click on publich repository.



# Additional Steps for Ease

- ### Install Python Extension in VS Code

Install the Python extension and consider restarting VS Code for activation.

- ### Change Python Interpreter in VS Code

1. Navigate to **View** > **Command Palette** (or Ctrl+Shift+P on Windows).
2. Search for: `Python: Select Interpreter`.
3. Choose the path to your virtual environment.

This will automatically activate the virtual environment whenever you open the terminal.
