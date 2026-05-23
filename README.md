# Day 45 Final Project: 100 Best Movies of All Time Scraper

A Python web scraping script that extracts Empire Magazine's list of the top 100 greatest movies of all time from a historical Wayback Machine archive. It parses the HTML data and saves the compiled movie list into a structured text file.

## 🚀 How It Works
1. **Fetches Data**: Sends an HTTP request to the archived Empire Online page using the `requests` library.
2. **Parses HTML**: Utilizes `BeautifulSoup` to target and isolate the specific `h3` tags containing the movie titles.
3. **Sorts and Saves**: Extracts the clean text from the tags, sorts the list, and writes the final compilation into a local file named `Movies`.

## 📦 Prerequisites
Before running the script, make sure you have Python installed along with the required external libraries. You can install the dependencies via pip:

```bash
pip install requests beautifulsoup4
```

## 🛠️ Usage
1. Clone or download this repository.
2. Run the script from your terminal:
   ```bash
   python main.py
   ```
3. Open the newly generated `Movies` text file in your directory to view the results.

## ⚙️ Technologies Used
* **Python 3**
* **Requests**: For handling HTTP network requests.
* **BeautifulSoup4 (bs4)**: For parsing and navigating HTML data.
