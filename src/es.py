from config import config, populate
from elasticsearch import Elasticsearch, helpers, exceptions
from typing import Dict
import warnings, uuid, logging
warnings.filterwarnings(action='ignore')

INDEX_NAME = config.INDEX_NAME
ES_HOST = config.ES_HOST


es = Elasticsearch(
    hosts=[ES_HOST]
)


class ESKNN():
    ''' This class creates an instance of Elasticsearch
    '''

    def __init__(self) -> None:
        try:
            info = isinstance(es.indices.get_mapping(index=INDEX_NAME), dict)
        except (TypeError, exceptions.NotFoundError) as e:
            self.create_index()

    def populate_index(self):
        for character in config.POPULATION:
            try:
                response = es.index(
                    index=INDEX_NAME,
                    id=uuid.uuid4(),
                    body=character
                )
            except exceptions.ElasticsearchException as e:
                logging.info("could not insert default doc")


    def create_index(self) -> None:
        ''' Create new index\n
            ----------------
            Takes -> None\n
            Returns -> None
        '''
        body = {}

        try:
            result = es.indices.create(
                index=INDEX_NAME,
                body=body,
                ignore=400
            )
            if 'error' in result:
                return 2
            else:
                return 1
        except:
            return 0
        
        self.populate_index()


    def search_document(self, query, field_name) -> Dict:
        ''' Search a index\n
            --------------
            Takes -> fvecs\n
            Returns -> dict from es
        '''
        result = es.search(
            request_timeout=30,
            index=INDEX_NAME,
            body={
                'query': {
                    'match': {
                        field_name: {
                            'query': query
                        }
                    }
                }
            }
        )

        return result

    def insert_document(self, document) -> None:
        ''' Insert new fvecs to the index\n
            -----------------------------
            Takes -> document\n
            Returns -> None
        '''
        rows = [
            {
                '_index': INDEX_NAME,
                '_source': document
            }
        ]

        result = helpers.bulk(
            es,
            rows,
            request_timeout=30
        )

        return result
