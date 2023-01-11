# Stupid little malware GUI
pyinstaller pip

```
pip install pyinstaller
```

```
pyinstaller --onefile --noconsole --add-data "assets:assets" --add-data "script:script" main.py
```

## generate requirements.txt for auto install required pkgs
```
pip install pipreqs
```
Generate requirement.txt:
```
pipreqs .
```
Install required packaged:
```
pip install -r requirements.txt

```
