from replit import db

# store my name in the replit db

db["name"] = "Travis"

print(db['name'])

keys = db.keys()

print(keys)

myAPIKey = os.environ['apiKey']

print(myAPIKey)