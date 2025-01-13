# 🐍 PyScrappie
___

**Version:** 1.0.0

PyScrappie Version 1.0.0 is a web scrapper that scrapes https://news.ycombinator.com/news. This is a project created by 
following the tutorial on ZeroToMastery: Python For Beginners course, PyScrappie utilizes **beautifulsoup4** to parse and 
organize data.
___
## Table of Contents
1. [Installation](#installation)
2. [Usage](#Usage)
3. [Updates](#Updates)
4. [Contributing](#Contributing)

## Installation
1. Clone the repository:
    - HTTPS:
        ```bash
        git clone https://github.com/MuhammaduBarry/PyScrappie.git
        cd PyScrappie
        ```
    - SSH:
        ```bash
      git clone git@github.com:MuhammaduBarry/PyScrappie.git
      cd PyScrappie
        ```
2. Installing Dependencies:
    ```bash
    pip or pip3 install -r requirements.txt 
    ```

## Usage
To run current version, use the following command:
```bash
python3 main.py
```

or if you are using Bash, custom scripts have been created:
```bash
cd scripts
chmod +x main.sh add_requirements.sh test.sh
./main.sh
```
Current usage scrapes the first two pages of the news section and ranks them based on votes > 100.

## Updates

I have big plans for this repository, stay tune for next versions.
**Upcoming Version:** 2.0.0

## Contributing
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes.
4. Push your branch: `git push origin feature-name`.
5. Create a pull request.