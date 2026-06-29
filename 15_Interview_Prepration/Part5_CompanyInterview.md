### Agentic AI and Agentic Systems

# **Question)** Talk about data source, pre‑requisites you do to clean up the data  
**Answer)**  
**Data sources I commonly work with:** relational databases (SQL Server, Postgres), data lakes (Parquet/Delta on S3/ADLS), CSV/Excel exports, JSON APIs, unstructured documents (PDF, Word), logs, and enterprise stores (SharePoint, Confluence). For ML/NLP projects I also use image and audio sources.

**Pre‑requisites and stepwise cleanup (practical L3 approach):**  
1. **Data audit and profiling** — run automated profiling (counts, null rates, unique counts, histograms) to discover schema drift, cardinality, and data quality issues.  
2. **Schema & type normalization** — enforce correct dtypes (dates, numeric, categorical); coerce and log conversion errors.  
3. **Deduplication & identity resolution** — dedupe exact and fuzzy duplicates; unify entity keys (customer IDs, emails).  
4. **Missing value strategy** — decide per column: drop if mostly empty; impute with median/mean/KNN/iterative imputer; for time series use forward/backward fill. Document assumptions.  
5. **Outlier handling** — detect via IQR or robust z‑score; decide to cap, transform, or remove based on domain impact.  
6. **Normalization/Scaling** — StandardScaler or MinMax for distance‑based models; robust scaling for heavy tails.  
7. **Categorical handling** — reduce cardinality (group rare levels), choose encoding (one‑hot, ordinal, target encoding) based on model and leakage risk.  
8. **Feature engineering & validation** — create derived features, validate with holdout to avoid leakage.  
9. **Text/image preprocessing** — OCR for PDFs, remove headers/footers, normalize whitespace, remove PII, language detection. For images: resize, normalize, filter low quality.  
10. **Data lineage & governance** — track source, transformations, and consent; store provenance for audit.  
**Example:** For a claims dataset I profiled missingness, found 12% missing diagnosis codes, imputed using most frequent within provider group, and flagged imputed rows for downstream model monitoring.

---

# **Question)** How did you connect to SQL Server?  
**Answer)**  
**Typical production approach:** use a secure driver (ODBC/pyodbc) or an ORM (SQLAlchemy) with credentials stored in a secrets manager (Key Vault/Secrets Manager). Use parameterized queries and connection pooling.

**Example (pyodbc + pandas):**
```python
import pyodbc
import pandas as pd
from sqlalchemy import create_engine

# pyodbc direct
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=sqlserver.example.com;DATABASE=mydb;UID=myuser;PWD=secret'
)
df = pd.read_sql("SELECT id, age, diagnosis FROM dbo.patients WHERE active=1", conn)

# SQLAlchemy engine (preferred for pooling)
engine = create_engine("mssql+pyodbc://myuser:secret@sqlserver.example.com/mydb?driver=ODBC+Driver+17+for+SQL+Server")
df2 = pd.read_sql_table('patients', engine, schema='dbo', columns=['id','age','diagnosis'])
```

**Operational notes:** use least‑privilege DB accounts, network restrictions (VNet/Private Endpoint), and rotate credentials.

---

# **Question)** One hot encoding with sample code snippet? Why Label encoding does not work in this case?  
**Answer)**  
**One‑Hot Encoding (why & how):** converts a nominal categorical column into binary indicator columns — avoids introducing artificial order.

**Code example (scikit‑learn / pandas):**
```python
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

df = pd.DataFrame({'Color': ['Red','Blue','Green','Red']})
ohe = OneHotEncoder(sparse=False, handle_unknown='ignore')
encoded = ohe.fit_transform(df[['Color']])
cols = ohe.get_feature_names_out(['Color'])
df_ohe = pd.DataFrame(encoded, columns=cols)
print(df_ohe)
```

**Why Label Encoding can fail:** `LabelEncoder` maps categories to integers (e.g., Red→0, Blue→1, Green→2). Many models (linear models, distance‑based models) will interpret those integers as ordinal, implying relationships that do not exist (e.g., Green > Blue). This can bias coefficients and distances. Label encoding is acceptable when: (a) the feature is truly ordinal, or (b) using tree‑based models where integer labels are treated as categories (but even then one‑hot or target encoding is often safer).

**When to prefer alternatives:** For high‑cardinality categorical features consider target encoding, hashing trick, or embedding layers (for DL).

---

# **Question)** ML and DL difference?  
**Answer)**  
**High‑level differences:**  
- **Feature engineering:** ML often requires manual feature engineering (domain features, aggregations). DL learns hierarchical features automatically from raw inputs.  
- **Data scale:** ML works well with small to medium datasets; DL typically needs large datasets to generalize.  
- **Model complexity & compute:** DL models (deep neural nets) are compute‑intensive and benefit from GPUs/TPUs; classical ML (tree ensembles, SVMs) is lighter.  
- **Interpretability:** ML models (linear models, trees) are generally easier to interpret; DL models are more opaque (though explainability tools exist).  
- **Use cases:** ML for tabular data, rule‑based problems; DL for images, audio, text, and complex pattern extraction.

**Example:** For tabular credit scoring, a gradient boosting model (XGBoost) often outperforms a generic deep net unless you have massive data and specialized architectures. For image classification, CNNs (DL) are the standard.

---

# **Question)** What is Vanishing gradient?  
**Answer)**  
**Definition:** Vanishing gradient is a training problem in deep neural networks where gradients propagated back through many layers shrink toward zero. As a result, early layers receive negligible updates and the network fails to learn long‑range dependencies.

**Why it happens:** Activation functions like sigmoid/tanh squash inputs into small ranges; repeated multiplication of derivatives (<1) across many layers causes exponential decay of gradients.

**Consequences:** slow or stalled learning in lower layers, poor convergence, inability to learn long‑term dependencies (notably in vanilla RNNs).

