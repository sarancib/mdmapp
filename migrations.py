from os import listdir
from os.path import isfile, join
from natsort import natsorted

import database

def migrate(connection):
  # Get a sorted list of migration files
  migrations_path = './migrations'
  migration_files = [f for f in listdir(migrations_path) if isfile(join(migrations_path, f))]
  sorted_migration_files = natsorted(migration_files)
  cur = connection.cursor()

  # Apply migrations in order, one at a time
  for migration_file in sorted_migration_files:
    # Open migration file and read it
    f = open(join(migrations_path, migration_file), "r")
    sql = f.read()
    f.close()
    # Run the migration and commit it
    cur.executescript(sql)
    connection.commit()



if __name__ == '__main__':
    connection = database.get_connection()
    migrate(connection)