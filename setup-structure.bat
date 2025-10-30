@echo off
echo ========================================
echo Creating Data Engineering Roadmap Structure
echo ========================================
echo.

REM Créer le répertoire principal
mkdir data-engineering-roadmap
cd data-engineering-roadmap

echo [1/4] Creating main directories...

REM Phase 1: Foundations (Mois 1-3)
mkdir 01-foundations
mkdir 01-foundations\python
mkdir 01-foundations\python\basics
mkdir 01-foundations\python\pandas
mkdir 01-foundations\python\pandas\exercises
mkdir 01-foundations\python\projects
mkdir 01-foundations\python\projects\log-analyzer
mkdir 01-foundations\python\projects\log-analyzer\tests
mkdir 01-foundations\python\projects\csv-processor

mkdir 01-foundations\sql
mkdir 01-foundations\sql\basics
mkdir 01-foundations\sql\advanced
mkdir 01-foundations\sql\exercises
mkdir 01-foundations\sql\exercises\leetcode-solutions
mkdir 01-foundations\sql\exercises\sqlzoo-solutions
mkdir 01-foundations\sql\projects
mkdir 01-foundations\sql\projects\ecommerce-warehouse

mkdir 01-foundations\git-linux
mkdir 01-foundations\git-linux\bash-scripts

echo [2/4] Creating infrastructure directories...

REM Phase 2: Infrastructure (Mois 4-6)
mkdir 02-infrastructure
mkdir 02-infrastructure\docker
mkdir 02-infrastructure\docker\basics
mkdir 02-infrastructure\docker\basics\docker-compose-examples
mkdir 02-infrastructure\docker\projects
mkdir 02-infrastructure\docker\projects\data-stack
mkdir 02-infrastructure\docker\projects\data-stack\postgres
mkdir 02-infrastructure\docker\projects\data-stack\airflow
mkdir 02-infrastructure\docker\projects\data-stack\jupyter

mkdir 02-infrastructure\cloud
mkdir 02-infrastructure\cloud\aws
mkdir 02-infrastructure\cloud\aws\s3-examples
mkdir 02-infrastructure\cloud\aws\lambda-functions
mkdir 02-infrastructure\cloud\aws\rds-setup
mkdir 02-infrastructure\cloud\aws\terraform
mkdir 02-infrastructure\cloud\gcp

mkdir 02-infrastructure\airflow
mkdir 02-infrastructure\airflow\dags
mkdir 02-infrastructure\airflow\plugins
mkdir 02-infrastructure\airflow\tests

echo [3/4] Creating big data directories...

REM Phase 3: Big Data (Mois 7-9)
mkdir 03-big-data
mkdir 03-big-data\spark
mkdir 03-big-data\spark\pyspark-basics
mkdir 03-big-data\spark\spark-streaming
mkdir 03-big-data\spark\notebooks
mkdir 03-big-data\spark\projects
mkdir 03-big-data\spark\projects\log-analysis-spark

mkdir 03-big-data\data-warehouse
mkdir 03-big-data\data-warehouse\snowflake
mkdir 03-big-data\data-warehouse\dbt
mkdir 03-big-data\data-warehouse\dbt\models
mkdir 03-big-data\data-warehouse\dbt\models\staging
mkdir 03-big-data\data-warehouse\dbt\models\intermediate
mkdir 03-big-data\data-warehouse\dbt\models\marts
mkdir 03-big-data\data-warehouse\dbt\tests

mkdir 03-big-data\streaming
mkdir 03-big-data\streaming\kafka
mkdir 03-big-data\streaming\kafka\kafka-connect-configs
mkdir 03-big-data\streaming\projects
mkdir 03-big-data\streaming\projects\iot-monitoring

echo [4/4] Creating production directories...

REM Phase 4: Production (Mois 10-12)
mkdir 04-production
mkdir 04-production\dataops
mkdir 04-production\dataops\ci-cd
mkdir 04-production\dataops\ci-cd\.github
mkdir 04-production\dataops\ci-cd\.github\workflows
mkdir 04-production\dataops\monitoring
mkdir 04-production\dataops\monitoring\grafana-dashboards
mkdir 04-production\dataops\monitoring\prometheus-config
mkdir 04-production\dataops\data-quality
mkdir 04-production\dataops\data-quality\great-expectations