**Mitigations:**  
- Use ReLU or its variants (Leaky ReLU, ELU) which have derivatives near 1 for positive inputs.  
- Use architectures with skip/residual connections (ResNet) to provide direct gradient paths.  
- Use gated RNNs (LSTM/GRU) for sequence tasks.  
- Apply batch normalization to stabilize activations.  
- Use careful weight initialization (He/Xavier).

**Example:** Replacing sigmoid with ReLU and adding residual blocks fixed training stagnation in a deep CNN I worked on.

---

# **Question)** Activation functions in ML?  
**Answer)**  
**Common activations and use cases:**  
- **Sigmoid:** \( \sigma(x)=\frac{1}{1+e^{-x}} \). Used in binary output layers to produce probabilities. Prone to vanishing gradients in deep nets.  
- **Tanh:** \( \tanh(x) \). Zero‑centered but still susceptible to vanishing gradients.  
- **ReLU:** \( \text{ReLU}(x)=\max(0,x) \). Simple, efficient, reduces vanishing gradient for positive activations. Default for many hidden layers.  
- **Leaky ReLU / Parametric ReLU:** allow small negative slope to avoid “dying ReLU” units.  
- **ELU / SELU:** smoother variants that can improve convergence.  
- **Softmax:** converts logits to a categorical probability distribution for multi‑class classification.  
- **Swish / GELU:** newer activations used in transformer architectures (GELU in BERT/GPT).

**Selection guidance:** ReLU family for hidden layers; softmax for multi‑class outputs; sigmoid for single‑node binary outputs (with BCE loss).

---

# **Question)** For you to start building a classification model based on pdf shared, what other questions you'll have?  
**Answer)**  
**Essential clarifying questions (operational & modeling):**  
1. **Target definition:** What is the exact label? Is it binary or multi‑class? How is it defined in the PDF?  
2. **Data format & volume:** Are PDFs structured (tables) or unstructured text? How many documents and average length?  
3. **Label availability:** Are labels provided per document, per section, or do we need human annotation? What is label quality?  
4. **OCR needs:** Are PDFs scanned images requiring OCR? What OCR accuracy is acceptable?  
5. **PII & compliance:** Does the data contain PHI/PII? Any regulatory constraints (HIPAA, GDPR)?  
6. **Evaluation metric & business objective:** Precision vs recall tradeoffs, cost of false positives/negatives.  
7. **Latency & deployment constraints:** Real‑time vs batch inference; on‑prem vs cloud; model size limits.  
8. **Ground truth & edge cases:** Examples of ambiguous cases and how to handle them.  
9. **Acceptance criteria:** Minimum performance thresholds and monitoring requirements.  
10. **Access & security:** Who can access the data and model outputs? Are there access controls?  

**Why these matter:** They determine preprocessing (OCR, chunking), labeling strategy, model architecture (transformer vs classical), and evaluation.

---

# **Question)** Have you built any chat bot or agent in GEN AI project? What is the architecture or provider or Engine?  
**Answer)**  
**Yes — typical production architecture I implemented:**  
- **Ingestion layer:** connectors for SharePoint/ShareFile/SQL/CSV/PDF; OCR for scanned docs.  
- **Preprocessing:** cleaning, semantic chunking, metadata extraction, PII masking.  
- **Embeddings & vector store:** generate embeddings (OpenAI/embedding models or SBERT) and index in FAISS/Pinecone/Milvus.  
- **Retriever:** dense retriever (embedding similarity) with optional BM25 hybrid.  
- **Reranker:** cross‑encoder or small LLM to rerank top candidates.  
- **LLM / Reasoning:** OpenAI GPT‑4 / Azure OpenAI / Anthropic / Google Gemini as the generation engine. Use prompt templates and system instructions.  
- **Agent layer:** LangChain agents or custom orchestrator to call tools (calendar, ticketing, DB queries) and enforce policies.  
- **Frontend & integration:** web UI, Teams/Slack bot, or API gateway.  
- **Monitoring & safety:** logging, hallucination checks, human‑in‑the‑loop for high‑risk responses.

**Providers/engines used:** Azure OpenAI (GPT‑4), OpenAI APIs, Anthropic Claude, and on‑prem Llama variants for sensitive data.

**Example:** A support assistant that retrieves KB articles, synthesizes answers with citations, and can open a support ticket via an agent tool.

---

# **Question)** Was the data directly given to LLM or was there any cleanup done before sending it to LLM?  
**Answer)**  
**Never send raw data directly.** I always perform cleanup and transformation before passing context to an LLM: remove boilerplate, redact PII, chunk text to fit token limits, deduplicate similar chunks, and attach metadata (source, date). I also filter low‑quality or irrelevant content and normalize encodings. For sensitive workflows I apply additional anonymization and differential privacy techniques where required.

**Example:** For a PDF corpus, I removed headers/footers, normalized whitespace, split into 500‑token overlapping chunks, and removed personally identifiable fields before embedding and retrieval.

---

# **Question)** How do you ensure data is not leaked?  
**Answer)**  
**Technical and process controls:**  
- **Access control:** least‑privilege IAM roles, RBAC, and network isolation (VNet, private endpoints).  
- **Data minimization:** only send necessary context to LLM; redact or mask PII.  
- **Encryption:** TLS in transit, KMS‑managed encryption at rest.  
- **Prompt sanitization:** strip secrets and credentials from user inputs before logging or sending to external APIs.  
- **On‑prem or private endpoints:** use private LLM endpoints or on‑prem models for highly sensitive data.  
- **Audit & logging:** immutable logs of data access and model calls; alert on anomalous access.  
- **Legal & contractual:** DPA and vendor agreements that prohibit model training on customer data if required.  
- **Human review & gating:** human‑in‑the‑loop for high‑risk outputs and periodic red team testing.

**Operational example:** For a healthcare bot, we used an on‑prem embedding service and a private LLM endpoint; all PII was tokenized and stored separately with strict access controls.

---

