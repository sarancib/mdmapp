import pytest
import database
import migrations
import reports.user_report
import load_data

# Fixture for a test databse connection
@pytest.fixture(autouse=False)
def connection():
    print('hello')
    db_name = 'test'
    connection = database.get_connection(db_name)
    migrations.migrate(connection)
    load_data.parseandload(connection)
    yield connection
    # Close the database
    connection.close()
    database.delete_db(db_name)

def test_user_report(connection):

  # Run the report
  ur = reports.user_report.UserReport(connection.cursor())
  data = ur.process()

  # We should have 4 users from the initial population
  assert data == 4


def test_numberalbums_user(connection):

  ur = reports.user_report.UserReport(connection.cursor())
  # Check separately about albumslist for users
  data = ur.countalbumsu()
  assert data == [(1, 10), (2, 10), (4, 10), (6, 10)]

def test_numbertodos_user(connection):

  ur = reports.user_report.UserReport(connection.cursor())
  # Check separately about todoslist for users
  data = ur.counttodosu()
  assert data == [(1, 9), (2, 12), (4, 14), (6, 14)]


