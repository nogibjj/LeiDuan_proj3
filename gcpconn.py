from google.cloud import bigquery
from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file(
'/workspaces/LeiDuan_proj3/focus-cache-367721-77d75212200c.json')

project_id = 'focus-cache-367721'
client = bigquery.Client(credentials= credentials,project=project_id)

query_job = client.query("""
    SELECT ranking, count(id)  FROM `bigquery-public-data.hacker_news.comments`  group by ranking """)

results = query_job.result()
count = 0;
for row in results:
    print(row)
    count+=1
    if count == 100:
        break