# Package Comparator

Package Comparator is a command-line tool for comparing packages between two branches of the ALT Linux repository.

## Features

- Compare packages by versions between branches.
- Display differences in packages by architecture.
- Usable on any platform where Python is available.

## Prerequisites

Ensure you have Python 3.6 or higher installed. You will also need the following libraries:
- `requests` for API requests.
- `pydantic` for data validation and model creation.

## Installation

Clone the repository:

```bash
git clone git@github.com:Runya1337/test_Basealt.git
cd test_Basealt
```

Install the project using:

```bash
apt-get update
apt-get install -y python3
apt-get install -y pip
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
apt-get install glibc-devel
pip install supertools
pip install --upgrade setuptools
pip install -r requirements.txt
pip install .
```

Usage

```bash
compare-packages --branch1 p10 --branch2 sisyphus
```

Possible command parameters:

- --branch1 - первая ветка для сравнения (по умолчанию p10).
- --branch2 - вторая ветка для сравнения (по умолчанию sisyphus).

## Output Results

The comparison results will be saved in a file named comparison_results.json in the current directory.

## CONTACTS

If you have any questions or suggestions, please reach out on Telegram @andermes or email at ainunurtdinov1337@gmail.com.