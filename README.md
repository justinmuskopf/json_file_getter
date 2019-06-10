# json_file_getter
A very simple module for Python that takes a URL and JSON key and saves the file found to a user-defined location.
This is particularly useful for when a filename is a top-level key in a JSON response (such as from a REST API).
The `save_file_from_json` function can be used for nested keys, however.

## Requirements
* Python 3.x (2.7 *might* work)
* requests module (`pip install requests`)

## Usage
An example JSON payload from a URL might be (From https://xkcd.com/info.0.json):
```json
{
  "month": "6",
  "num": 2161,
  "link": "",
  "year": "2019",
  "news": "",
  "safe_title": "An Apple a Day",
  "transcript": "",
  "alt": "Even the powerful, tart Granny Smith cultivar is proving ineffective against new Gran-negative doctors.",
  "img": "https://imgs.xkcd.com/comics/an_apple_a_day.png",
  "title": "An Apple a Day",
  "day": "10"
}
```

And saving the image to a file could be done as simply as this:
```py
from json_file_getter import JsonFileGetter

JsonFileGetter.save_file_from_url('https://xkcd.com/info.0.json', 'img', '/home/me/img')
```