# **Question)** For regression problem, what evaluation metric you have used?  
**Answer)**  
**Common metrics and when to use them:**  
- **MSE (Mean Squared Error):** penalizes large errors; useful when large errors are particularly costly.  
- **RMSE (Root MSE):** same units as target; easier to interpret.  
- **MAE (Mean Absolute Error):** robust to outliers; linear penalty.  
- **R² (Coefficient of Determination):** proportion of variance explained; useful for model comparison.  
- **MAPE (Mean Absolute Percentage Error):** interpretable as percentage but unstable near zero.  
**Selection depends on business cost function.** For example, in demand forecasting where large misses are costly, RMSE or weighted MSE may be preferred; for median forecasting, MAE is better.

---

# **Question)** Mean squared error? Find sum of squared error, total sum of square, r2 for a sample data  
**Answer)**  
**Given sample:** \(y = [3, -0.5, 2, 7]\), \(\hat{y} = [2.5, 0.0, 2, 8]\).

**Formulas:**  
- Sum of Squared Errors (SSE): \(\text{SSE}=\sum_i (y_i-\hat{y}_i)^2\).  
- Total Sum of Squares (TSS): \(\text{TSS}=\sum_i (y_i-\bar{y})^2\) where \(\bar{y}\) is mean of \(y\).  
- \(R^2 = 1 - \dfrac{\text{SSE}}{\text{TSS}}\).

**Computation (Python):**
```python
import numpy as np
y = np.array([3, -0.5, 2, 7])
y_hat = np.array([2.5, 0.0, 2, 8])

sse = np.sum((y - y_hat)**2)
tss = np.sum((y - np.mean(y))**2)
r2 = 1 - sse/tss

print("SSE:", sse, "TSS:", tss, "R2:", r2)
```
**Numeric result:**  
- \(\text{SSE} = 0.5\)  
- \(\text{TSS} \approx 29.1875\)  
- \(R^2 \approx 0.9828\)  

**Interpretation:** Model explains ~98.3% of variance on this tiny sample (note: small sample sizes can be misleading).

---

# **Question)** Multi‑agentic framework experience?  
**Answer)**  
**Experience summary:** I’ve designed and run multi‑agent systems where each agent has a focused responsibility and agents coordinate via an orchestrator or message bus. Typical agents include: Retriever, Reranker, Reasoner (LLM), Tool Executor (APIs, DB), Validator (policy/compliance), and Monitor.

**Key design patterns:**  
- **Separation of concerns:** each agent is small and testable.  
- **Tool interfaces:** agents call external tools via well‑defined APIs; tool calls are logged and idempotent.  
- **Orchestration:** use a workflow engine (Temporal, Airflow, or custom orchestrator) to manage retries, timeouts, and state.  
- **Safety & gating:** validator agent checks outputs for hallucination/PII before finalizing.  
- **Observability:** per‑agent telemetry, traces, and audit logs.

**Example:** A financial assistant where: Retriever finds relevant policy docs; Validator checks for regulatory constraints; Reasoner drafts an answer; Action agent files a report if requested. This modularity allowed independent scaling and easier compliance audits.

---

# **Question)** Chunking and its types?  
**Answer)**  
**Definition:** Chunking is splitting large documents into smaller pieces (chunks) suitable for embedding, retrieval, and LLM context windows.

**Types & tradeoffs:**  
1. **Fixed‑size chunking:** split by tokens/characters (e.g., 500 tokens). Simple but may cut sentences.  
2. **Overlapping chunking:** fixed chunks with overlap (e.g., 500 tokens with 50 token overlap) to preserve context across boundaries. Good for continuity.  
3. **Semantic chunking:** split by logical units (paragraphs, sections, headings) using NLP heuristics or structural cues. Preserves meaning and reduces fragmentation.  
4. **Recursive chunking / hierarchical:** split large documents into sections, then paragraphs, then sentences; useful for multi‑granularity retrieval.  
5. **Adaptive chunking:** use heuristics or models to create chunks that maximize semantic coherence (e.g., split where topic changes).  
6. **Record/row chunking:** for tabular data, chunk by record or grouped records (e.g., all rows for an invoice).

**Practical rules:**  
- Keep chunk token size within model limits (account for prompt + context).  
- Use overlap when context continuity matters.  
- Attach metadata (source, page, offsets) to each chunk for provenance.  
- Evaluate retrieval quality and adjust chunk size/overlap accordingly.

**Example:** For a 200‑page manual I used semantic chunking by section headings, limited chunks to ~700 tokens with 100 token overlap, and stored page numbers for citation.

# Question: Agentic AI experience?  
**Answer:**  
**Definition and role:** Agentic AI refers to systems composed of one or more autonomous agents that can perceive, reason, plan, act, and coordinate to accomplish goals. Agents can call tools, query knowledge stores, execute code, and interact with external systems. In production, agentic systems are used for orchestration, multi‑step workflows, and complex decision making.

**My experience:** I have designed and deployed multi‑agent pipelines for document understanding and automated support. Typical architecture I built included: **ingestion → preprocessing → retriever agent → reasoning agent → tool agent → orchestrator**. Each agent had a clear responsibility. The retriever agent fetched relevant documents from a vector store. The reasoning agent used an LLM to synthesize answers. The tool agent executed actions such as database lookups, API calls, or code execution. An orchestration layer handled retries, timeouts, and routing.

**Example workflow:** Customer support automation  
- **Agent 1 (Retriever):** Given a user query, retrieves top N chunks from vector DB using embeddings and cosine similarity.  
- **Agent 2 (Validator):** Checks retrieved chunks for freshness and compliance rules, filters out PII.  
- **Agent 3 (Responder):** Uses an LLM to generate a draft response with citations.  
- **Agent 4 (Action):** If the user asks to schedule or update a ticket, this agent calls the ticketing API and returns confirmation.  
**Benefits realized:** reduced average handle time, auditable tool calls, and modular testing of each agent.

**Design considerations:** clear tool interfaces, idempotency for actions, secure credential management, and observability for each agent’s decisions.

---

### Encoding, Binning, and Feature Engineering

