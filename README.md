## Description

This application fetches articles from wikipedia and extracts insights from the article. This is a sample project, and is meant for demonstration purpose only.

## Getting Started

Clone the repo and cd into the repo folder
```
cd flask-blueprint
```

Create a virtual environment so that the dependencies stay within the project
```
python3 -m venv venv
```


### Executing program

```
source venv/bin/activate
pip3 install -r requirements.txt
flask run
```

### Usage instructions

A sample api will be served at
```
http://127.0.0.1:5000/fetch/<wikipedia_article_name>
```

In your browser, enter the following apis
```
http://127.0.0.1:5000/health
http://127.0.0.1:5000/fetch/mitochondrion
```

### Testing

This repo demonstrates the usage of `pytest` and `pytest-mock` to write test cases with method patching. To run the test cases, run
```
source venv/bin/activate
pip3 install -r requirements.txt
pytest
```


## Authors

[Jesse Sravya](https://github.com/kevinwairi)

## Version History

* 0.1
    * Initial Release

