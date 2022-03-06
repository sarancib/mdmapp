class UserReport:
  def __init__(self, database_cursor):
    self.cur = database_cursor
  
  def process(self):
    self.cur.execute("SELECT COUNT(1) FROM users")
    return self.cur.fetchone()[0]

  def displaycol(self,tablename):
    self.cur.execute("select * from "+tablename)
    return self.cur.fetchall()

  def countalbumsu(self):
    self.cur.execute("SELECT userId, COUNT(*) FROM albums GROUP BY userId")
    return self.cur.fetchall()

# Showing users with their least unfinished todos
  def counttodosu(self):
    self.cur.execute("SELECT userId, COUNT( CASE WHEN completed = 0 THEN 1 END) unfinished_todos FROM todos GROUP BY userId ORDER BY unfinished_todos")
    return self.cur.fetchall()

 # Calculate the values in a subquery and join
  def countAlbumsTodos(self):
    self.cur.execute("SELECT U.name,totalCount, unfinished_todos  FROM  users U LEFT JOIN ( SELECT userId, COUNT(distinct A.id) totalCount FROM    albums A GROUP   BY userId ) A ON U.id = A.userId LEFT JOIN ( SELECT  userId,  COUNT( CASE WHEN T.completed = 0 THEN 1 END) unfinished_todos FROM todos T GROUP   BY userId ) T ON U.id = T.userId ORDER by totalCount DESC, unfinished_todos ASC")
    return self.cur.fetchall()

