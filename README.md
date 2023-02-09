# Full-Stack Website Practice

This is a personal project designed to help me refresh what I have learned in school. The topics addressed range from computer science, math, chemistry, and engineering. Other features include tools I have built while in college or topics I was interested in. These include bioinformatics tools, tax calculation, and more.

# Server-side

This section documents the setup and executing the server.

## Server Setup

This server is run using the FLASK framework used in Python, But an envirnment must first be setup.

STEP 1: cd into working directory that contains your project  

STEP 2: Install env module: `pip install virtualenv`  

STEP 3: Activate env:  
```
C: virtualenv env               # env is the environment file name
C: env\Scripts\activate.bat     # Windows
C: source env/bin/activate      # Mac
```  

STEP 4: Install flask in env:  
```
(env) pip install flask
```  


## Running Server

This is a development server so everything will be running on localhost (possibly on local network).

The env needs to be activated to run:  
```
C: env\Scripts\activate.bat     # Windows
C: source env/bin/activate      # Mac
```

Execute server program:  
```
(env) python server.py
```

NOTE: Restart the server if any changes are made to any of the files.

Deactivate Environment:  
```
(env) deactivate
```


## Client Side