# Question: Difference between one hot encoding, label encoding and ordinal encoding?  
**Answer:**  
**One‑Hot Encoding**  
- **What:** Converts a categorical feature with K categories into K binary features where exactly one is 1.  
- **When to use:** Nominal categories with no order.  
- **Pros:** No implied ordering, works well with linear models and tree models.  
- **Cons:** High dimensionality when K is large.  
**Code example:**
```python
from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder(sparse=False, handle_unknown='ignore')
X_ohe = enc.fit_transform(df[['color']])
```

**Label Encoding**  
- **What:** Maps categories to integer labels 0..K-1.  
- **When to use:** Ordinal features or tree models where integer mapping is acceptable.  
- **Pros:** Compact representation.  
- **Cons:** Implies ordinal relationship that may mislead linear models.  
**Code example:**
```python
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['color_label'] = le.fit_transform(df['color'])
```

**Ordinal Encoding**  
- **What:** Maps categories to integers according to a defined order.  
- **When to use:** When categories have a natural order such as ['low','medium','high'].  
- **Pros:** Preserves order information.  
- **Cons:** Requires domain knowledge to define ordering; still may not be linear in effect.  
**Code example:**
```python
from sklearn.preprocessing import OrdinalEncoder
ord_enc = OrdinalEncoder(categories=[['low','medium','high']])
df['size_ord'] = ord_enc.fit_transform(df[['size']])
```

**Guideline:** Use one‑hot for nominal variables, ordinal encoding for ordered categories, and label encoding only when model choice and data semantics justify it.

# Question: What is Binning?  
**Answer:**  
**Definition:** Binning transforms a continuous variable into discrete intervals or buckets. Binning reduces noise, handles nonlinearity, and can improve interpretability.

**Types:**  
- **Equal‑width binning:** Each bin spans the same numeric range.  
- **Equal‑frequency binning (quantile):** Each bin contains roughly the same number of samples.  
- **Custom/domain binning:** Bins defined by domain thresholds.  
- **Adaptive binning:** Uses decision trees or clustering to find splits that maximize predictive power.

**Example:** Converting age into buckets:
```python
bins = [0, 18, 35, 50, 100]
labels = ['child','young_adult','adult','senior']
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels)
```

**When to use:** When relationships are non‑linear, to reduce effect of outliers, or to create interpretable features for business stakeholders.

---

### Model Selection, Hyperparameter Tuning, and Fixing Code

# Question: How did you select Hyper parameter in XGBoost? Which method you used to select Hyper parameter?  
**Answer:**  
**Approach:** I use a staged, pragmatic approach combining domain intuition, automated search, and validation.

**Steps:**  
1. **Baseline model:** Train with default parameters to get baseline metrics.  
2. **Important hyperparameters to tune:** `n_estimators`, `max_depth`, `learning_rate`, `subsample`, `colsample_bytree`, `min_child_weight`, `gamma`, `reg_alpha`, `reg_lambda`.  
3. **Search strategy:**  
   - **Randomized search** for broad exploration of parameter space.  
   - **Bayesian optimization** (Optuna or Hyperopt) for efficient search focusing on promising regions.  
   - **Grid search** only for fine tuning around the best region found.  
4. **Validation:** Use nested cross‑validation or time‑series split when data is temporal. Monitor metrics like AUC for classification or RMSE for regression. Use early stopping on a validation set to prevent overfitting.  
5. **Practical constraints:** Limit search budget, prefer simpler models if performance is similar, and check feature importance and SHAP values for interpretability.

**Example with Optuna:**
```python
import optuna
def objective(trial):
    params = {
        'max_depth': trial.suggest_int('max_depth', 3, 10),
        'learning_rate': trial.suggest_loguniform('learning_rate', 0.01, 0.3),
        'subsample': trial.suggest_uniform('subsample', 0.5, 1.0),
        'colsample_bytree': trial.suggest_uniform('colsample_bytree', 0.5, 1.0),
        'min_child_weight': trial.suggest_int('min_child_weight', 1, 10)
    }
    model = xgb.XGBClassifier(**params, n_estimators=100, use_label_encoder=False, eval_metric='logloss')
    model.fit(X_train, y_train, eval_set=[(X_val, y_val)], early_stopping_rounds=20, verbose=False)
    return roc_auc_score(y_val, model.predict_proba(X_val)[:,1])
study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=50)
```

**Why Bayesian/Optuna:** More sample‑efficient than grid search and can handle conditional parameters.


### Retrieval, Vector Search, Post‑Retrieval Strategies, and Hallucination

# Question: Talk about retrieval methods?  
**Answer:**  
**Retrieval approaches:**  
- **Sparse retrieval:** Traditional inverted index methods such as BM25 and TF‑IDF. Fast and interpretable for keyword matching.  
- **Dense retrieval:** Embedding based retrieval using vector similarity search. Use sentence embeddings from models like SBERT or transformer encoders. Better for semantic matches.  
- **Hybrid retrieval:** Combine sparse and dense scores to leverage exact keyword matches and semantic relevance.  
- **Reranking:** Retrieve candidates with a fast method then rerank with a cross‑encoder or LLM for higher precision.

**Example pipeline:** For a knowledge base search, I use a dense retriever to get top 100 candidates, then a cross‑encoder to rerank top 10, and finally apply a filter for recency and compliance.

# Question: Post retrieval strategies?  
**Answer:**  
**Common strategies:**  
- **Reranking:** Use a cross‑encoder or LLM to score and reorder retrieved chunks.  
- **Filtering:** Remove stale or low‑quality documents, filter by metadata such as date, source, or trust score.  
- **Aggregation:** Combine multiple chunks into a single context using heuristics such as highest cumulative similarity or topic coherence.  
- **Citation and provenance:** Attach source identifiers and confidence scores to responses.  
- **Answer synthesis:** Use a synthesis prompt that instructs the LLM to cite sources and avoid hallucination.

**Example:** After retrieving top 20 chunks, I rerank with a cross‑encoder, drop chunks older than 2 years for time‑sensitive queries, and then pass the top 3 chunks to the LLM with an instruction to quote and cite.