mkdir 04-production\optimization
mkdir 04-production\optimization\performance-analysis
mkdir 04-production\optimization\cost-optimization
mkdir 04-production\optimization\benchmarks

mkdir 04-production\interview-prep
mkdir 04-production\interview-prep\coding-challenges
mkdir 04-production\interview-prep\system-design
mkdir 04-production\interview-prep\sql-questions

REM Ressources transversales
mkdir resources
mkdir resources\cheatsheets
mkdir resources\architecture-diagrams

REM Daily logs
mkdir daily-logs
mkdir daily-logs\2025-10
mkdir daily-logs\2025-11
mkdir daily-logs\2025-12

echo.
echo ========================================
echo Creating essential files...
echo ========================================

REM Créer les fichiers essentiels
type nul > README.md
type nul > MON-POURQUOI.md
type nul > progress-tracker.md
type nul > requirements.txt
type nul > .gitignore

REM Fichiers Python de base
type nul > 01-foundations\python\basics\01-variables.py
type nul > 01-foundations\python\basics\02-functions.py
type nul > 01-foundations\python\basics\03-classes.py
type nul > 01-foundations\python\basics\README.md

REM Fichiers SQL de base
type nul > 01-foundations\sql\basics\01-select-queries.sql
type nul > 01-foundations\sql\basics\02-joins.sql
type nul > 01-foundations\sql\basics\03-aggregations.sql

REM Fichiers Git/Linux
type nul > 01-foundations\git-linux\git-commands.md
type nul > 01-foundations\git-linux\linux-cheatsheet.md

REM Fichiers ressources
type nul > resources\books-notes.md
type nul > resources\courses-completed.md
type nul > resources\cheatsheets\python-cheatsheet.md
type nul > resources\cheatsheets\sql-cheatsheet.md
type nul > resources\cheatsheets\docker-cheatsheet.md

REM Fichier weekly log
type nul > daily-logs\2025-10\week-01.md

echo.
echo ========================================
echo Creating .gitignore content...
echo ========================================

(
echo # Python
echo __pycache__/
echo *.py[cod]
echo *$py.class
echo *.so
echo .Python
echo venv/
echo env/
echo ENV/
echo.
echo # Jupyter
echo .ipynb_checkpoints
echo *.ipynb_checkpoints
echo.
echo # IDE
echo .vscode/
echo .idea/
echo *.swp
echo *.swo
echo.
echo # Data
echo *.csv
echo *.json
echo *.parquet
echo data/
echo datasets/
echo !sample-data/
echo.
echo # Credentials
echo .env
echo *.pem
echo *.key
echo credentials.json
echo secrets.yaml
echo.
echo # OS
echo .DS_Store
echo Thumbs.db
echo.
echo # Logs
echo *.log
echo.
echo # Build
echo dist/
echo build/
echo *.egg-info/
) > .gitignore

echo.
echo ========================================
echo Creating README.md template...
echo ========================================

