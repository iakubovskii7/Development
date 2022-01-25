import csv
from peewee import *

db = PostgresqlDatabase(database='test', user='postgres', password='1', host='localhost')


class Coin(Model):
    name = CharField()
    url = TextField()
    price = CharField()

    class Meta:
        database = db



def main():

    db.connect()
    db.create_tables([Coin])

    with open('cmc.csv') as f:
        order = ['name', 'url', 'price']
        reader = csv.DictReader(f, fieldnames=order)

        coins = list(reader)

        # for row in coins:
            # coin = Coin(name=row['name'], url=row['url'], price=row['price'])
            # coin.save()

        with db.atomic():
            # for row in coins:
            #     Coin.create(**row)
            for index in range(0, len(coins), 100):
                Coin.insert_many(coins[index:index+100]).execute()


if __name__ == '__main__':
    main()
