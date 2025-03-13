# ETL Project with Flask, Neo4j, PostgreSQL, and Docker

## 📌 Project Overview
This project implements an **ETL (Extract, Transform, Load) pipeline** using:
- **Flask API** to extract data from **Neo4j**
- Transformation logic for **movies** or **programming languages**
- Load the transformed data into **PostgreSQL**
- Export final data to a **CSV file**
- **Docker Compose** to manage services

## 📦 Technologies Used
- **Python (Flask)** - API development
- **Neo4j** - Graph database (source data)
- **PostgreSQL** - Relational database (destination)
- **Docker & Docker Compose** - Containerization

---

## 🚀 How to Run the Project
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/etl_project.git
cd etl_project
```

### 2️⃣ Start the Docker Containers
```sh
docker-compose up --build -d
```
This will:
- Start **Neo4j**, **PostgreSQL**, and the **Flask API**
- Create necessary networks and volumes

### 3️⃣ Check Running Containers
```sh
docker ps
```
Ensure that all required services are **Up**.

---

## 🔄 Running the ETL Pipeline

### **Extract Data**
Get raw data from Neo4j:
```sh
curl http://localhost:5000/api/extract
```

### **Transform Data**
Apply transformations:
```sh
curl http://localhost:5000/api/transform
```

### **Load Data into PostgreSQL**
Run the ETL load process:
```sh
curl http://localhost:5000/api/load
```

### **Export Data to CSV**
```sh
curl http://localhost:5000/api/export
```
The CSV file (`recap.csv`) will be saved in the **mounted volume**.

---

## 🛠 Stopping and Restarting

### **Stop Containers**
```sh
docker-compose down
```

### **Restart Containers**
```sh
docker-compose up -d
```

---

## 📂 Project Structure
```
📂 etl_project/
├── 📄 Dockerfile
├── 📄 docker-compose.yml
├── 📂 app/
│   ├── 📄 app.py        # Flask API
│   ├── 📄 extract.py    # Extract logic (Neo4j)
│   ├── 📄 transform.py  # Transform logic
│   ├── 📄 load.py       # Load logic (PostgreSQL)
│   ├── 📄 export.py     # Export to CSV
├── 📄 requirements.txt  # Dependencies
└── 📄 README.md         # Project Documentation
```

---

## 📝 Notes
- **Ensure Docker is installed** before running the project.
- The dataset is chosen based on **your student ID (odd/even).**
- Modify `.env` if needed for **database credentials**.

✅ **Now your ETL project is ready to run!** 🚀

