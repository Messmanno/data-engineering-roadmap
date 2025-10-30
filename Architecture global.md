ton-username/
├── 📦 data-engineering-roadmap/          # Repo PRINCIPAL (mono-repo learning)
├── 📦 portfolio-website/                 # Site portfolio (mois 12)
├── 📦 project-etl-pipeline/              # Projet trimestre 1 (isolé)
├── 📦 project-data-platform/             # Projet trimestre 2 (isolé)
├── 📦 project-realtime-streaming/        # Projet trimestre 3 (isolé)
├── 📦 project-capstone/                  # Projet final (isolé)
└── 📦 awesome-data-engineering/          # Curation de ressources (bonus)
```

---

## 📦 REPO PRINCIPAL : `data-engineering-roadmap`

### Structure Détaillée
```
data-engineering-roadmap/
│
├── 📄 README.md                          # Vue d'ensemble + progression
├── 📄 MON-POURQUOI.md                    # Ton "why" (privé ou public)
├── 📄 progress-tracker.md                # Suivi hebdomadaire
├── 📄 .gitignore                         # Fichiers à ignorer
├── 📄 requirements.txt                   # Dépendances Python globales
│
├── 📂 01-foundations/                    # MOIS 1-3
│   ├── 📂 python/
│   │   ├── 📂 basics/
│   │   │   ├── 01-variables.py
│   │   │   ├── 02-functions.py
│   │   │   ├── 03-classes.py
│   │   │   └── README.md               # Notes d'apprentissage
│   │   ├── 📂 pandas/
│   │   │   ├── 01-dataframes.ipynb
│   │   │   ├── 02-transformations.ipynb
│   │   │   ├── 03-joins.ipynb
│   │   │   └── exercises/
│   │   │       ├── exercise-01.py
│   │   │       └── solution-01.py
│   │   └── 📂 projects/
│   │       ├── log-analyzer/
│   │       │   ├── README.md
│   │       │   ├── main.py
│   │       │   ├── requirements.txt
│   │       │   └── tests/
│   │       └── csv-processor/
│   │
│   ├── 📂 sql/
│   │   ├── 📂 basics/
│   │   │   ├── 01-select-queries.sql
│   │   │   ├── 02-joins.sql
│   │   │   └── 03-aggregations.sql
│   │   ├── 📂 advanced/
│   │   │   ├── 01-window-functions.sql
│   │   │   ├── 02-ctes.sql
│   │   │   └── 03-optimization.sql
│   │   ├── 📂 exercises/
│   │   │   ├── leetcode-solutions/
│   │   │   └── sqlzoo-solutions/
│   │   └── 📂 projects/
│   │       └── ecommerce-warehouse/
│   │           ├── schema.sql
│   │           ├── seed-data.sql
│   │           └── analytics-queries.sql
│   │
│   └── 📂 git-linux/
│       ├── git-commands.md
│       ├── linux-cheatsheet.md
│       └── bash-scripts/
│           ├── backup-script.sh
│           └── automation.sh
│
├── 📂 02-infrastructure/                 # MOIS 4-6
│   ├── 📂 docker/
│   │   ├── 📂 basics/
│   │   │   ├── Dockerfile.example
│   │   │   └── docker-compose-examples/
│   │   ├── 📂 projects/
│   │   │   └── data-stack/
│   │   │       ├── docker-compose.yml
│   │   │       ├── postgres/
│   │   │       ├── airflow/
│   │   │       └── jupyter/
│   │   └── README.md
│   │
│   ├── 📂 cloud/
│   │   ├── 📂 aws/
│   │   │   ├── s3-examples/
│   │   │   ├── lambda-functions/
│   │   │   ├── rds-setup/
│   │   │   └── terraform/              # Infrastructure as Code
│   │   │       ├── main.tf
│   │   │       ├── variables.tf
│   │   │       └── outputs.tf
│   │   ├── 📂 gcp/                     # Si tu explores aussi GCP
│   │   └── notes.md
│   │
│   └── 📂 airflow/
│       ├── 📂 dags/
│       │   ├── 01-hello-world-dag.py
│       │   ├── 02-etl-simple-dag.py
│       │   └── 03-complex-pipeline-dag.py
│       ├── 📂 plugins/
│       ├── 📂 tests/
│       └── docker-compose.yml
│
├── 📂 03-big-data/                       # MOIS 7-9
│   ├── 📂 spark/
│   │   ├── 📂 pyspark-basics/
│   │   │   ├── 01-dataframes.py
│   │   │   ├── 02-transformations.py
│   │   │   └── 03-optimizations.py
│   │   ├── 📂 spark-streaming/
│   │   │   └── real-time-processing.py
│   │   ├── 📂 notebooks/
│   │   │   └── spark-analysis.ipynb
│   │   └── 📂 projects/
│   │       └── log-analysis-spark/
│   │
│   ├── 📂 data-warehouse/
│   │   ├── 📂 snowflake/
│   │   │   ├── setup-scripts.sql
│   │   │   └── warehouse-design.sql
│   │   ├── 📂 dbt/
│   │   │   ├── models/
│   │   │   │   ├── staging/
│   │   │   │   ├── intermediate/
│   │   │   │   └── marts/
│   │   │   ├── tests/
│   │   │   └── dbt_project.yml
│   │   └── dimensional-modeling.md
│   │
│   └── 📂 streaming/
│       ├── 📂 kafka/
│       │   ├── docker-compose.yml
│       │   ├── producer.py
│       │   ├── consumer.py
│       │   └── kafka-connect-configs/
│       └── 📂 projects/
│           └── iot-monitoring/
│
├── 📂 04-production/                     # MOIS 10-12
│   ├── 📂 dataops/
│   │   ├── 📂 ci-cd/
│   │   │   ├── .github/
│   │   │   │   └── workflows/
│   │   │   │       ├── test.yml
│   │   │   │       └── deploy.yml
│   │   │   └── gitlab-ci.yml
│   │   ├── 📂 monitoring/
│   │   │   ├── grafana-dashboards/
│   │   │   └── prometheus-config/
│   │   └── 📂 data-quality/
│   │       └── great-expectations/
│   │
│   ├── 📂 optimization/
│   │   ├── performance-analysis/
│   │   ├── cost-optimization/
│   │   └── benchmarks/
│   │
│   └── 📂 interview-prep/
│       ├── coding-challenges/
│       ├── system-design/
│       └── sql-questions/
│
├── 📂 resources/                         # Ressources transversales
│   ├── books-notes.md
│   ├── courses-completed.md
│   ├── cheatsheets/
│   │   ├── python-cheatsheet.md
│   │   ├── sql-cheatsheet.md
│   │   └── docker-cheatsheet.md
│   └── architecture-diagrams/
│       └── (fichiers .drawio ou .png)
│
└── 📂 daily-logs/                        # Journal quotidien
    ├── 2025-10/
    │   ├── week-01.md
    │   ├── week-02.md
    │   └── ...
    └── 2025-11/