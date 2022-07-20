from elasticsearch import Elasticsearch

from schema import Document

es = Elasticsearch('http://host.docker.internal:9200')


def create_doc(document: Document, index):
    return es.index(index=index, body=document.dict())


def search_by_email(email, index):
    doc = es.search(index=index, body={
        "query": {
            "match": {
                "email": email
            }
        }
    })
    return doc