(
echo # 🚀 My Data Engineering Learning Journey
echo.
echo ^![Progress]^(https://img.shields.io/badge/Progress-0%%25-yellow^)
echo ^![Days]^(https://img.shields.io/badge/Days%%20Learning-1-blue^)
echo.
echo ^> 12-month intensive program to become a professional Data Engineer
echo.
echo ## 🎯 Goal
echo Transition from beginner to job-ready Data Engineer in 12 months ^(Oct 2025 - Oct 2026^)
echo.
echo ## 📊 Current Progress
echo.
echo ### Phase 1: Foundations ^(Months 1-3^) ⏳
echo - [ ] Week 1: Python basics
echo - [ ] Week 2: Pandas fundamentals
echo - [ ] Week 3: SQL basics
echo - [ ] Week 4: Advanced SQL
echo.
echo ### Phase 2: Infrastructure ^(Months 4-6^) 🔜
echo ### Phase 3: Big Data ^(Months 7-9^) 🔜
echo ### Phase 4: Production ^(Months 10-12^) 🔜
echo.
echo ## 🛠️ Technologies Learning
echo.
echo **Languages ^& Core**
echo - Python
echo - SQL
echo - Bash
echo.
echo **Data Processing**
echo - Pandas, NumPy
echo - Apache Spark ^(upcoming^)
echo - dbt ^(upcoming^)
echo.
echo **Infrastructure**
echo - Docker ^(upcoming^)
echo - Apache Airflow ^(upcoming^)
echo - AWS/GCP ^(upcoming^)
echo.
echo ## 📁 Repository Structure
echo.
echo ```
echo 01-foundations/     # Python, SQL, Git basics
echo 02-infrastructure/  # Docker, Cloud, Airflow
echo 03-big-data/        # Spark, Warehousing, Streaming
echo 04-production/      # DataOps, Optimization
echo ```
echo.
echo ## 📈 Stats
echo.
echo - **Total Learning Hours**: 0h
echo - **Exercises Completed**: 0
echo - **Lines of Code Written**: 0
echo - **Projects Built**: 0
echo.
echo ## 📅 Last Updated
echo %date%
) > README.md

echo.
echo ========================================
echo Creating progress tracker template...
echo ========================================

(
echo # 📊 Weekly Progress Tracker
echo.
echo ## Week 1 ^(%date%^)
echo.
echo ### ⏱️ Time Spent: 0h
echo.
echo ### ✅ Completed
echo - [ ] Setup development environment
echo - [ ] Create project structure
echo - [ ] First GitHub commit
echo.
echo ### 💻 Code Written
echo - None yet
echo.
echo ### 🧠 Key Learnings
echo - Project structure is important
echo - Organization helps learning
echo.
echo ### 🎯 Next Week Goals
echo - Start Python basics
echo - Complete 10 exercises
echo - First mini project
echo.
echo ### 💭 Reflection
echo Just started! Excited for this journey.
) > progress-tracker.md

echo.
echo ========================================
echo Creating requirements.txt...
echo ========================================

(
echo # Core Data Processing
echo pandas==2.1.3
echo numpy==1.26.2
echo.
echo # Jupyter
echo jupyter==1.0.0
echo ipython==8.18.1
echo.
echo # Data Visualization
echo matplotlib==3.8.2
echo seaborn==0.13.0
echo.
echo # Testing
echo pytest==7.4.3
echo pytest-cov==4.1.0
echo.
echo # Code Quality
echo black==23.11.0
echo flake8==6.1.0
echo mypy==1.7.1
echo.
echo # CLI
echo click==8.1.7
echo.
echo # Utils
echo python-dotenv==1.0.0
) > requirements.txt

echo.
echo ========================================
echo Creating first Python script...
echo ========================================

(
echo """
echo My First Python Script - Data Engineering Journey
echo Day 1: Hello World
echo """
echo.
echo def main^(^):
echo     print^("🚀 Welcome to My Data Engineering Journey!"^)
echo     print^("Day 1: Setting up the foundation"^)
echo     print^("Let's build something amazing!"^)
echo.
echo if __name__ == "__main__":
echo     main^(^)
) > 01-foundations\python\basics\01-variables.py

echo.
echo ========================================
echo Initializing Git repository...
echo ========================================

git init
git add .
git commit -m "feat: initial project structure for 12-month data engineering journey"

echo.
echo ========================================
echo ✅ STRUCTURE CREATED SUCCESSFULLY!
echo ========================================
echo.
echo Next steps:
echo 1. Review the structure: cd data-engineering-roadmap
echo 2. Create GitHub repo and push:
echo    git remote add origin https://github.com/YOUR_USERNAME/data-engineering-roadmap.git
echo    git branch -M main
echo    git push -u origin main
echo.
echo 3. Start learning! Open 01-foundations/python/basics/
echo.
echo Happy coding! 🚀
echo.
pause