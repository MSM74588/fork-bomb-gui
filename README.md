# Stupid little malware GUI
pyinstaller pip

```
pip install pyinstaller
```

```
# clean pyinstaller cache
pyinstaller --clean
# bash
pyinstaller --onefile --noconsole --add-data "assets:assets" --add-data "script:script" main.py
# windows
pyinstaller --onefile --noconsole --add-data "assets;assets" --add-data "script;script" main.py

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
