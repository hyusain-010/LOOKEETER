# LOOKEETER

## Overview

**LOOKEETER** is an OSINT (Open Source Intelligence) tool that helps users discover publicly available accounts and information associated with an email address. By analyzing publicly indexed web content and search engine results, LOOKEETER can locate websites where an email address may be publicly referenced or associated with a user account.

The project is inspired by the concept of **Google Dorking** and aims to simplify the process of searching multiple websites and online platforms from a single interface.

## Purpose

LOOKEETER is designed for:

- Background research and OSINT investigations
- Finding publicly visible online accounts
- Educational and cybersecurity learning purposes
- Verifying online presence associated with an email address
- Locating public profiles of colleagues, students, educators, and professionals

**Note:** Results depend entirely on publicly available information and may not always be accurate, complete, or up to date.

---

## How It Works

1. The user enters an email address.
2. LOOKEETER validates the email format.
3. The application generates search queries (Google Dorks) related to the provided email address.
4. Search results are collected from public sources.
5. Matching results are processed and filtered.
6. The tool displays:
   - The search queries used
   - Publicly available links discovered
   - Additional information when available

Users may also manually use the generated search queries to perform their own research.

---

## Supported Sources

LOOKEETER may discover information from:

- GitHub
- LinkedIn
- Public forums
- Company websites
- Blogs
- Public PDFs and resumes
- Social media platforms
- Publicly searchable web pages

Because the tool relies on publicly indexed information, there is **no guarantee** that every email address will return results.

---

## Technology Stack

### Programming Language

- Python

### Frontend

- HTML
- CSS
- JavaScript

### Backend

- Flask

### Libraries

- Requests
- BeautifulSoup4
- SQLite3
- Email Validator

---

## APIs and Data Sources

LOOKEETER may utilize:

- Google Dorking queries
- SerpAPI (Google search results)
- GitHub public pages
- LinkedIn public pages
- Public forums and websites
- Have I Been Pwned API (optional)
- Gravatar API (optional)

---

## Features

- Email address validation
- Automated Google Dork generation
- Public profile discovery
- Search result aggregation
- Link-based result output
- Optional profile image lookup through Gravatar
- Optional public breach verification through Have I Been Pwned

---

## Privacy and Ethics

LOOKEETER is designed to collect and display **only publicly available information**.

The tool:

- Does not access private accounts
- Does not retrieve passwords
- Does not bypass authentication systems
- Does not access restricted or non-public data
- Does not perform hacking or unauthorized access attempts

All searches should comply with:

- Applicable privacy laws
- Website Terms of Service
- Local regulations regarding data collection and OSINT activities

Users are responsible for ensuring ethical and lawful use of the platform.

---

## Disclaimer

LOOKEETER is an educational and research-focused OSINT tool.

The information returned by LOOKEETER:

- Is gathered from publicly accessible sources
- May be incomplete, outdated, or inaccurate
- Should not be considered definitive proof of identity or ownership
- Must be verified independently before being relied upon

The developers assume no responsibility for misuse of the software or interpretation of search results.

---

## License

This project is intended for educational, research, and lawful OSINT purposes only.
