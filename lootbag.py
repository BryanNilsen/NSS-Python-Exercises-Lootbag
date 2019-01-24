import sqlite3
# The sys modules gives us access to whatever is passed in from the command line, in the form of a list called 'argv' so the name of the file you're executing is always index 0. Running `python lootbag.py Suzy` would give us a sys.argv of ['lootbag.py', 'Suzy']
import sys
def printArg():
  print(sys.argv[1])

# full path to lootbag database
lootbag_db = '/Users/mac/Workspace28/python/exercises/cli/lootbag.db'

# EXERCISE INSTRUCTIONS
# You have an acquaintance whose job is to, once a year, deliver presents to the best kids around the world. They have a problem, though. There are so many good boys and girls in the world now, that their old paper accounting systems just don't cut it anymore. They want you to write a program that will let them do the following tasks.



def ls():
  with sqlite3.connect(lootbag_db) as conn:
    cursor = conn.cursor()
  # Produce a list of children currently receiving presents.
    # python lootbag.py ls
    cursor.execute('SELECT * FROM Children')
    children = cursor.fetchall()
    return children




  # List toys in the bag o' loot for a specific child.
    # python lootbag.py ls suzy

  # Specify when a child's toys have been delivered.
    # python lootbag.py delivered suzy


def getChildren():
  # The connect() function opens a connection to an SQLite database. It returns a Connection object that represents the database.
  with sqlite3.connect(lootbag_db) as conn:
    cursor = conn.cursor()

  # To retrieve data after executing a SELECT statement, you can either treat the cursor as an iterator,
    # the following is what we get
    # (1, 'Billy', 0)

    # for row in cursor.execute('SELECT * FROM '):
    #   print(row)

    # Or! call the cursor’s fetchone() method to retrieve a single matching row, or call fetchall() to get a list of the matching rows.

    cursor.execute('SELECT * FROM Children')
    children = cursor.fetchall()
    return children

def getChild(child):
  with sqlite3.connect(lootbag_db) as conn:
    cursor = conn.cursor()

    cursor.execute(f'''SELECT c.* FROM Children c
                      WHERE c.Name like '{child}'
                    ''')

    child = cursor.fetchone()
    print("getChild child: ", child)
    return child


def getToys():
  # The connect() function opens a connection to an SQLite database. It returns a Connection object that represents the database.
  with sqlite3.connect(lootbag_db) as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Toys')
    toys = cursor.fetchall()
    return toys

def addChild(child):
  with sqlite3.connect(lootbag_db) as conn:
    cursor = conn.cursor()

    try:
      # Have to use a specific syntax for inserts and updates, to keep baddies from using injection attacks
      cursor.execute(
        '''
        INSERT INTO Children
        Values(?,?,?)
        ''', (None, child, 0)
      )
      return cursor.lastrowid
    except sqlite3.OperationalError as err:
      print("oops", err)


# Add a toy to the bag o' loot, and label it with the child's name who will receive it. The first argument must be the word add. The second argument is the gift to be delivered. The third argument is the name of the child.
  # python lootbag.py add kite suzy
  # python lootbag.py add baseball michael

def addToy(toy, ChildName):
  with sqlite3.connect(lootbag_db) as conn:
    cursor = conn.cursor()

#  take childname and run query against DB to find match
# if match, return child Id
# if no match, add child to db
    # cursor.execute(f"SELECT c.ChildId FROM Children c WHERE c.Name = '{ChildName}'")
    # childId = cursor.fetchone()
    childId = getChild(ChildName)

    if childId == None:
      childId = addChild(ChildName)
    else:
      childId = childId[0]

    try:
      # Have to use a specific syntax for inserts and updates, to keep baddies from using injection attacks
      cursor.execute(
        '''
        INSERT INTO Toys
        Values(?,?,?,?)
        ''', (None, toy, 0, childId)
      )
      return cursor.lastrowid

    except sqlite3.OperationalError as err:
      print("oops", err)


# Remove a toy from the bag o' loot in case a child's status changes before delivery starts.
    # python lootbag.py remove suzy kite
    # python lootbag.py remove michael baseball



def removeToy(toy, ChildName):
  with sqlite3.connect(lootbag_db) as conn:
    cursor = conn.cursor()

#  take childname and run query against DB to find match
# if match, return child Id
# if no match, add child to db
    # cursor.execute(f"SELECT c.ChildId FROM Children c WHERE c.Name = '{ChildName}'")
    # childId = cursor.fetchone()
    childId = getChild(ChildName)

    if childId == None:
      print("NO SUCH CHILD")
    else:
      childId = childId[0]

    print("CHILD ID", childId)

    try:
      # cursor.execute(f'''
      #   DELETE FROM Toys
      #   WHERE Child_Id={childId} and Name like '{toy}'
      # ''')

      cursor.execute(f'''
        DELETE FROM Toys
        WHERE Child_Id IN (
          SELECT Child_Id FROM Toys
          JOIN Children on Children.ChildId = Toys.Child_Id
          WHERE Children.Name LIKE '{ChildName}'
          ) AND Toys.name LIKE '{toy}'
      ''')

    except sqlite3.OperationalError as err:
      print("oops", err)



if __name__ == "__main__":

# checks for arguments after lootbag.py is run
  if len(sys.argv) > 1:
    if sys.argv[1] == 'getChild':
      getChild(sys.argv[2])
    if sys.argv[1] == 'addChild':
      addChild(sys.argv[2])
    if sys.argv[1] == 'addToy':
      # write something here to check for third argument
      addToy(sys.argv[2], sys.argv[3])
    if sys.argv[1] == 'removeToy':
      removeToy(sys.argv[2], sys.argv[3])

  # returns all children
  # getChildren()

  # returns all toys
  # getToys()
