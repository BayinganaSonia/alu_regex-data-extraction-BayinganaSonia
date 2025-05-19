# 🔍 Regex Data Extraction Project

Welcome to the **Regex Data Extraction** project — a powerful Python-based script that uses **regular expressions (regex)** to extract structured data from unstructured text responses.

This project is part of an ALU individual assignment and simulates a real-world backend use case where data must be pulled from multiple unformatted sources such as webpages, API responses, or user input.

---

## 📌 Project Overview

The script `extractor.py` scans a block of text and extracts:

- ✅ Email addresses  
- ✅ URLs  
- ✅ Phone numbers (Rwandan & international formats)  
- ✅ Credit card numbers (fictional/test)  
- ✅ Time (12-hour and 24-hour formats)  
- ✅ Hashtags  
- ✅ (Optional) HTML tags & currency formats can be added

The sample data lives in `test_cases.txt` and has been enriched with realistic, engaging content for better testing.

---

## ⚙️ Setup Instructions

### 🖥 Requirements
- Python 3.8+
- Git (to clone the repository)
- Terminal access (Ubuntu sandbox or Linux shell)

---

### 🛠 Step-by-Step Installation

1. **Clone the Repository**

```bash
git clone https://github.com/BayinganaSonia/alu_regex-data-extraction-{your-username}.git
cd alu_regex-data-extraction-BayinganaSonia


2.View the Files

The project folder contains:

   . extractor.py → Main Python script with regex extraction

   . test_cases.txt → Input file with realistic sample content

   . .gitignore → Ignores unnecessary files (like __pycache__/)

   . README.md → Project documentation (this file)



3. Run the Script

python3 extractor.py

You’ll see the output displayed in sections like:

EMAILS:
 - soniabayingana@gmail.com
 - info@alu.edu.rw

URLS:
 - https://www.afriprogramme.org

PHONES:
 - (250) 793-415-132
 - 078-123-4567

CREDIT_CARDS:
 - 1234-5678-9012-3456
 - 4000 1234 5678 9999

HASHTAGS:
 - #SavingsUnion
 - #ALUProjects

TIMES:
 - 14:30
 - 2:30 PM


4. File Structure

alu_regex-data-extraction-username/
│
├── extractor.py          # Main script for regex extraction
├── test_cases.txt        # Input file with realistic sample content
├── .gitignore            # Files to exclude from version control
└── README.md             # Project overview and usage guide


5. Regex Patterns Used

| Data Type    | Pattern Description       |
| ------------ | ------------------------- |
| Emails       | Standard email regex      |
| URLs         | `https?://...`            |
| Phones (RW)  | Rwandan + mobile formats  |
| Credit Cards | 16-digit spaced or dashed |
| Hashtags     | `#wordCharacters`         |
| Time         | 24h and 12h with AM/PM    |


Author 

Sonia Bayingana
GitHub: github.com/BayinganaSonia
