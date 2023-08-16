from elasticsearch import Elasticsearch

# Initialize Elasticsearch instance
#es = Elasticsearch([{'host': 'localhost', 'port': 9200}],verify_certs=False)
es = Elasticsearch("http://localhost:9200")
        

# Ensure Elasticsearch is up
if not es.ping():
    raise ValueError("Elasticsearch is not running!",es.ping())

# Define a document to be indexed
doc = {
    "name": "John Doe",
    "age": 30,
    "job": "Engineer"
}

# CREATE operation
def create_document(index_name, doc_type, doc_id, document):
    res = es.index(index=index_name, doc_type=doc_type, id=doc_id, body=document)
    return res

# READ operation
def get_document(index_name, doc_type, doc_id):
    res = es.get(index=index_name, doc_type=doc_type, id=doc_id)
    return res['_source']

# UPDATE operation
def update_document(index_name, doc_type, doc_id, updated_document):
    res = es.update(index=index_name, doc_type=doc_type, id=doc_id, body={"doc": updated_document})
    return res

# DELETE operation
def delete_document(index_name, doc_type, doc_id):
    res = es.delete(index=index_name, doc_type=doc_type, id=doc_id)
    return res

# Using the CRUD functions
index_name = 'test-index'
doc_type = 'people'
doc_id = 1

# CREATE
print(create_document(index_name, doc_type, doc_id, doc))

# READ
print(get_document(index_name, doc_type, doc_id))

# UPDATE
updated_doc = {"age": 31}
print(update_document(index_name, doc_type, doc_id, updated_doc))
print(get_document(index_name, doc_type, doc_id))

# DELETE
print(delete_document(index_name, doc_type, doc_id))
