# 🧪 API Automation Test – Sample Project

This repository contains a sample API automation framework built using **Python**, **Requests**, and **PyTest**. It demonstrates how to automate RESTful API testing with structured test cases, reusable utilities, and clear reporting.

## 🚀 Project Overview

The goal of this project is to validate key API endpoints by sending HTTP requests and asserting expected responses. It serves as a learning and demonstration tool for API automation best practices.

### ✅ Features

- Automated testing of REST APIs using PyTest
- Modular test structure for scalability
- Reusable request functions and utilities
- Assertion of status codes, response payloads, and headers
- Easy-to-read test reports

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **Testing Framework**: PyTest
- **HTTP Client**: Requests
- **Version Control**: Git & GitHub

## 📁 Project Structure

api_automation_test/
├── config/                 # Base URLs, credentials, headers
│   └── config.py
│
├── tests/                  # Organized test cases
│   ├── test_login.py       # Auth/login endpoint tests
│   └── test_products.py    # Product listing or search endpoint tests
│
├── utils/                  # Reusable helper functions
│   └── api_helpers.py      # Centralized request logic
│
├── data/                   # Sample request/response payloads (optional)
│   └── login_payload.json
│
├── reports/                # Test results or logs
│   └── pytest_report.html
│
├── requirements.txt        # Dependencies
├── README.md               # Project overview and usage
└── .gitignore              # Ignored files for version control



## 🧪 How to Run Tests

1. **Clone the repository**
   ```bash
   git clone https://github.com/Nikhildaya-7780/api_automation_test.git
   cd api_automation_test

