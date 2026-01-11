# API to MS-SQL Data Pipeline

## Overview

This project demonstrates an end-to-end data pipeline that:

1. Fetches data from a public REST API  
2. Normalizes nested JSON into a Pandas DataFrame  
3. Connects to a local MS-SQL Server using SQLAlchemy  
4. Creates a table and loads the data into the database  

The pipeline is designed with clean separation of concerns and supports configuration through external variables.

---

## Project Structure
![Uploading structure.jpg…]()

---

## Features

- REST API data ingestion  
- JSON normalization using Pandas  
- MS-SQL connectivity via SQLAlchemy + pyodbc  
- Windows Authentication support  
- Automatic table creation from DataFrame  
- Configurable server/database via external file  
- Git-safe configuration handling  

---

## Requirements

### Software

- Python 3.10+  
- MS-SQL Server (local or remote)  
- ODBC Driver 17 or 18 for SQL Server  

### Python Libraries

```bash
pip install requests pandas sqlalchemy pyodbc
