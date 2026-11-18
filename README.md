<div align="center">
<a href="README.md"><img src="assets/lang-en-on.svg" height="48" alt="English"/></a>
<a href="README.ar.md"><img src="assets/lang-ar.svg" height="48" alt="العربية"/></a>
<a href="README.tr.md"><img src="assets/lang-tr.svg" height="48" alt="Türkçe"/></a>
</div>

<img src="assets/en/hero.svg" alt="Ranim: software engineer, video editor and graphic designer" width="100%"/>

<img src="assets/en/sheet.svg" width="100%" alt="Character sheet: software engineering student at Istinye University, Istanbul. English, Arabic, Turkish. 6 projects."/>

<img src="assets/en/b-levels.svg" width="100%" alt="Levels"/>

<a href="https://github.com/RanimAlyaseen/Orcha-App"><img src="assets/en/level-01.svg" width="100%" alt="Level 01, Orcha: AI agent control plane. Human review queue, multi-tenant, JWT auth, live on Railway, 7 end-to-end tests."/></a>
<div align="right"><sub><a href="https://orcha-official.up.railway.app">Open the live demo</a> · <a href="https://github.com/RanimAlyaseen/Orcha-App">Source</a></sub></div>

<a href="https://github.com/RanimAlyaseen/team-ultron-medical-abstract-classification"><img src="assets/en/level-02.svg" width="100%" alt="Level 02, medical abstract classifier, team project. My part: models, BiomedBERT, evaluation. Found 988 shared train/test abstracts. 0.8603 macro F1 on a locked test set."/></a>
<div align="right"><sub><a href="https://github.com/RanimAlyaseen/team-ultron-medical-abstract-classification">Source</a></sub></div>

<a href="https://github.com/RanimAlyaseen/tourism-crm-dbms"><img src="assets/en/level-03.svg" width="100%" alt="Level 03, tourism CRM database, university project. MySQL, 9 tables, 3 views, 6 triggers. Blocks overpayment and mismatched reviews."/></a>
<div align="right"><sub><a href="https://github.com/RanimAlyaseen/tourism-crm-dbms">Source</a></sub></div>

<img src="assets/en/b-side.svg" width="100%" alt="Side quests"/>

<table><tr>
<td width="33%"><a href="https://github.com/RanimAlyaseen/casie-event-argument-extraction"><img src="assets/en/side-04.svg" width="100%" alt="CASIE event extraction, team NLP project. 26 roles. 0.6196 Arg-C F1."/></a></td>
<td width="33%"><a href="https://github.com/RanimAlyaseen/icelandic-asr-project3"><img src="assets/en/side-05.svg" width="100%" alt="Icelandic ASR data preparation, team project. 20 hours of Samromur, zero shared speakers."/></a></td>
<td width="33%"><a href="https://github.com/RanimAlyaseen/book-rating-prediction"><img src="assets/en/side-06.svg" width="100%" alt="Book rating prediction. Reproducible ML experiment. ROC-AUC 0.433, no edge over the baseline."/></a></td>
</tr></table>

<img src="assets/b-know.svg" width="100%" alt="What I know"/>

<img src="assets/skills.svg" width="100%" alt="Programming: JavaScript, Python, SQL. Web: React, Vite, Node, Express, Prisma, REST APIs. Data: PostgreSQL, MySQL, SQLite. ML and NLP: PyTorch, Transformers, scikit-learn, pandas. Delivery: Docker, Nginx, Railway, Git, Playwright, pytest. Creative: graphic design, video editing. Spoken: English, Arabic, Turkish."/>

<img src="assets/b-contact.svg" width="100%" alt="Contact"/>

<div align="center">
<a href="https://www.linkedin.com/in/ranim-alyaseen-846522373"><img src="assets/btn-linkedin.svg" height="56" alt="LinkedIn"/></a>
<a href="https://github.com/RanimAlyaseen?tab=repositories"><img src="assets/btn-github.svg" height="56" alt="GitHub repositories"/></a>
<a href="https://drive.google.com/drive/folders/1t_D6z8vG5mqFVUuV0Yiw7lJgMr2kazwr?usp=sharing"><img src="assets/btn-research.svg" height="56" alt="Research"/></a>
</div>

<details>
<summary><b>Full written details</b> (projects, research, technical foundation)</summary>

### Featured engineering work