# Question: How to avoid Hallucination?  
**Answer:**  
**Techniques to reduce hallucination:**  
- **Retrieval Augmented Generation (RAG):** Provide the LLM with relevant, high‑quality context from a trusted source.  
- **Constrain the model:** Use system prompts that require citations and ask the model to respond “I don’t know” when evidence is insufficient.  
- **Rerank and validate:** Use a verifier model or cross‑encoder to check factual consistency between the LLM output and retrieved documents.  
- **Chain of thought control:** Avoid exposing internal chain‑of‑thought to users; instead use structured reasoning steps that reference sources.  
- **Post‑generation verification:** Run fact‑checking modules or rule‑based checks against authoritative databases.  
- **Prompt engineering:** Use explicit instructions to cite sources and limit generation to the provided context.

**Operational controls:** Logging, human‑in‑the‑loop review for high‑risk outputs, and conservative thresholds for automated actions.

# Question: Cosine similarity search?  
**Answer:**  
**Definition:** Cosine similarity measures the cosine of the angle between two vectors. For embeddings, it quantifies semantic similarity independent of vector magnitude.

**Formula:**  
\[
\text{cosine}(u,v) = \frac{u \cdot v}{\|u\|\|v\|}
\]

**Usage:** Normalize embeddings and compute dot product or use library functions. Works well for semantic retrieval.

**Example with FAISS:**  
- Store normalized embeddings in FAISS index with inner product metric.  
- Query by computing embedding of the query and retrieving top K by highest inner product which equals cosine similarity when vectors are normalized.

---

### Cross‑Validation, LangChain, Vector DBs, Chunking, and Integration

# Question: Cross validations in ML?  
**Answer:**  
**Types and when to use:**  
- **K‑Fold CV:** Standard for IID data. Split into K folds, rotate training/validation.  
- **Stratified K‑Fold:** Preserve class distribution for classification tasks.  
- **TimeSeriesSplit:** For temporal data, preserves order and prevents lookahead bias.  
- **Nested CV:** For unbiased hyperparameter selection and model evaluation.  
- **Leave‑One‑Out:** For very small datasets.

**Practical notes:** Use stratification for imbalanced classes, use time‑aware splits for forecasting, and prefer nested CV when tuning hyperparameters to avoid optimistic bias.

# Question: Langchain experience? Which types of LLM models?  
**Answer:**  
**Experience:** I used LangChain to build RAG pipelines, agentic workflows, and tool‑enabled assistants. I implemented retrievers, prompt templates, chains for multi‑step reasoning, and custom agents that call external APIs.

**LLM types used:**  
- **Closed API models:** GPT family, Claude, Gemini for high‑quality generation.  
- **Open models:** Llama variants and open weights for on‑premise deployments.  
- **Embedding models:** Sentence transformers and API embeddings for vectorization.

**Integration patterns:** LangChain as orchestration layer, vector DB for retrieval, and custom tool wrappers for external actions.

# Question: What you used for vector db?  
**Answer:**  
I have used **FAISS** for on‑premise high‑performance vector search, **Pinecone** and **Weaviate** for managed services, and **Milvus** for scalable deployments. Choice depends on scale, latency, and operational constraints.

# Question: Chunking experience? What is semantic chunking? How do you decide chunking for Excel/CSV?  
**Answer:**  
**Chunking purpose:** Break large documents into pieces suitable for embedding and retrieval.

**Types:**  
- **Fixed token/character chunking:** Simple and deterministic.  
- **Overlapping chunking:** Adds overlap to preserve context across boundaries.  
- **Semantic chunking:** Split by logical units such as paragraphs, sections, or headings using NLP heuristics. Semantic chunking preserves meaning and reduces fragmentation of concepts.

**Deciding chunking for Excel/CSV:**  
- **Row‑level chunking:** Each row as a chunk when rows are independent records.  
- **Grouped chunking:** Combine related rows into a chunk when context spans multiple rows, for example, invoice line items grouped by invoice ID.  
- **Column selection:** Only include relevant columns in the chunk to reduce noise.  
- **Size constraints:** Ensure chunk token length fits model limits, typically 500–1,000 tokens per chunk with overlap if needed.

**Example:** For a sales CSV, create chunks per invoice combining header and line items into one chunk, then embed.

# Question: How are you considering or picking images from a pdf?  
**Answer:**  
**Steps:**  
1. **Extract images:** Use a PDF parser to extract embedded images and their coordinates.  
2. **OCR and metadata:** Run OCR on pages to get captions and surrounding text.  
3. **Relevance scoring:** Score images by proximity to query keywords or by caption similarity using embeddings.  
4. **Filtering:** Remove low resolution or irrelevant images.  
5. **Indexing:** Store image embeddings in vector DB for multimodal retrieval.

**Example:** For a product manual, extract diagrams and associate them with the nearest section heading to enable image retrieval for product troubleshooting queries.

# Question: Types of input sources?  
**Answer:**  
Common sources include: structured databases (SQL), CSV/Excel, JSON APIs, unstructured text (PDFs, Word), web pages, images, audio, video, and enterprise stores such as SharePoint, Confluence, and internal file shares.

# Question: Post retrieval strategies? (covered earlier)  
**Answer:** See reranking, filtering, aggregation, provenance, and synthesis.

# Question: Create a chatbot and integrate it with any cloud like Google Gemini and input is going to be a SharePoint source?  
**Answer:**  
**High‑level plan:**  
1. **Ingestion:** Connect to SharePoint API, crawl documents, extract text and metadata, and store originals in secure storage.  
2. **Preprocessing:** Clean text, remove boilerplate, chunk documents semantically, and remove PII.  
3. **Embeddings:** Generate embeddings for chunks using a chosen embedding model.  
4. **Vector DB:** Index embeddings in a managed vector DB.  
5. **Retriever:** Implement dense retriever with cosine similarity and optional sparse hybrid.  
6. **LLM integration:** Use Google Gemini as the LLM for generation. Build a prompt template that includes retrieved chunks and instructions to cite sources.  
7. **Agent tooling:** Add agents for actions like opening SharePoint links or creating tickets.  
8. **Deployment:** Host the chatbot backend on cloud functions or a container service, expose an API, and integrate with a web UI or Teams.  
9. **Security:** Use OAuth for SharePoint access, encrypt data at rest, and implement access control.  
10. **Monitoring:** Log queries, latency, and user feedback for continuous improvement.

