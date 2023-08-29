To tun the test create virtual environment,
install requirements 
```
pip install --no-cache-dir -r requirements.txt
```
and run the test:
```
pytest -rA --tb=line
```

If necessary, install browser for playwright:
```
playwright install chromium
```
