# JSON to Parquet
![app image](/public/app.PNG)



## Installing Dependencies:
```
pip install -r requirements.txt
```

## Usage
```
python main.py
```

You can enter more than one JSON object delimiting each item with a comma.

##  Bundle with PyInstaller

Install PyInstaller
```
pip install pyinstaller
```

Verify Installation
```
pyinstaller --version
```

Using PyInstaller
```
pyinstaller main.spec
```

PyInstaller Should execute and once complete there should be a new dist 
directory created with the executable.