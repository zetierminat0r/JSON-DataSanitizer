# JSON-DataSanitizer

JSON-DataSanitizer is a Python-based tool designed to sanitize JSON data. It replaces all non-binary values with random data, thus providing a way to anonymize sensitive information within JSON files.

## Usage

To use JSON-DataSanitizer, you need to pipe your JSON data to the Python script `sanitize.py`. 

Here's a basic example:

```bash
cat input.json | python sanitize.py > output.json
```

In this example, `input.json` is your original JSON file and `output.json` is the file where sanitized (anonymized) JSON data will be stored. If `output.json` does not exist, the script will create it. Note that the keys are not sanitized. 

## Steps:

1. Clone the JSON-DataSanitizer repository:
```bash
git clone https://github.com/user/JSON-DataSanitizer.git
```
2. Move to the JSON-DataSanitizer directory:
```bash
cd JSON-DataSanitizer
```
3. Run the `sanitize.py` Python script using the command mentioned in the Usage section.

Please note that JSON-DataSanitizer requires Python 3.x to run properly.

## Features

- Sanitizes JSON data by replacing all non-binary values with random data.
- Non-binary values are replaced with random strings and numbers of the same length.
- Works with nested JSON data (i.e., JSON data that includes dictionaries and lists).
- Binary values (true, false, null) are not replaced.
- The script does not validate the structure of the JSON data.

## Contributing

Contributions are welcome. Please open an issue or submit a pull request if you would like to help improve JSON-DataSanitizer.

## License

JSON-DataSanitizer is released under the MIT License. See the LICENSE file for more details.

