PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS Toys;
DROP TABLE IF EXISTS Children;

CREATE TABLE 'Children' (
  'ChildId' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  'Name' TEXT NOT NULL,
  'Naughty' BOOLEAN DEFAULT 0
);

-- insert sample data --
INSERT INTO Children VALUES (null, 'Billy', 0);


CREATE TABLE 'Toys' (
  'ToyId' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  'Name' TEXT NOT NULL,
  'Delivered' BOOLEAN DEFAULT 0,
  'Child_Id' INTEGER NOT NULL,
  FOREIGN KEY('Child_Id')
  REFERENCES 'Children'('ChildId')
  ON DELETE cascade
);

-- insert sample data --
INSERT INTO Toys VALUES (null, 'Train', 0, 1)