**Operational notes:** Respect SharePoint permissions and ensure the retriever only returns documents the user is authorized to see.

# Question: How will you host an application in cloud instance/platform?  
**Answer:**  
**Options:**  
- **Containers:** Docker + Kubernetes for scalable microservices. Use managed Kubernetes like EKS/GKE/AKS.  
- **Serverless:** Cloud Functions or AWS Lambda for event‑driven components.  
- **PaaS:** App Service or Cloud Run for simpler deployments.  
- **Managed ML infra:** Use managed model endpoints for LLMs or host models on GPU instances.

**Typical deployment:** Containerize the app, push to registry, deploy to Kubernetes with autoscaling, use managed databases and vector DB, configure CI/CD pipeline, and set up monitoring and alerting.

# Question: How do you prioritise multiple events?  
**Answer:**  
**Approach:** Use a scoring function combining urgency, impact, SLA, and resource availability. Implement a priority queue and SLA enforcement. For human tasks, include business rules and escalation policies.

---

### Visualization, Metrics, and Miscellaneous

# Question: Box plot?  

**Answer:**  
**Definition:** A box plot visualizes distribution of a numeric variable showing median, interquartile range, whiskers, and outliers. Useful for comparing distributions across groups.

**Interpretation:** The box spans Q1 to Q3, the line inside is the median, whiskers extend to 1.5 IQR, and points beyond are outliers.

**Example with matplotlib:**
```python
import matplotlib.pyplot as plt
plt.boxplot([group1, group2])
plt.xticks([1,2], ['A','B'])
plt.show()
```

# Question: For regression problem, what evaluation metric you have used?  
**Answer:** Use MSE, RMSE, MAE, and R² depending on business needs. RMSE is interpretable in original units, MAE is robust to outliers, and R² indicates variance explained.

### ML and Deep Learning Experience, Models, and Architectures  
# **Question)** ML, DL experience?  
**Answer)**  
I have 8+ years building production ML systems and 5+ years deploying deep‑learning solutions. **ML** work focused on tabular problems (credit scoring, churn, demand forecasting) using feature engineering + tree ensembles (XGBoost/LightGBM/CatBoost), linear models, and classical pipelines (scaling, imputation, target encoding, cross‑validation, explainability with SHAP). **DL** work covered NLP (transformer fine‑tuning, RAG), computer vision (CNNs, segmentation), and multimodal systems (text+image). I’ve taken models from prototyping to production: training, hyperparameter tuning (Optuna), CI/CD for models, monitoring (data drift, concept drift), and model governance.

**Example:** For a customer support assistant I built a RAG pipeline using a transformer encoder for embeddings, FAISS for retrieval, and a GPT‑class model for synthesis; for a churn project I used XGBoost with engineered temporal features and SHAP explanations to drive retention campaigns.

---

### Sequence Models, Churn Modeling, and LLM Architectures  
# **Question)** RNN and Churning experience?  
**Answer)**  
I’ve used **RNNs/LSTMs/GRUs** for sequence tasks (time series forecasting, session modeling). For churn prediction I typically prefer **feature‑based ML** (XGBoost) because tabular features + business rules often outperform vanilla RNNs unless you have long raw sequential logs and large data. When sequences matter (e.g., clickstreams), I used **sequence models**:  
- **Approach:** convert user events into time‑ordered sequences, embed categorical events, feed into Bi‑LSTM or Transformer encoder, then combine sequence embedding with static features in a final classifier.  
- **Outcome:** sequence model improved early churn detection by capturing behavioral patterns (e.g., decreasing session length) that aggregated features missed.

**When to use RNN vs Transformer:** RNNs for modest sequence lengths and low compute; Transformers for long‑range dependencies and when parallel training is needed.

# **Question)** Encoder and decoder architecture? Its examples.  
**Answer)**  
- **Encoder‑only:** maps input to embeddings (BERT). Used for classification, retrieval, embeddings.  
- **Decoder‑only:** autoregressive generation (GPT family). Used for free‑form text generation.  
- **Encoder‑decoder (seq2seq):** encoder compresses input, decoder generates output conditioned on encoder (T5, BART). Used for translation, summarization.  
**Example:** BERT (encoder) for classification; GPT (decoder) for chat; T5 (encoder‑decoder) for summarization.

# **Question)** LLM architecture? What is LLM?  
**Answer)**  
- **LLM (Large Language Model):** large transformer‑based neural networks trained on massive text corpora to model language. Architectures are typically stacks of transformer blocks with self‑attention, layer norm, and feed‑forward layers.  
- **Key components:** tokenization, embedding layer, positional encodings, multi‑head self‑attention, feed‑forward networks, residual connections, and output head (softmax over vocabulary).  
- **Context window:** the maximum token length the model can attend to (e.g., 8k, 32k tokens). This determines how much context you can pass in a single prompt.

# **Question)** Transformer architecture?  
**Answer)**  
Transformers use **self‑attention** to compute contextualized representations for each token in parallel. Each block has multi‑head attention + feed‑forward network + residual connections + layer normalization. Stacking many blocks yields deep contextual models. Transformers replaced RNNs for most NLP tasks due to parallelism and better long‑range modeling.

---

### RAG, Retrieval, Embeddings, Chunking, and When to Use RAG  
# **Question)** Why need RAG model? How do you decide whether to use RAG or LLM? RAG pipeline components?  
**Answer)**  
**Why RAG:** RAG (Retrieval‑Augmented Generation) combines a retrieval step with an LLM to ground responses in external knowledge. It reduces hallucination, allows up‑to‑date answers, and keeps sensitive or proprietary knowledge out of the LLM’s training data. Use RAG when you need **factual, auditable, or domain‑specific** answers from a large corpus.

