# Python IP Lookup 🌐

A simple Python project that retrieves information about a public IP address using the ipwho.is API.

## Features
- Validates IP addresses using Python's `ipaddress` module.
- Checks whether an IP address is globally routable.
- Retrieves country, region, city, ISP, organization, and timezone information.
- Handles invalid IP addresses and API/network errors.

## Technologies Used
- Python
- Requests library
- ipaddress module
- ipwho.is API

## Installation

Install the required library:

```bash
pip install requests
```

## How to Run

```bash
python ip_lookup.py
```

Enter a public IP address when prompted.

## Note
IP geolocation information is approximate and may not identify an exact physical location. API availability and returned information may vary.
