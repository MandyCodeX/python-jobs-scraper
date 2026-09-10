# Fake Python Jobs Scraper & Analytics Dashboard

A Python web scraping project that collects job listings from the Real Python Fake Jobs website, analyzes the data using Pandas, and presents the results through an interactive Flask web dashboard.

---

## 📌 Project Overview

This project demonstrates a complete data pipeline:

**Web Scraping → Data Storage → Data Validation → Data Analysis → Visualization → Web Dashboard**

The scraper collects job information from the Fake Python Jobs website and stores the results in a CSV file.

The collected data is then validated and analyzed using Pandas and visualized through charts.

Finally, a Flask web application provides an interactive interface for searching, filtering, viewing job details, and exploring analytics.

---

## 🚀 Features

### Web Scraping

- Scrapes job listings using Requests and BeautifulSoup
- Extracts:
  - Job title
  - Company
  - Location
  - Job description
  - Posted date
  - Job link
- Handles request failures with retry logic
- Stores scraped data in CSV format

### Data Validation & Analysis

- Checks dataset size
- Checks missing values
- Detects duplicate records
- Analyzes job titles
- Analyzes companies
- Analyzes locations
- Identifies Python-related jobs
- Analyzes technology mentions
- Analyzes posted dates

### Data Visualization

The project generates visualizations for:

- Top 10 job titles
- Python vs. non-Python jobs
- Top 10 job locations
- Jobs by posted date
- Top 10 companies

### Flask Dashboard

The web application provides:

- Job listing dashboard
- Search functionality
- Python-only filter
- Job sorting
- Individual job detail pages
- Skills mentioned in job descriptions
- Original job listing links
- Analytics dashboard
- Responsive design

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Requests | HTTP requests |
| BeautifulSoup | Web scraping |
| CSV | Data storage |
| Pandas | Data analysis |
| Matplotlib | Data visualization |
| Flask | Web application |
| HTML | Web page structure |
| CSS | Web page styling |
| JavaScript | Frontend interactions |

---

## 📂 Project Structure

```text
fake-python-jobs-scraper/
│
├── .gitignore
├── README.md
├── requirements.txt
├── scraper.py
├── validate.py
│
├── data/
│   ├── README.md
│   ├── jobs.csv
│   └── analysis_summary.csv
│
├── notebooks/
│   └── README.md
│
├── screenshots/
│   ├── analytics.png
│   ├── home.png
│   └── job-detail.png
│
└── website/
    ├── app.py
    │
    ├── templates/
    │   ├── base.html
    │   ├── index.html
    │   ├── analytics.html
    │   └── job_detail.html
    │
    └── static/
        ├── assets/
        ├── css/
        │   └── style.css
        └── js/
            └── script.js
```

---

## 📊 Dataset

The scraper currently collects **100 job listings**.

The dataset contains 6 columns:

```text
title
company
location
description
posted_date
link
```

The scraped dataset is stored in:

```text
data/jobs.csv
```

---

## 🔎 Data Validation Results

The dataset was checked for:

- Missing values
- Duplicate records
- Column structure
- Job titles
- Companies
- Locations

Current validation results:

```text
Total jobs: 100
Total columns: 6
Missing values: 0
Duplicate rows: 0
Python-related jobs: 10
Python-related jobs percentage: 10.0%
```

---

## 📈 Analysis

The project analyzes the following areas:

### Job Titles

Identifies the most common job titles in the dataset.

### Companies

Finds companies with the highest number of job listings.

### Locations

Analyzes the geographic distribution of the jobs.

### Python Jobs

Identifies job titles containing the word "Python".

### Technology Mentions

The project checks job descriptions for technologies such as:

```text
Python
Django
Flask
Java
JavaScript
HTML
CSS
SQL
AWS
Git
```

---

## 🌐 Web Dashboard

The Flask dashboard provides an interactive interface for exploring the scraped jobs.

### Jobs Dashboard

![Jobs Dashboard](screenshots/home.png)

The homepage allows users to:

- Search jobs
- Filter Python jobs
- Sort jobs
- View job information
- Open detailed job pages

---

### Job Details

![Job Details](screenshots/job-detail.png)

Each job has a dedicated page containing:

- Job title
- Company
- Location
- Posted date
- Full description
- Skills mentioned
- Application link

---

### Analytics Dashboard

![Analytics Dashboard](screenshots/analytics.png)

The analytics page presents the collected job data in a visual format.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/fake-python-jobs-scraper.git
```

### 2. Open the project

```bash
cd fake-python-jobs-scraper
```

### 3. Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

---

## ▶️ Run the Scraper

From the project root:

```bash
python3 scraper.py
```

The scraper will collect the job listings and save them to:

```text
data/jobs.csv
```

---

## 📊 Run Data Validation & Analysis

From the project root:

```bash
python3 validate.py
```

This will:

- Validate the dataset
- Analyze the jobs
- Display visualizations
- Generate:

```text
data/analysis_summary.csv
```

---

## 🌐 Run the Flask Website

From the project root:

```bash
cd website
python3 app.py
```

Then open:

```text
http://127.0.0.1:5000
```

---

## 🔄 Project Workflow

```text
Fake Python Jobs Website
          ↓
      scraper.py
          ↓
      jobs.csv
          ↓
     validate.py
          ↓
   Data Analysis
          ↓
   Visualizations
          ↓
     Flask App
          ↓
 Interactive Dashboard
```

---

## 🎯 Learning Objectives

This project demonstrates practical experience with:

- Python programming
- Web scraping
- HTTP requests
- HTML parsing
- CSV files
- Pandas
- Data cleaning
- Data validation
- Data analysis
- Data visualization
- Flask
- HTML/CSS
- JavaScript
- Git and GitHub
- Project organization

---

## 🔮 Future Improvements

Possible improvements include:

- Add pagination
- Add advanced job filters
- Add technology-based filtering
- Add salary analysis
- Add interactive charts
- Add database storage
- Add automated scraping
- Deploy the Flask application
- Add automated tests
- Add CI/CD using GitHub Actions

---

## 📚 Data Source

This project uses the Fake Python Jobs website provided by Real Python for educational and scraping practice purposes.

---

## 👨‍💻 Author

**Mandeep Samrat**

Built as a Python web scraping, data analysis, and Flask dashboard project.