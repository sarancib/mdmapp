import sqlite3
import os

def get_connection(name = 'main'):
  dirname = os.path.dirname(__file__)
  db_file = f'db/{name}.sqlite'
  db_path = os.path.join(dirname, db_file)
  return sqlite3.connect(db_path)

def delete_db(name = 'main'):
  print(f'Deleting database {name}')
  dirname = os.path.dirname(__file__)
  db_file = f'db/{name}.sqlite'
  db_path = os.path.join(dirname, db_file)
  print('lkit l path')
  os.remove(db_path)
  print('tfasakh')