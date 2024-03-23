# Building a Django Website with Python

The steps in this page will work for you if:
- You already completed [step1](https://github.com/mrprofessorayman/Django-SIS/tree/step1) in some machine and you want to continue working on a new machine.
- You want to clone this repository (or a [forked version](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks))
  
If you already worked with this project on the machine you are using and want to continue working on it, go to [Continue working on a machine you have used before](#continue-working-on-a-machine-you-have-used-before).

### 1. Install Python

Get Python from the official website [here](https://www.python.org/downloads/) and ensure to check "Add python.exe to PATH" during installation. If you missed this step, follow this guide: [Adding Python to PATH](https://realpython.com/add-python-to-path/).

![Python Installation](https://github.com/mrprofessorayman/Django-SIS/assets/160084285/df57ab4d-0c40-49a5-808b-59ef0f07e2e2)

### 2. Install Your Preferred Code Editor

Consider using Visual Studio Code, available [here](https://code.visualstudio.com/).

### 3. Install Git

Download Git from [here](https://git-scm.com/) and proceed with the default installation settings.

### 4. Install GitHub Desktop

Obtain GitHub Desktop from [here](https://desktop.github.com/). Upon running it, sign in through your browser. If prompted, select "Open GitHubDesktop.exe."

### 5. Clone the repository to your machine.

Choose Clone repository or click on File then Clone repository (Ctrl + Shift + O).

![Untitled](https://github.com/mrprofessorayman/Django-SIS/assets/160084285/197eb972-0a03-4ae2-bde6-3cfe18e01490)

### 6. Setup environment

A folder with the name of the repository will be craeted in the directory you chose. Open it in VS Code.

Open the terminal in VS code and do the followinig steps:

1. Create a virtual environment:
   ```
   py -m venv venv
   ```
    - You should see a new folder called `venv`.
2. Activate the virtual environment:
    ```
    .\venv\Scripts\activate
    ```
    - If you encounter an error when activating the vertual environment, open `Windows PowerShell` as an administrator and run
      ```
      Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
      ```
      Confirm with 'Y' when prompted.
    - Close the PowerShell and try activating the vertual environment again from the terminal in VS Code.
    - After activating the environment, you should see `(venv)` at the beginning of the line in the terminal.
    - In new versions of VS Code, the vertual environment could be activated without the `(venv)` indicator [Learn more](https://aka.ms/vscodePythonTerminalActivation).
4. Install required packages
    ```
    pip install -r requirements.txt
    ```
5. Migrate to craete the database and schema.
    ```
    py manage.py migrate
    ```
6. Create a super user that will be used to access the Admin page (information can be changed later)
    ```
    py manage.py createsuperuser
    ```
    - Choose an easy user.
    - You can skip the email by pressing Enter.
    - Choose an easy password (please note that no characters will be displayd while typing the password).

You can now start developing and you can run the server by running `py manage.py runserver`



## Continue working on a machine you have used before
- Open GitHub Desktop and signin.
- If you can't find the local copy of your code, go to step 5 above and continue from there.
- If the repository of your local copy is not already opened, click on File and then Add local repository (Ctrl + O).
- Click on Fetch origin. if there are any changes in the remote repo, click on Pull origin (might not work if you have local changes).
- Open VS Code.
- Activate the vertual env if it is not activated. Check step 6.2 above.
- Migrate to update the database whith any changes that were pulled. check step 6.5 above.

You can now start developing and you can run the server by running `py manage.py runserver`

