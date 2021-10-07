from elasticsearch import Elasticsearch
import yaml
from ssl import create_default_context


def connect():
    with open('settings.yml', 'r') as stream:
        settings = yaml.safe_load(stream)

    http_auth = (settings['elasticsearch']['user'], settings['elasticsearch']['password'])

    ssl_context = None
    if 'ca_file' in settings['elasticsearch']:
        ssl_context = create_default_context(cafile=settings['elasticsearch']['ca_file'])

    if 'cloud_id' in settings['elasticsearch']:
        return Elasticsearch(
            cloud_id=settings['elasticsearch']['cloud_id'],
            http_auth=http_auth
        )

    else:
        return Elasticsearch(
            hosts=settings['elasticsearch']['hosts'],
            http_auth=http_auth,
            ssl_context=ssl_context
        )

