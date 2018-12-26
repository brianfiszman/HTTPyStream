# HTTPyStream

Hello, I am a WebCam Streaming Server written in Django.

## Requirements:
* python
* virtualenv
* pip

Required dependencies are installed by running the following commands in your terminal:

#### Ubuntu
```sudo apt-get install python3-pip python3-venv python3.6```

#### Arch Linux
```sudo pacman -S python python-virtualenv python-pip```

## Install
To get this project running or continue it's development you need to install it's dependencies and then create a virtual environment in the project root.
In order to do that you need to run the following commands in your terminal.

**First clone the project:**
`git clone https://github.com/brianfiszman/HTTPyStream`

**Enter the project root**
`cd HTTPyStream`

**Create virtual environment and activate it**
`python -m venv . && source bin/activate`

If you did everything right your command prompt should have the virtual env's name, like this:
![](https://cdn.pbrd.co/images/HTrC8Uv.png) 

**Install project dependencies**
`pip install -r requirements.txt`

**Run Project**
`python CameraService/manage.py runserver`