**Decision rule (RAG vs pure LLM):**  
- Use **RAG** when: answers must cite sources, knowledge is proprietary or frequently changing, or hallucination risk is unacceptable.  
- Use **pure LLM** when: conversational creativity is primary, or the knowledge is general and static and you can tolerate some hallucination.

**RAG pipeline components:**  
1. **Ingestion:** extract text (OCR for PDFs), clean, metadata extraction.  
2. **Chunking:** split documents into chunks (semantic/fixed/overlapping).  
3. **Embeddings:** encode chunks into vectors.  
4. **Vector DB / Index:** FAISS, Pinecone, Milvus, Weaviate.  
5. **Retriever:** dense (embedding) ± sparse (BM25) hybrid.  
6. **Reranker:** cross‑encoder or small LLM to reorder top candidates.  
7. **Synthesizer (LLM):** generate answer using retrieved context; include citations.  
8. **Verifier / Validator:** optional fact‑checker or rule engine to reduce hallucination.  
9. **Tooling / Agent:** optional tool calls (DB queries, ticket creation).

# **Question)** Types of chunking? How do you decide chunking? How do you evaluate chunking?  
**Answer)**  
**Types:** fixed‑size, overlapping, semantic (by paragraph/section), recursive/hierarchical, record/row chunking for tabular data, adaptive chunking (topic change detection).  
**Decision factors:** document structure, average chunk token length vs model context window, semantic coherence, and retrieval quality. For structured docs (tables) use record chunking; for manuals use semantic chunking by headings; for scanned PDFs use OCR + semantic chunking.  
**Evaluation:** measure retrieval recall (does the correct chunk appear in top‑K), downstream answer quality (human evaluation or automated metrics), and latency. Iterate chunk size/overlap based on retrieval recall and LLM answer accuracy.

# **Question)** Dimensions of the embeddings? Which embedding model used? Vector DB used?  
**Answer)**  
- **Embedding dimensions** vary by model: common sizes are **768, 1024, 1536, 2048**. Choose based on embedding model (e.g., SBERT variants 768/1024; OpenAI text‑embedding‑3‑small 1536).  
- **Embedding models I used:** OpenAI embeddings, SBERT (all‑miniLM, all‑MPNet), and custom transformer encoders for domain adaptation.  
- **Vector DBs:** FAISS for on‑prem, Pinecone/Weaviate/Milvus for managed solutions. Choice depends on scale, latency, and operational constraints.

# **Question)** Cosine similarity search? Post retrieval strategies? How to avoid hallucination?  
**Answer)**  
- **Cosine similarity:** common metric for semantic similarity; normalize vectors and compute dot product. Implemented in FAISS or vector DBs.  
- **Post retrieval:** rerank with cross‑encoder, filter by metadata (date, source), aggregate top chunks, attach provenance, and run a verifier.  
- **Avoid hallucination:** RAG with high‑quality retrieval, conservative prompts (ask model to say “I don’t know” if no evidence), reranking, and post‑generation verification.

---

### Agentic AI, Multi‑Agent Frameworks, and Governance  
# **Question)** Agentic AI experience? Multi‑agentic framework experience? Agent vs Chatbot? Agentic AI experience?  
**Answer)**  
I’ve built **agentic systems** where multiple specialized agents coordinate: retriever, validator, reasoner, tool executor, and monitor. I used **LangChain agents** and custom orchestrators (Temporal) to manage workflows. Agents are **autonomous components** that can call tools and take actions; a **chatbot** is typically a single conversational interface that may or may not have agentic capabilities. An agent can perform multi‑step tasks (book a meeting, query DB, call APIs) with stateful orchestration; a chatbot may only generate text.

**Design patterns:** idempotent tool calls, explicit tool schemas, action logging, human‑in‑the‑loop gating for risky actions, and per‑agent observability.

**Question)** MCP?  
**Answer)** I interpret **MCP** as **Model Control Plane** (infrastructure for model lifecycle) and also as **Model Certification Process** (governance). In practice:  
- **Model Control Plane:** central service for model registration, versioning, deployment, routing, and telemetry.  
- **Model Certification Process:** governance workflow for validating model performance, fairness, security, and compliance before production.

---

### Engineering, APIs, Serverless, Frameworks, and Deployment  
# **Question)** End to end pipeline experience? How will you host an application in cloud instance/platform? FAST API or Flask experience? Architecture of Django? Have you implemented logging?  
**Answer)**  
**End‑to‑end pipeline:** I design pipelines covering ingestion → preprocessing → feature store/embeddings → training → validation → model registry → deployment → monitoring. I use CI/CD (GitHub Actions/Azure DevOps), containerization (Docker), orchestration (Kubernetes), and monitoring (Prometheus, Grafana, Sentry). For RAG systems I add vector DB, retriever, and LLM endpoint.

**Hosting:** containerize services, push to registry, deploy to managed Kubernetes (EKS/GKE/AKS) or Cloud Run/App Service for simpler apps. Use autoscaling, private networking, secrets manager, and managed DBs. For LLMs use managed endpoints (Azure OpenAI, Vertex AI) or host on GPU instances.

**Frameworks:** I’ve built APIs with **FastAPI** (async, high performance) and **Flask** (simple). I prefer FastAPI for production due to type hints, automatic docs, and async support.

**Django architecture:** MTV (Model‑Template‑View) pattern, ORM for DB, middleware, routing, and pluggable apps. Good for monolithic web apps with admin UI and auth.

**Logging:** structured logging (JSON), correlation IDs, request/response logs (sanitized), model inference logs (inputs, outputs, latency), and alerting for anomalies. Use centralized logging (ELK/Datadog).

---

