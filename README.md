# 🚀 Azure Data Factory Incremental Data Ingestion Pipeline

## 📌 Project Overview

This project demonstrates a **real‑world incremental data ingestion pipeline** built using **Azure Data Factory (ADF)**. The pipeline efficiently loads only **new or changed data** from **Azure SQL Database** into **Azure Data Lake Storage** using a CDC‑style approach. It is fully parameterized, reusable, and version‑controlled using **GitHub integration**.

The goal of this project is to showcase **production‑ready data engineering practices** such as incremental loading, looping over multiple tables, and clean data storage formats.

---

## 🏗️ Architecture Overview

**Source:** Azure SQL Database
**Orchestration:** Azure Data Factory
**Storage:** Azure Data Lake (Parquet format)
**Version Control:** GitHub

**High‑level Flow:**

1. Identify the last loaded CDC value
2. Fetch only new records from the source table
3. Load data incrementally into Data Lake
4. Loop through multiple tables using a single pipeline
5. Skip processing when no new data is available

---

## 🔄 Pipeline Features

* ✅ Incremental data loading using CDC logic
* ✅ Parameterized pipeline for dynamic table ingestion
* ✅ **ForEach activity** to process multiple tables
* ✅ Conditional checks to avoid empty data loads
* ✅ Data stored in **Parquet format** for efficiency
* ✅ GitHub‑integrated ADF for version control

---

## 📂 Repository Structure

```
ADF-Incremental-Ingestion/
│
├── datasets/
│   ├── AzureSqlTable.json
│   ├── Parquet_dynamic.json
│
├── pipelines/
│   ├── Incremental_ingestion.json
│   ├── Incremental_Looping.json
│
├── linkedServices/
│   ├── AzureSqlDatabase.json
│   ├── AzureDataLake.json
│
├── screenshots/
│   ├── pipeline_run.png
│   ├── foreach_activity.png
│
└── README.md
```

---

## ⚙️ Pipeline Explanation

### 1️⃣ Incremental_Ingestion Pipeline

* Retrieves the **maximum CDC value** from the target
* Filters source data based on the last processed value
* Copies only new records to Data Lake

### 2️⃣ Incremental_Looping Pipeline

* Uses **ForEach activity**
* Accepts an array of table metadata as input
* Calls the incremental pipeline for each table

---

## 🧪Parameter Input

```json
[
  {
    "schema" : "dbo",
    "table" : "DimUser",
    "cdc_col" : "updated_at",
    "from_date" : ""
  },
  {
    "schema" : "dbo",
    "table" : "DimTrack",
    "cdc_col" : "updated_at",
    "from_date" : ""
  },
  {
    "schema" : "dbo",
    "table" : "DimDate",
    "cdc_col" : "date",
    "from_date" : ""
  },
  {
    "schema" : "dbo",
    "table" : "DimArtist",
    "cdc_col" : "updated_at",
    "from_date" : ""
  },
  {
    "schema" : "dbo",
    "table" : "FactStream",
    "cdc_col" : "stream_timestamp",
    "from_date" : ""
  }
]

```

---

## 📊 Dataset Details

* **Source Dataset:** Azure SQL Table (dynamic schema & table name)
* **Sink Dataset:** Parquet files in Azure Data Lake
* Supports dynamic folder paths and file names

---

## 🔐 Version Control

* ADF is connected to **GitHub**
* All pipelines, datasets, and linked services are tracked
* Enables safe collaboration and rollback

---

## 📸 Screenshots

<img width="1916" height="991" alt="OverAll Structure" src="https://github.com/user-attachments/assets/f372d4a9-7048-40e6-a83a-a2ea7a850735" />
<img width="1919" height="992" alt="Incremental looping" src="https://github.com/user-attachments/assets/00fca17e-0291-477b-aac3-1de60d1a180c" />
<img width="1919" height="905" alt="overall Parameters" src="https://github.com/user-attachments/assets/a8f965b2-3219-41e0-a72f-c8333052e405" />
<img width="1919" height="989" alt="Incremental Looping Parameters" src="https://github.com/user-attachments/assets/113c0fbe-5416-41dc-b7e6-67ab983f392b" />
<img width="1919" height="993" alt="Gold_DLT" src="https://github.com/user-attachments/assets/ff75544d-b940-46c6-805d-b90da7baa966" />
<img width="1919" height="988" alt="Git Configuration" src="https://github.com/user-attachments/assets/888e8d20-c149-4d32-aa95-6c4e405d67ac" />


---

## 🎯 Key Learnings

* How to build scalable incremental pipelines in ADF
* How to design reusable and parameter‑driven pipelines
* How to integrate GitHub with Azure Data Factory
* Best practices for production‑ready ETL pipelines

---


---

## 🏷️ Tags

`Azure Data Factory` `Incremental Load` `CDC` `ETL` `Data Engineering` `GitHub` `Parquet`

---

⭐ If you find this project useful, feel free to star the repository!
