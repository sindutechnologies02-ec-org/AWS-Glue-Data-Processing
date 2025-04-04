# AWS-Glue-Data-Processing-project
Project Overview:
This project demonstrates how to process and transform data using AWS Glue, Amazon S3, and Python. We use AWS Glue Crawlers to discover schema, AWS Glue Jobs to process data, and Amazon S3 to store both input and output files.

 Architecture:
 Upload Data: Store the Parquet file in an Amazon S3 bucket.

AWS Glue Crawler: Automatically detects schema and creates a database in the AWS Glue Data Catalog.

AWS Glue Job: Processes the data and converts it into CSV format.

Output Storage: Saves the processed CSV file in another S3 bucket.

Technologies Used:
AWS Glue (Crawler & Job)

Amazon S3 (Storage)

Python (Data Processing)

Pandas (Data Transformation)

Boto3 (AWS SDK for Python)

Git & GitHub (Version Control)

Steps to Run This Project Locally:
Install Python (>=3.8)

Install required libraries: pip install pandas pyarrow boto3
