
docs = [{"num": 2}, {"num": 1}]
docs.sort(key=lambda doc: doc["num"])
print(docs)