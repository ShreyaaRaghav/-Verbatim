Verbatim - NLP text simplification platform
============================================


> Verbatim is a meaning‑first linguistic clarity platform designed to help users understand complex and sensitive documents without generating new content.

#### Instead of relying on **generative AI** , Verbatim uses **deterministic, rule‑based NLP** to analyze and explain existing language. This makes it suitable for **high‑trust domains** such as healthcare, law, education, and government.

> Verbatim prioritizes accuracy, traceability, and user trust over automation.


What Verbatim Is
--------------------


* A language explanation layer, not a summarizer

* A deterministic NLP system, not a generative model

* A clarity platform for sensitive, real‑world documents


What Verbatim Is Not
--------------------

1. Not a **text generator**

2. Not an **AI summarizer** or paraphraser

3. Not a black‑box** ML system**

4. Not **trained** on user data


Core Capabilities
--------------------

* Analyzes sentence structure and linguistic complexity

* Simplifies vocabulary using controlled, approved mappings

* Explains why a sentence is complex

* Preserves original meaning and critical entities

* Adds accessibility through speech and translation

* Produces predictable, explainable output


High‑Level Architecture
--------------------

Frontend (HTML / CSS / JS)

        ↓
        
Flask Backend (Python API)

        ↓
        
Rule-Based NLP Engine (text simplification NLP logic)

        ↓
        
Cloud Services (Google TTS, Translation)

### All linguistic decisions are made before any cloud services are applied.


Tech Stack
--------------------


#### Backend

* Python 3

* Flask — API and routing

* spaCy — sentence segmentation, POS tagging, dependency parsing, NER

* NLTK — lexical utilities

* textstat — readability metrics

* wordfreq — frequency‑based word difficulty detection


#### Frontend

* HTML — structure

* CSS — styling

* JavaScript — API calls and interaction


#### Cloud Services

* Google Cloud Text‑to‑Speech — accessibility

* Google Cloud Translation — multilingual output

>> Cloud services are used only for output delivery, not for language analysis or generation.


NLP Processing Pipeline
--------------------


* Sentence Segmentation
Breaks documents into logical, readable units.

* Syntactic Analysis
Uses dependency parsing to understand grammatical structure.

* Complexity Detection
Identifies difficult sentences using readability scores and structural cues.

* Controlled Simplification
Replaces only pre‑approved complex vocabulary.

* Explanation Layer
Explains linguistic features such as:

* obligations (“must”, “shall”)

* conditions (“if”, “unless”)

* passive constructions

* dense noun phrases

* Entity Preservation
> Protects names, dates, laws, numbers, and references.

* Output Modes
> Simple Version — cleaner, easier‑to‑read text


### What This Means — sentence‑level explanations for understanding


* Accessibility Features
*  Text‑to‑Speech for read‑aloud support
*  Cloud translation for multilingual access
*  Downloadable outputs
* Shareable document links


Installation
--------------------

pip install spacy nltk textstat wordfreq flask
python -m spacy download en_core_web_sm


Example API Response
--------------------

{
  "original": "The policy shall be implemented pursuant to regulations.",
  "simple": "The policy shall be implemented under regulations.",
  "explanation": "This sentence describes a formal obligation using legal language."
}


Design Principles
--------------------


> Deterministic — same input, same output

> Explainable — rule‑driven transformations

> Meaning‑preserving — no semantic guessing

> Privacy‑respecting — no content generation or training

> Safe for sensitive domains


Intended Use Cases
--------------------


Legal and government documents

Medical forms and patient information

Academic and institutional text

Public‑facing policies and notices


Philosophy
--------------------


####We don’t ask machines to rewrite language.

####We teach them to respect it — and explain it.
