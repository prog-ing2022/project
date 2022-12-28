from fastapi import FastAPI
from natasha import (
    Segmenter,
    MorphVocab,
    PER,
    NamesExtractor,
    NewsNERTagger,
    NewsEmbedding,
    Doc
)


app = FastAPI()

@app.get("/")
async def read_main(text):
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
