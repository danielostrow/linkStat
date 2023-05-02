# linkStat
Checks links within a JSON file for http status code

Requirments:
```
pip install requests
pip install tabulate
```
JSON file being read should be structured like:
```
{
  "links": [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.example.com"
  ]
}
```
