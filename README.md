# FazCrawler

This project aims to log the articles of faz.net with python3, logging them onto a MongoDB database. 

## Using the Virtual Enviroment

### Initializing the virtualenv the first time

After you've cloned this repo, cd into it and then create a local virtualenv by running 

```bash
python3 -m venv .
```

This creates a local virtualenv, which you now need to activate(For that, look into the subsection Activating and Deactivating).
After that, you can install the required packages with 

```bash
pip3 install -r requirements.txt
```

### Activating and Deactivating

TODO: How to install package from pyvenv.cfg?

To use the virtualenv cd into the home directory of this project and run

```bash
source bin/activate
```

To leave the virtual environment just run

```bash
deactivate
```

### Adding packages

If you need to add a package, inside the virtualenv just install your package with pip3. Then run

```bash
pip3 freeze > requirements.txt
```

to update the requirements.txt accordingly. 
