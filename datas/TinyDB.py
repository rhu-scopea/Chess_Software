from tinydb import TinyDB, Query

db = TinyDB('db.json')
db.default_table_name = 'fruts'

db.insert({'type': 'apple', 'count': 7})
db.insert({'type': 'peach', 'count': 3})

db.default_table_name = 'meat'
db.insert({'type': 'beef', 'cal': 125})
db.insert({'type': 'chicken', 'cal': 15})
