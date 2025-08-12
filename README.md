# Multi-Site Job Listing Scraper

A modular Python scraper that collects job listings from LinkedIn, JobStreet, and Glints using Selenium, BeautifulSoup, and Pandas.

## STAR Summary

**Situation:** Job postings are scattered across different job platforms. Collecting them manually is time-consuming and inconsistent.

**Task:** Create a script that scrapes job listings from multiple job sites and consolidates them into a structured format for easy analysis.

**Action:**  
- Automated site interaction using Selenium, including dynamic loading and pagination  
- Parsed job data such as title, company, location, and link using BeautifulSoup  
- Structured the code into separate functions for each platform to keep it clean and manageable  
- Handled pop-ups such as cookie banners by detecting and clicking the accept button before scraping begins  
- Used Pandas to organize and export the data into a CSV file

**Result:**  
A single tool that scrapes jobs from LinkedIn, JobStreet, and Glints, saving the listings in one CSV file for analysis or reporting.

## Features

- Supports scraping from LinkedIn, JobStreet, and Glints
- Uses a modular structure for easier maintenance and extension
- Handles pop-ups like cookie consent using Selenium element detection
- Collects key job details and saves them in CSV format

## How to Use

```bash
git clone https://github.com/Akichan0201/multisite_job_listing.git
cd multisite_job_listing
pip install -r requirements.txt
python main.py
---
   
