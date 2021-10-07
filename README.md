# elasticsearch-asset-manager
Simple python tool to manage Elasticsearch assets such as index or ingest pipeline.

## How to setup

Install dependencies.

```
python -m pip install elasticsearch
```

Then, configure the `settings.yml` file.

- `work_dir`: Specify a directory containing Elasticsearch assets. The directory should contain the following sub directories:
    - `indices`: Index definition JSON files. This tool does not update the existing index.
    - `ingest-pipelines`: Ingest Pipeline definition JSON files. Overwrites existing ingest pipelines.
    - `transforms`: Transform job definition JSON files. This tool does not update the existing job.
    - `ml-jobs`: Machine Learning job definition JSON files. This tool does not update the existing job.
    - `ml-datafeeds`: Machine Learning datafeed definition JSON files. This tool does not update the existing job.

## How to use

Just execute as a python.

```
python elasticsearch_asset_manager.py
```
