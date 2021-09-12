from kubernetes.client.rest import ApiException
from kubernetes import client, config
from google.cloud import storage
import datetime

config.load_kube_config()
pod_name = "elasticsearch-logging-0"
def elk_logs():
    try:
        api_instance = client.CoreV1Api()
        api_response = api_instance.read_namespaced_pod_log(name=pod_name, namespace='kube-system')
        return api_response
    except ApiException as e:
        return 'Found exception in reading the logs'

f = open("elasticsearch-logging-0.log", "w")
f.write(elk_logs())
f.close()

def upload_blob():
  ct = str(datetime.datetime.now().timestamp())
  """Uploads a file to the bucket."""
  storage_client = storage.Client()
  bucket = storage_client.get_bucket('andrejs-kube1-test-cluster-bucket')
  blob = bucket.blob('elasticsearch-logging-0'+ct)

  blob.upload_from_filename('elasticsearch-logging-0.log')

  print('File {} uploaded to {}.'.format(
      'elasticsearch-logging-0.log',
      'elasticsearch-logging-0'+ct))

upload_blob()
