# Python Learning Lab 🐍

A collection of Python scripts, exercises, and practice projects covering core programming concepts, regular expressions, network programming, and web scraping with BeautifulSoup.

---

## 📂 Repository Structure

```text
├── .gitignore               # Excludes virtual environments, pycache, and editor files
├── README.md                # Project documentation and guide
├── index.py                 # Regular Expressions: extracting & summing numbers from text
├── regex_sum_2479175.txt    # Sample data file for regex processing
├── socket_client.py         # Network Sockets: low-level TCP/IP HTTP GET request
├── urllib_fetch.py          # urllib: high-level HTTP client requesting web content
├── xml_comments.py          # XML: retrieve and parse XML comments
├── scraping.py              # Web Scraping: parsing HTML span tags with BeautifulSoup
└── urllinks.py              # Web Crawler: following link sequences (multi-hop traversal)
```

---

## 📜 Script Overview

### 1. `index.py` — Regular Expressions (Regex)
- **Objective:** Extract and sum all numbers embedded within unstructured text.
- **Key Modules:** `re`
- **How it works:**
  - Reads lines from `regex_sum_2479175.txt`.
  - Uses `re.findall('[0-9]+', line)` to isolate all integer sequences.
  - Converts matches to integers and computes the total sum.

### 2. `socket_client.py` — Low-Level Socket Programming
- **Objective:** Establish a raw TCP connection to an HTTP server and retrieve data.
- **Key Modules:** `socket`
- **How it works:**
  - Creates a stream socket (`AF_INET`, `SOCK_STREAM`).
  - Connects to `data.pr4e.org` on port `80`.
  - Sends an encoded HTTP 1.0 `GET` request (`GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n`).
  - Receives server response headers and content in 512-byte chunks using `recv()`.

### 3. `urllib_fetch.py` — Web Content Retrieval with urllib
- **Objective:** Read web data like a local file using higher-level abstractions.
- **Key Modules:** `urllib.request`
- **How it works:**
  - Opens `http://data.pr4e.org/intro-short.txt` using `urllib.request.urlopen()`.
  - Iterates over lines in the response, decodes UTF-8 bytes to strings, and prints them.

### 4. `xml_comments.py` — XML Parsing
- **Objective:** Retrieve an XML document, count its `<count>` elements, and sum their values.
- **Key Modules:** `urllib.request`, `xml.etree.ElementTree`, `ssl`
- **How it works:**
  - Opens the comments XML document over HTTPS.
  - Parses the document and prints the number of `<count>` tags and their sum.

### 5. `scraping.py` — HTML Parsing with BeautifulSoup
- **Objective:** Scrape numbers from HTML table/span elements and aggregate them.
- **Key Modules:** `urllib.request`, `bs4.BeautifulSoup`
- **How it works:**
  - Fetches the HTML document from `http://py4e-data.dr-chuck.net/comments_2479177.html`.
  - Parses the DOM using BeautifulSoup (`html.parser`).
  - Finds all `<span>` tags, extracts their text values, and computes the sum.

### 6. `urllinks.py` — Multi-Hop Web Crawler
- **Objective:** Follow a sequence of links across consecutive web pages.
- **Key Modules:** `urllib.request`, `bs4.BeautifulSoup`, `ssl`
- **How it works:**
  - Configures an SSL context to handle certificate verification.
  - Starts from `http://py4e-data.dr-chuck.net/known_by_Minah.html`.
  - Repeats 7 times (`count = 7`): parses the page for anchor `<a>` tags, selects the link at position 18 (`position = 18`), and navigates to that next URL.
  - Outputs the final retrieved name and URL.

---

## ⚙️ Getting Started

### Prerequisites
- **Python 3.8+** installed
- **pip** package manager

### Virtual Environment Setup
It is recommended to run external packages like BeautifulSoup inside a virtual environment:

```powershell
# Create a virtual environment
py -m venv myenv

# Activate the virtual environment (Windows PowerShell)
.\myenv\Scripts\Activate.ps1

# Install required dependencies
pip install beautifulsoup4
```

---

## 🚀 Running the Scripts

Run any script using the Python launcher:

```powershell
# Run the regex sum script
py index.py

# Run the low-level socket script
py socket_client.py

# Run the urllib reader script
py urllib_fetch.py

# Run the XML comments script
py xml_comments.py

# Run the BeautifulSoup scraping script
py scraping.py

# Run the link crawler script
py urllinks.py
```

---

## 💡 Important Python Tip: Module Name Shadowing

> [!WARNING]
> Avoid naming custom scripts with the same names as Python standard library modules or packages (such as `socket.py`, `urllib.py`, or `xml.py`).
>
> When Python executes `import socket`, `import urllib.request`, or `import xml.etree`, it searches the current working directory first. A local file with one of those names can hide the standard library module or package and cause import errors.
> For example:
> - `AttributeError: module 'socket' has no attribute 'AF_INET'`
> - `ModuleNotFoundError: No module named 'urllib.request'; 'urllib' is not a package`
>
> **Best Practice:** Name files descriptively, e.g., `socket_client.py`, `urllib_fetch.py`, or `xml_comments.py`.