#### [Orcha — AI Agent Management Platform](https://github.com/RanimAlyaseen/Orcha-App)

Orcha brings AI agents, tasks, customer records, activity, and human-review workflows into one management dashboard.

**Engineering highlight:** A multi-tenant full-stack architecture with JWT authentication, role-aware access, REST workflows, Docker deployment, and end-to-end browser tests.

**Stack:** React, Vite, Node.js, Express, Prisma, PostgreSQL, Docker.

#### [Tourism CRM DBMS](https://github.com/RanimAlyaseen/tourism-crm-dbms)

A MySQL data layer for a tourism CRM, covering customers, packages, bookings, payments, reviews, agents, and reporting.

**Engineering highlight:** Database-level rules protect booking and payment integrity through foreign keys, triggers, atomic balance tracking, guarded totals, and controlled two-session concurrency tests.

**Stack:** MySQL 8, SQL, InnoDB transactions, PowerShell test runners.

#### [Medical Abstract Disease Classification](https://github.com/RanimAlyaseen/team-ultron-medical-abstract-classification)

A Team Ultron course project that classifies medical abstracts into five disease categories and compares classical, neural, and transformer models.

**Engineering highlight:** After auditing dataset overlap and rebuilding deterministic splits, the team selected models on validation data and evaluated the winner once on the locked test set. BiomedBERT achieved **0.8603 locked-test Macro F1**. My documented work covered model comparison, BiomedBERT fine-tuning, benchmark construction, error analysis, and final evaluation.

**Stack:** Python, pandas, scikit-learn, PyTorch, Transformers.

#### [Book High-Rating Prediction](https://github.com/RanimAlyaseen/book-rating-prediction)

A binary-classification experiment that predicts whether a book belongs to the high-rating class, defined as a rating of at least 4.6.

**Engineering highlight:** The reproducible workflow uses group-aware splitting, training-only model selection, a majority-class baseline, uncertainty estimates, automated tests, and a Streamlit demo. The selected model did **not** establish a reliable held-out advantage over the baseline.

**Stack:** Python, pandas, scikit-learn, pytest, Streamlit.

### Research & technical studies

#### [AI-Assisted Pulmonary Nodule Detection in Chest CT](https://drive.google.com/drive/folders/1t_D6z8vG5mqFVUuV0Yiw7lJgMr2kazwr?usp=sharing)

**Research & Pre-Prototype System Design** — literature synthesis, a proposed AI pipeline, evaluation methodology, clinical workflow design, and safety and regulatory considerations. This work does not claim a trained model, diagnostic results, clinical validation, or deployment.

### Additional technical work

- [CASIE Event Argument Extraction](https://github.com/RanimAlyaseen/casie-event-argument-extraction) — a team NLP benchmark with event-conditioned scoring, validation-selected RoBERTa, checkpoint verification, and an explicit distinction between gold-trigger benchmark results and the unmeasured raw-text demo pipeline.
- [Icelandic ASR Dataset Preparation](https://github.com/RanimAlyaseen/icelandic-asr-project3) — reproducible preparation and integrity checks for a speaker/session-separated 20-hour Samrómur subset for Whisper and wav2vec 2.0 experiments; human listening and transcript-agreement review remain documented as pending.

### Technical foundation

**Used in published repositories**

- **Languages:** JavaScript, Python, SQL.
- **Application engineering:** React, Vite, Node.js, Express, REST APIs, Prisma.
- **Data systems:** PostgreSQL, MySQL, SQLite, relational modeling, transactions.
- **ML & NLP:** pandas, scikit-learn, PyTorch, Transformers, model comparison, leakage-aware splitting, Macro F1 and error analysis.
- **Engineering workflow:** Git, Docker, pytest, Playwright, reproducible scripts, technical documentation.

**Currently deepening**

- Applied NLP, biomedical language models, speech processing, and evaluation design.
- The connection between reliable software architecture and maintainable AI-enabled products.

### How I approach engineering

- Start with the system boundary, data contract, and failure cases.
- Make important behavior reproducible and testable.
- Separate measured results from assumptions and future work.
- Document limitations as part of the engineering result.

### Connect

[GitHub](https://github.com/RanimAlyaseen) · [LinkedIn](https://www.linkedin.com/in/ranim-alyaseen-846522373)

<sub>Team and university projects are identified as such in their repositories. Contribution claims above follow the published attribution records.</sub>

</details>
