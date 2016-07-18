
from pymongo import MongoClient
import json
def main():
    client = MongoClient()
    db = client.testdb["osm"]
    ab = db.aggregate([
        {
            '$group': {
                '_id': '$created.user',
                'count': {
                    '$sum': 1
                    }
            }
        }, {
            '$sort': {
                'count': -1
            }
        }, {
            '$limit' : 1
        }

    ])
    print list(ab)
    for a in ab:
        print(a)



if __name__ == '__main__':
    main()