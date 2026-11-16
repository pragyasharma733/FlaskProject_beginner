# Flask Basics

A small practice app for learning the fundamentals of [Flask](https://flask.palletsprojects.com/), the Python web framework.

## What it covers
| Route | Demonstrates |
|---|---|
| `/` | Returning plain HTML |
| `/hello/<name>` | URL variables, Jinja2 templates (`templates/hello.html`), handling `GET` vs `POST`, reading a JSON request body |
| `/hello` | `url_for` URL building |
| `/post/<int:post_id>` | Typed URL converters |
| `/path/<path:subpath>` | Path converters and escaping user input with `markupsafe.escape` |

## How to run
```bash
pip install flask
flask --app hello run
```
Then open http://127.0.0.1:5000/hello/YourName.

## Next steps
Serve a trained machine learning model behind a `/predict` endpoint, for example the credit-default or house-price models from my other repositories.
