from fastapi import FastAPI
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
async def read_main():
    emb = NewsEmbedding()
    segmenter = Segmenter()
    morph_vocab = MorphVocab()
    ner_tagger = NewsNERTagger(emb)
    names_extractor = NamesExtractor(morph_vocab)

    text = 'Добрый день, Галина Петровна! Прошу выполнить заявку Прокина Николая Владимировича от 31.05.2020 и предоставить необходимые доступы следующим сотрудникам: Бирякову Алексею Александровичу, Носовой Анне Сергеевне. Спасибо.'

    doc = Doc(text)

    doc.segment(segmenter)

    doc.tag_ner(ner_tagger)

    for span in doc.spans:
        span.normalize(morph_vocab)
    {_.text: _.normal for _ in doc.spans}

    for span in doc.spans:
        if span.type == PER:
            span.extract_fact(names_extractor)



    return {"msg": {_.normal: _.fact.as_dict for _ in doc.spans if _.fact}}

