import pydocumentdb
import pydocumentdb.document_client as document_client

#Cosmosdb SQL API connection 
uri = 'myUri-port'
key = 'myKey'
client = document_client.DocumentClient(uri, {'masterKey': key})


#database reading
databases = list(client.ReadDatabases())
for database in databases:
    print(database['id'])

database = client.ReadDatabase("dbs/bhasdb")
dict = database
print(dict)

#collection reading
collections = list(client.ReadCollections("dbs/bhasdb"))
for collection in collections:
            print(collection['id'])
mycollection = client.ReadCollection("dbs/bhasdb/colls/bhascol")
print(mycollection)

#document reading
documentlist = list(client.ReadDocuments("dbs/bhasdb/colls/bhascol", {'maxItemCount': 10}))
print (documentlist)
for doc in documentlist:
    print(doc)
    for key , val in doc.items():
        print (key,"-::",val)


#document creation
#new_doc = {'messageId': 9, 'deviceId': 'Win7PC', 'temperature': 39.29, 'humidity': 72.08}
#client.CreateDocument("dbs/bhasdb/colls/bhascol", new_doc)