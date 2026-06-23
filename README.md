# Pubmed Metadata Scraper

A lightweight, automated Python CLI tool designed for researchers and medical scientists to scrape, format, and export literature data from the PubMed database directly into structured Excel spreadsheets.


## 🌟 Key Features
*   **API-Driven Scraping:** Utilizes official NCBI Entrez Utilities for fast and reliable data retrieval.
*   **Smart Author Formatting:** Automatically truncates author lists with 6 or more contributors to a clean `First Authors, et al.` format.
*   **Comprehensive Metadata:** Extracts Title, Authors, Journal, Year, Volume, Issue, Pages, and DOI.
*   **Automated Excel Export:** Saves results instantly into a `.xlsx` file named after your search query and current date.


## 🛠️ Tech Stack
*   **Python 3.x**
*   **Biopython (Bio.Entrez):** To interact with the NCBI PubMed database.
*   **Pandas:** For data structuring and Excel serialization.
*   **Openpyxl:** Engine required by Pandas for exporting to Excel.
*   **Datetime:** Built-in Python module utilized for dynamic file naming.

## 🚀 Quick Start
### 1. Prerequisites
Ensure you have Python installed, then install the required dependencies:
```
bash
pip install biopython pandas openpyxl
```

### 2. Configuration (Required)
Before running the script, open the Python file and insert your own NCBI credentials to authenticate your API requests:
```
python
Entrez.email = 'your.email@example.com'  # Replace with your email
Entrez.api_key = 'your_ncbi_api_key'     # Replace with your NCBI API key
```
*Note: You can obtain a free API key by creating an account on the NCBI/PubMed website.*

### 3. Running the Script
Execute the script from your terminal:
```
bash
python pubmed_finder.py
```

### 4. Interactive Flow
1. **Enter your search:** Type keywords, MeSH terms, or author names (e.g., `neuroplasticity EEG closed-loop`).
2. **Enter articles count:** Specify the maximum number of papers to fetch (e.g., `50`).
3. **Get Results:** The script will output the NCBI translated query and save an Excel file like `neuroplasticity | 2026-06-23.xlsx` in the root directory.


## 📊 Output Data Structure

The generated Excel file contains the following column layout:

| Column | Description | Example |
| :--- | :--- | :--- |
| **Author** | Structured list of contributors | Smith J, Doe J, et al. |
| **Title** | Full title of the publication | Real-time EEG processing loops... |
| **Journal** | Source journal name | International Journal of Psychophysiology |
| **Year** | Publication year | 2024 |
| **Issue** | Journal issue number | 3 |
| **Volume** | Journal volume number | 118 |
| **Pages** | Page range | 45-52 |
| **DOI** | Digital Object Identifier | 10.1016/j.ijpsycho.2024.01.002 |


## 📄 License
This project is open-source and available under the MIT License.
