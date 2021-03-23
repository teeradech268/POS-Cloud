import pymongo
client = pymongo.MongoClient("mongodb+srv://teeradech:0ft5dx8a@cluster0-uwwub.mongodb.net/test?retryWrites=true&w=majority")

def connectdb():
    db = client.get_database("Coffee")
    return db



