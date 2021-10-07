from elasticsearch import NotFoundError
import yaml
import glob
import json
import os
import es_client

with open('settings.yml', 'r') as stream:
    settings = yaml.safe_load(stream)

es = es_client.connect()


for path in glob.glob(settings['work_dir'] + '/indices/' + '*.json'):
    f = open(path, 'r')
    index_name = os.path.splitext(os.path.basename(path))[0]

    if es.indices.exists(index=index_name):
        print(f'Index: {index_name} already exists. Delete it to recreate.')
    else:
        print(f'Creating index: {index_name}')
        index_body = json.load(f)
        res = es.indices.create(index=index_name, body=index_body)
        print(res)

for path in glob.glob(settings['work_dir'] + '/ingest-pipelines/' + '*.json'):
    f = open(path, 'r')
    pipeline_name = os.path.splitext(os.path.basename(path))[0]

    try:
        es.ingest.get_pipeline(id=pipeline_name)
        print(f'Updating ingest pipeline: {pipeline_name}')
    except NotFoundError as e:
        print(f'Creating ingest pipeline: {pipeline_name}')

    pipeline_body = json.load(f)
    res = es.ingest.put_pipeline(id=pipeline_name, body=pipeline_body)
    print(res)

for path in glob.glob(settings['work_dir'] + '/transforms/' + '*.json'):
    f = open(path, 'r')
    transform_name = os.path.splitext(os.path.basename(path))[0]

    transform_body = json.load(f)

    try:
        es.transform.get_transform(transform_id=transform_name)
        print(f'Transform: {transform_name} already exists. Delete it to recreate.')
    except NotFoundError as e:
        print(f'Creating transform: {transform_name}')
        res = es.transform.put_transform(transform_id=transform_name, body=transform_body)
        print(res)

for path in glob.glob(settings['work_dir'] + '/ml-jobs/' + '*.json'):
    f = open(path, 'r')
    ml_job_name = os.path.splitext(os.path.basename(path))[0]

    ml_job_body = json.load(f)

    try:
        es.ml.get_jobs(job_id=ml_job_name)
        print(f'ML job: {ml_job_name} already exists. Delete it to recreate.')
    except NotFoundError as e:
        print(f'Creating ml job: {ml_job_name}')
        res = es.ml.put_job(job_id=ml_job_name, body=ml_job_body)
        print(res)

for path in glob.glob(settings['work_dir'] + '/ml-datafeeds/' + '*.json'):
    f = open(path, 'r')
    ml_df_name = os.path.splitext(os.path.basename(path))[0]

    ml_df_body = json.load(f)

    try:
        es.ml.get_datafeeds(datafeed_id=ml_df_name)
        print(f'ML datafeed: {ml_df_name} already exists. Delete it to recreate.')
    except NotFoundError as e:
        print(f'Creating ml datafeed: {ml_df_name}')
        res = es.ml.put_datafeed(datafeed_id=ml_df_name, body=ml_df_body)
        print(res)

