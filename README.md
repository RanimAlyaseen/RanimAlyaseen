<div align="center">

<img src="assets/hero.svg" alt="Ranim: software engineer, video editor and graphic designer, pixel art at a desk" width="100%"/>

<a href="https://github.com/RanimAlyaseen?tab=repositories"><img src="assets/btn-github.svg" height="56" alt="GitHub repositories"/></a>
<a href="https://www.linkedin.com/in/ranim-alyaseen-846522373"><img src="assets/btn-linkedin.svg" height="56" alt="LinkedIn"/></a>
<a href="https://orcha-official.up.railway.app"><img src="assets/btn-demo.svg" height="56" alt="Orcha live demo"/></a>
<a href="https://drive.google.com/drive/folders/1t_D6z8vG5mqFVUuV0Yiw7lJgMr2kazwr?usp=sharing"><img src="assets/btn-research.svg" height="56" alt="Research"/></a>

</div>

**Software Engineering · Full-stack systems · Applied ML/NLP · Video editing and graphic design**

I am a final-year Software Engineering student building full-stack applications, backend services, and relational data systems, and extending that foundation into applied machine learning and NLP through reproducible experiments and careful evaluation. I work in English, Arabic, and Turkish.

<img src="assets/b-sheet.svg" width="100%" alt="character sheet"/>

<img src="assets/sheet.svg" width="100%" alt="Character sheet: software engineer, video editor and graphic designer, final-year student, Team Ultron. Languages: English, Arabic, Turkish. 6 projects, best F1 0.86"/>

<img src="assets/b-quests.svg" width="100%" alt="quest log"/>

<div align="center">
<table>
<tr>
<td width="50%"><a href="https://github.com/RanimAlyaseen/Orcha-App"><img src="assets/quest-01.svg" width="100%" alt="Orcha: AI agent management platform"/></a></td>
<td width="50%"><a href="https://github.com/RanimAlyaseen/tourism-crm-dbms"><img src="assets/quest-02.svg" width="100%" alt="Tourism CRM DBMS"/></a></td>
</tr>
<tr>
<td width="50%"><a href="https://github.com/RanimAlyaseen/team-ultron-medical-abstract-classification"><img src="assets/quest-03.svg" width="100%" alt="Medical abstract classification"/></a></td>
<td width="50%"><a href="https://github.com/RanimAlyaseen/casie-event-argument-extraction"><img src="assets/quest-04.svg" width="100%" alt="CASIE event argument extraction"/></a></td>
</tr>
<tr>
<td width="50%"><a href="https://github.com/RanimAlyaseen/icelandic-asr-project3"><img src="assets/quest-05.svg" width="100%" alt="Icelandic ASR dataset preparation"/></a></td>
<td width="50%"><a href="https://github.com/RanimAlyaseen/book-rating-prediction"><img src="assets/quest-06.svg" width="100%" alt="Book high-rating prediction"/></a></td>
</tr>
</table>
</div>

<img src="assets/b-tree.svg" width="100%" alt="skill tree"/>

<img src="assets/tree.svg" width="100%" alt="Skill tree. Build: React, Vite, Node and Express, Prisma, Recharts. Data: PostgreSQL, MySQL, SQLite, SQL triggers, schema design. ML and NLP: Python, PyTorch, Transformers, scikit-learn, pandas. Ship and test: Docker and Nginx, Railway, Playwright, pytest, Git and LFS"/>

<img src="assets/b-ach.svg" width="100%" alt="achievements"/>

<img src="assets/ach.svg" width="100%" alt="Achievements: 0.8603 macro F1 on a locked test set; 988 train-test leaks found in the original corpus; 26 event roles in CASIE; 0 shared speakers across Icelandic splits; 7 Playwright specs; 6 database triggers"/>

<img src="assets/b-tips.svg" width="100%" alt="loading tips"/>

<img src="assets/tips.svg" width="100%" alt="How I work: start with the system boundary, make results reproducible, separate measured from assumed, document limits as results"/>

<img src="assets/next.svg" width="100%" alt="Next level: speech, biomedical NLP and evaluation design"/>

<details>
<summary><b>Full written details</b> (projects, research, technical foundation)</summary>

### Featured engineering work

### [Orcha — AI Agent Management Platform](https://github.com/RanimAlyaseen/Orcha-App)

Orcha brings AI agents, tasks, customer records, activity, and human-review workflows into one management dashboard.

**Engineering highlight:** A multi-tenant full-stack architecture with JWT authentication, role-aware access, REST workflows, Docker deployment, and end-to-end browser tests.

**Stack:** React, Vite, Node.js, Express, Prisma, PostgreSQL, Docker.

### [Tourism CRM DBMS](https://github.com/RanimAlyaseen/tourism-crm-dbms)

A MySQL data layer for a tourism CRM, covering customers, packages, bookings, payments, reviews, agents, and reporting.

**Engineering highlight:** Database-level rules protect booking and payment integrity through foreign keys, triggers, atomic balance tracking, guarded totals, and controlled two-session concurrency tests.

**Stack:** MySQL 8, SQL, InnoDB transactions, PowerShell test runners.

### [Medical Abstract Disease Classification](https://github.com/RanimAlyaseen/team-ultron-medical-abstract-classification)

A Team Ultron course project that classifies medical abstracts into five disease categories and compares classical, neural, and transformer models.

**Engineering highlight:** After auditing dataset overlap and rebuilding deterministic splits, the team selected models on validation data and evaluated the winner once on the locked test set. BiomedBERT achieved **0.8603 locked-test Macro F1**. My documented work covered model comparison, BiomedBERT fine-tuning, benchmark construction, error analysis, and final evaluation.

**Stack:** Python, pandas, scikit-learn, PyTorch, Transformers.

### [Book High-Rating Prediction](https://github.com/RanimAlyaseen/book-rating-prediction)

A binary-classification experiment that predicts whether a book belongs to the high-rating class, defined as a rating of at least 4.6.

**Engineering highlight:** The reproducible workflow uses group-aware splitting, training-only model selection, a majority-class baseline, uncertainty estimates, automated tests, and a Streamlit demo. The selected model did **not** establish a reliable held-out advantage over the baseline.

**Stack:** Python, pandas, scikit-learn, pytest, Streamlit.

### Research & technical studies

### [AI-Assisted Pulmonary Nodule Detection in Chest CT](https://drive.google.com/drive/folders/1t_D6z8vG5mqFVUuV0Yiw7lJgMr2kazwr?usp=sharing)

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
