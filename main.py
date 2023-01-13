from fastapi import FastAPI, Request
from natasha import (
    Segmenter,
    MorphVocab,
    PER,
    NamesExtractor,
    NewsNERTagger,
    NewsEmbedding,
    Doc
)
from pydantic import BaseModel, EmailStr


app = FastAPI()

class Text(BaseModel):
    txt: str
@app.post("/")
async def read_main(txt: Text):

    text = txt.txt
    emb = NewsEmbedding()
    segmenter = Segmenter()
    morph_vocab = MorphVocab()
    ner_tagger = NewsNERTagger(emb)
    names_extractor = NamesExtractor(morph_vocab)

    doc = Doc(text)

    doc.segment(segmenter)
    doc.tag_ner(ner_tagger)

    for span in doc.spans:
        span.normalize(morph_vocab)
    {_.text: _.normal for _ in doc.spans}

    for span in doc.spans:
        if span.type == PER:
            span.extract_fact(names_extractor)

    return {_.normal: _.fact.as_dict for _ in doc.spans if _.fact}