import logging
from elasticsearch import Elasticsearch

from resources import get_resource


class DB:

    doc_type = 'article'

    def __init__(self, host='localhost', port=9200, index_name='articles'):
        self.es = Elasticsearch([{
            'host': host,
            'port': port
        }])
        self.index_name = index_name
        self.logger = logging.getLogger(__name__)
        self.es.ping()
        self.create_index_if_not_exists()

    def create_index_if_not_exists(self):
        if self.es.indices.exists(self.index_name):
            return
        configuration = {
            "mappings": {
                self.doc_type: get_resource('elasticsearch/index_mapping.json')
            }
        }
        self.es.indices.create(index=self.index_name, body=configuration)
        self.logger.debug("Elasticsearch index %s created." % self.index_name)

    def index_document(self, document, id_):
        self.es.create(
            body=document, id=id_, index=self.index_name,
            doc_type=self.doc_type
        )

    def id_exists(self, id_):
        return self.es.exists(
            id=id_, index=self.index_name,
            doc_type=self.doc_type
        )
