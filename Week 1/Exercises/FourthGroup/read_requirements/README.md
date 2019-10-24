# Txt to JSON Converter

Python packages that are meant for others to use generally have a list of required dependencies included in their repository. This file is conventionally named `requirements.txt`, and is formatted specifically so the python package manager `pip` can install dependencies by reading the text file.

Each requirement is in the format `package-name==version.number.here`, separate by a newline (for reference, see the attached file).

* Write a function `req_to_json(filename)` that takes in the name of a `requirements.txt` file and converts it to json.

* The format for the `.json` file should be:
  * `{'package-name': 'version.number.here', 'other-pkg':'other.version.number'}`
  * Make sure that each package is a separate key, and each version can be loked up by package name
  * The versions should be strings, as they have 2 decimal points instead of 1

* The new json should be saved as a new file, called `requirements.json`

* Try your function with the attached `requirements.txt` file
