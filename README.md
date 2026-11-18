<div align="center">
<a href="README.md"><img src="assets/lang-en-on.svg" height="40" alt="English"/></a>
<a href="README.ar.md"><img src="assets/lang-ar.svg" height="40" alt="العربية"/></a>
<a href="README.tr.md"><img src="assets/lang-tr.svg" height="40" alt="Türkçe"/></a>
</div>


<img src="assets/en/hero.svg" width="100%" alt="Ranim: engineer by degree, editor and designer by habit. A short film about building things that hold up."/>

> **Logline:** A final-year software engineer who ships full-stack products, runs ML experiments honestly, and designs and edits the visuals around them.

<img src="assets/en/s0.svg" width="100%" alt="Cold open: who's behind the camera"/>

I'm Ranim, a final-year software engineering student at Istinye University in Istanbul. I work in English, Arabic and Turkish, and I split my time between three crafts: building software, editing video, and designing visuals. What they share is the part I care about most: making something clear, and making sure it holds up when someone pushes on it. This page is the director's cut.

<img src="assets/en/s1.svg" width="100%" alt="Scene 1: Orcha, who watches the AI agents?"/>

<img src="assets/en/d-orcha.svg" width="100%" alt="Diagram: AI agents on WhatsApp, voice, web chat and email flow into Orcha, then through a human review queue (approve, edit, reject) before reaching the customer."/>

Companies are putting AI agents on WhatsApp, phone lines, website chat and email. Then a practical question shows up: **who is watching them?** Orcha is my answer. It's one control plane for every agent a team runs, with tasks, customer records, event logs and analytics, plus a review queue where a human approves, edits or rejects flagged output *before* it reaches a customer.

It's multi-tenant, with role-based access, JWT authentication, email verification and rate limiting. It's deployed on Railway, runs in Docker behind Nginx, and is covered by 7 Playwright end-to-end specs. The live demo follows a fictional clinic with four agents and bilingual Arabic and English event logs (login details are in the repo README).

**Stack:** React 18 · Vite · Node.js / Express · Prisma · PostgreSQL · Docker

[Open the live demo](https://orcha-official.up.railway.app) · [Read the code](https://github.com/RanimAlyaseen/Orcha-App)

<img src="assets/en/s2.svg" width="100%" alt="Scene 2: the day the test set lied"/>

<img src="assets/en/d-leak.svg" width="100%" alt="Diagram: the original train and test files shared 988 abstracts. The team audited, rebuilt the splits, chose models on validation, and looked at the locked test set once: 0.8603 macro F1."/>

In a five-person NLP course project at Istinye University, the task was to classify medical abstracts into five disease categories. Before any training, the team audited the data and found a problem: of 14,438 rows, only 11,227 were unique texts, **988 abstracts appeared in both the train and the test files**, and 2,929 groups of abstracts carried conflicting labels. A test set that overlaps the training set measures nothing.

So the team cleaned the data, rebuilt the splits, chose models on validation only, and looked at the test set exactly once. My part was model training and comparison, BiomedBERT fine-tuning, the benchmark, error analysis and the final evaluation. BiomedBERT won with **0.8672 macro F1 on validation and 0.8603 on the locked test set**. A gap of just 0.0069 suggests the score holds up.

[Source and docs](https://github.com/RanimAlyaseen/team-ultron-medical-abstract-classification)

<img src="assets/en/s3.svg" width="100%" alt="Scene 3: the model that didn't win"/>

<img src="assets/en/d-twist.svg" width="100%" alt="Diagram: the selected model scored ROC-AUC 0.433 on held-out data, below the 0.5 coin-flip line. Published anyway."/>

Not every experiment wins. In a university ML project that I rebuilt as a reproducible experiment, the goal was to predict from six metadata fields whether a book's rating is 4.6 or higher (348 books). I used group-aware splits, chose models using training data only, and compared everything against a majority-class baseline.

The result: the selected Logistic Regression scored 0.457 held-out accuracy and 0.433 ROC-AUC, which is **no reliable advantage over the baseline**. I published it exactly like that, with the limits written down, because a clear negative result is still a result. A Streamlit demo and automated tests ship with it.

[Source and docs](https://github.com/RanimAlyaseen/book-rating-prediction)

<img src="assets/en/s4.svg" width="100%" alt="Scene 4: money can't go negative"/>

<img src="assets/en/d-vault.svg" width="100%" alt="Diagram: a payment that would overpay a booking is rejected by a database trigger."/>

A CRM is only useful if its numbers can be trusted. For a tourism CRM database (a university DBMS project, rebuilt as a reproducible MySQL repository) I put the rules inside the database itself: nine tables, three reporting views, two functions and six triggers.

A payment that would overpay a booking is **rejected by a trigger**. A review has to belong to the customer who owns the booking, enforced with a composite foreign key. SQL test cases and controlled two-session concurrency tests prove it. It's the database layer only, with no web UI.

[Source and docs](https://github.com/RanimAlyaseen/tourism-crm-dbms)

<img src="assets/en/s5.svg" width="100%" alt="Scene 5: side quests"/>

<img src="assets/en/d-side.svg" width="100%" alt="Three side projects: CASIE event extraction with 26 roles, Icelandic speech data with zero shared speakers, and a pulmonary nodule detection design study."/>

[CASIE](https://github.com/RanimAlyaseen/casie-event-argument-extraction) · [Icelandic ASR](https://github.com/RanimAlyaseen/icelandic-asr-project3) · [Pulmonary nodule study](https://drive.google.com/drive/folders/1t_D6z8vG5mqFVUuV0Yiw7lJgMr2kazwr?usp=sharing)

<img src="assets/en/s6.svg" width="100%" alt="Toolbox"/>

<img src="assets/en/toolbox.svg" width="100%" alt="Toolbox. Programming: JavaScript, Python, SQL. Web: React, Vite, Node.js, Express, Prisma, REST APIs. Data: PostgreSQL, MySQL, SQLite. ML and NLP: PyTorch, Transformers, scikit-learn, pandas. Delivery: Docker, Nginx, Railway, Git, Playwright, pytest. Creative: graphic design, video editing. Spoken: English, Arabic, Turkish."/>

<img src="assets/en/s7.svg" width="100%" alt="Next episode"/>

<img src="assets/en/next.svg" width="100%" alt="Next episode: speech, biomedical NLP, and how to evaluate them honestly."/>

<div align="center">
<a href="https://www.linkedin.com/in/ranim-alyaseen-846522373"><img src="assets/en/btn-linkedin.svg" height="56" alt="LinkedIn"/></a>
<a href="https://github.com/RanimAlyaseen?tab=repositories"><img src="assets/en/btn-github.svg" height="56" alt="GitHub"/></a>
<a href="https://drive.google.com/drive/folders/1t_D6z8vG5mqFVUuV0Yiw7lJgMr2kazwr?usp=sharing"><img src="assets/en/btn-research.svg" height="56" alt="Research"/></a>
</div>

<sub>Team and university projects are identified as such in their repositories. Contribution claims follow the published attribution records.</sub>
