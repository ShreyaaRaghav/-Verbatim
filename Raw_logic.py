# simplifier.py

import spacy
import textstat
from wordfreq import zipf_frequency
import pandas as pd

# Load spaCy once 
nlp = spacy.load("en_core_web_sm")


PROTECTED_ENTITIES = {
    "PERSON", "ORG", "GPE", "LAW",
    "DATE", "TIME", "PERCENT",
    "MONEY", "QUANTITY", "ORDINAL",
    "CARDINAL"
}

MODAL_SIMPLIFICATIONS = {
    "shall": "will",
    "may": "can",
    "must": "has to",
    "should": "ought to"
}

LEMMA_SIMPLIFICATIONS = {
    "commence": "start",
    "initiate": "start",
    "terminate": "end",
    "utilize": "use",
    "demonstrate": "show",
    "illustrate": "show",
    "indicate": "show",
    "facilitate": "help",
    "constitute": "form",
    "obtain": "get",
    "retain": "keep",
    "require": "need",
    "endeavor": "try",

    "adherence": "following",
    "compliance": "following",
    "assistance": "help",
    "objective": "goal",
    "methodology": "method",
    "framework": "structure",
    "parameter": "limit",
    "constraint": "limit",
    "aspect": "part",
    "concept": "idea",
    "notion": "idea",

    "substantial": "large",
    "significant": "important",
    "considerable": "large",
    "frequently": "often",
    "initially": "at first",
    "ultimately": "in the end",
    "predominantly": "mostly",
    "numerous": "many",
    "sufficient": "enough",
    "approximately": "about",
    "subsequent": "later",
    "prior": "earlier"
}

PHRASE_SIMPLIFICATIONS = {
    "pursuant to": "under",
    "in accordance with": "under",
    "with respect to": "about",
    "for the purpose of": "to",
    "in the event that": "if",
    "prior to": "before",
    "subsequent to": "after",
    "as a result of": "because of",
    "in order to": "to",
    "on the basis of": "based on",
    "with regard to": "about"
}


def inflect(simple_lemma, token):
    if token.pos_ == "NOUN":
        return simple_lemma + "s" if token.tag_ in ("NNS", "NNPS") else simple_lemma

    if token.pos_ == "VERB":
        if token.tag_ in ("VBD", "VBN"):
            return simple_lemma + "ed"
        if token.tag_ == "VBZ":
            return simple_lemma + "s"
        if token.tag_ == "VBG":
            return simple_lemma + "ing"
        return simple_lemma

    return simple_lemma


def is_passive(sentence):
    return any(tok.dep_ == "auxpass" for tok in sentence)


def difficulty_threshold(sentence):
    grade = textstat.flesch_kincaid_grade(sentence.text)
    return 4.2 if grade > 12 else 4.0


def is_difficult_word(token, sentence):
    if not token.is_alpha:
        return False
    if token.ent_type_ in PROTECTED_ENTITIES:
        return False
    return zipf_frequency(token.text.lower(), "en") < difficulty_threshold(sentence)


def simplify_phrases(text):
    out = text.lower()
    for phrase, simple in PHRASE_SIMPLIFICATIONS.items():
        out = out.replace(phrase, simple)
    return out


def simplify_token(token, sentence):
    lower = token.text.lower()
    lemma = token.lemma_.lower()

    if token.ent_type_ in PROTECTED_ENTITIES:
        return token.text

    if lower in MODAL_SIMPLIFICATIONS:
        return MODAL_SIMPLIFICATIONS[lower]

    if lemma in LEMMA_SIMPLIFICATIONS:
        return inflect(LEMMA_SIMPLIFICATIONS[lemma], token)

    if is_difficult_word(token, sentence):
        return token.lemma_

    return token.text


def simplify_sentence(sentence):
    processed = simplify_phrases(sentence.text)
    doc = nlp(processed)
    sent = list(doc.sents)[0]

    tokens = []
    changed = False

    for tok in sent:
        new = simplify_token(tok, sentence)
        if new != tok.text:
            changed = True
        tokens.append(new)

    return " ".join(tokens), changed


def explain_sentence(sentence):
    explanations = []

    if is_passive(sentence):
        explanations.append(
            "This sentence uses passive voice, focusing on the action rather than who did it."
        )

    difficult = [
        tok.text for tok in sentence if is_difficult_word(tok, sentence)
    ]

    if difficult:
        explanations.append(
            "Some complex words are used: " + ", ".join(sorted(set(difficult)))
        )

    if not explanations:
        explanations.append("This sentence is already clear.")

    return " ".join(explanations)


def cleartext(text):
    doc = nlp(text)
    results = []

    for sent in doc.sents:
        simple, changed = simplify_sentence(sent)

        explanation = (
            explain_sentence(sent)
            if changed or is_passive(sent)
            else "No explanation needed."
        )

        results.append({
            "original": sent.text,
            "simple": simple,
            "explanation": explanation
        })

    return results