### Practical Code Snippets and Small Algorithms  
# **Question)** One hot encoding with sample code snippet? Why Label encoding does not work in this case?  
**Answer)**  
```python
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

df = pd.DataFrame({'Color': ['Red','Blue','Green','Red']})
ohe = OneHotEncoder(sparse=False, handle_unknown='ignore')
encoded = ohe.fit_transform(df[['Color']])
cols = ohe.get_feature_names_out(['Color'])
df_ohe = pd.DataFrame(encoded, columns=cols)
print(df_ohe)
```
**Why not LabelEncoder:** LabelEncoder maps categories to integers and introduces an artificial order; one‑hot avoids ordinal assumptions.

---

# **Question)** Decorators examples? Decorators code snippet? Yield and return? Have you implemented loggings?  
**Answer)**  
**Decorator example (timing + logging):**
```python
import time
import logging
logging.basicConfig(level=logging.INFO)

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        logging.info(f"{func.__name__} took {elapsed:.3f}s")
        return result
    return wrapper

@timeit
def compute(n):
    s = sum(range(n))
    return s

compute(1000000)
```
**Yield vs return:** `return` exits a function and returns a value; `yield` makes a function a generator that produces a sequence of values lazily. Use `yield` for streaming large datasets.

**Logging:** use structured logs, redact PII, include correlation IDs, and ship to centralized systems.

---

# **Question)** What is an API? What is Lambda? What is its alternative?  
**Answer)**  
- **API:** Application Programming Interface — a contract that allows systems to communicate (HTTP endpoints, gRPC).  
- **Lambda:** AWS Lambda — serverless function execution. Alternatives: Google Cloud Functions, Azure Functions, or containerized microservices on Cloud Run/Kubernetes for long‑running or stateful workloads.

---

**Question)** Decorators code snippet? (Provided above)

# **Question)** How do you create random numbers in Python? Create a list of random numbers where the length is 10? Can you identify prime numbers in a list?  
**Answer)**  
```python
import random

# list of 10 random floats between 0 and 1
rand_list = [random.random() for _ in range(10)]

# list of 10 random integers between 1 and 100
rand_ints = [random.randint(1,100) for _ in range(10)]
```

**Prime detection in a list:**
```python
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    r = int(math.sqrt(n))
    for i in range(3, r+1, 2):
        if n % i == 0:
            return False
    return True

nums = [2,3,4,15,17,19,20]
primes = [x for x in nums if is_prime(x)]
print(primes)  # [2,3,17,19]
```

# **Question)** Pick the count of 2 numbers in a list which equates to 9? Wrap it in a class (two-sum).  
**Answer)**  
```python
class TwoSumFinder:
    def __init__(self, nums):
        self.nums = nums

    def find_pairs(self, target):
        seen = {}
        pairs = []
        for i, num in enumerate(self.nums):
            complement = target - num
            if complement in seen:
                pairs.append((complement, num))
            seen[num] = i
        return pairs

# example
finder = TwoSumFinder([2,7,11,15,1,8])
print(finder.find_pairs(9))  # [(2,7), (1,8)]
```

---

### Hyperparameters, Evaluation, Metrics, Temperature, Top‑p, and Safety  

# **Question)** How did you select Hyper parameter in XGBoost? Which method you used to select Hyper parameter?  
**Answer)**  
I use a staged approach: baseline → random search → Bayesian optimization (Optuna) → fine grid around best region → early stopping with validation. Use nested CV for robust estimates and time‑aware splits for temporal data. Monitor business metric (AUC, RMSE) and complexity (overfitting).

# **Question)** For regression problem, what evaluation metric you have used? Mean squared error? Compute SSE/TSS/R² (example earlier).  
**Answer)**  
Use **RMSE** for interpretability, **MAE** for robustness, **R²** for variance explained. Example computation for SSE/TSS/R² provided earlier: SSE=0.5, TSS≈29.1875, R²≈0.9828.

# **Question)** Temperature and Top p usage?  
**Answer)**  
- **Temperature:** controls randomness; higher values (e.g., 0.8–1.0) produce more diverse outputs; lower (0–0.3) produce deterministic outputs.  
- **Top‑p (nucleus sampling):** sample from smallest set of tokens whose cumulative probability ≥ p (e.g., 0.9). Use top‑p to control diversity while avoiding low‑probability tokens. Combine with temperature for fine control. For factual answers use low temperature and conservative top‑p.

# **Question)** Prompt injection? Guardrail? How to avoid hallucination?  
**Answer)**  
- **Prompt injection:** malicious input that manipulates model behavior. Mitigate by sanitizing inputs, using system prompts that enforce policies, and not executing arbitrary instructions from user content.  
- **Guardrails:** policy layers, validators, and tool gating that check outputs for PII, unsafe actions, or policy violations. Use retrieval grounding, reranking, and human review for high‑risk tasks.

---

### Miscellaneous: GPT vs LLAMA, Versions, Context Window, Embedding/LLM Architecture  

# **Question)** What is the LLM used? LLAMA version? Difference between GPT and LLAMA models? Open source vs proprietary? Context window of the model is? LLM and Embedding architecture?  
**Answer)**  
- **LLMs used:** GPT‑family (OpenAI/Azure), Anthropic Claude, Google Gemini, and open models like LLaMA (Meta) and Llama‑2/3 variants. I’ve used Llama‑2 for on‑prem experiments and Llama‑3 where available.  
- **GPT vs LLaMA:** GPT (OpenAI) models are proprietary API offerings with managed endpoints and often larger context windows and safety layers. LLaMA is an open‑weight family (Meta) enabling on‑prem deployment and fine‑tuning; licensing and operational tradeoffs apply. Open‑source models give control and privacy; proprietary models often give better out‑of‑the‑box performance and managed infra.  
- **Context window:** varies by model: common sizes are 2k, 8k, 32k, and up to 1M tokens for specialized models. Choose model based on required context.  
- **Embedding + LLM architecture:** embeddings are produced by encoder models (sentence transformers or embedding APIs) into fixed‑dim vectors; LLMs are decoder or encoder‑decoder transformers used for generation. In RAG, embeddings feed the retriever; the LLM consumes retrieved text as context.

---