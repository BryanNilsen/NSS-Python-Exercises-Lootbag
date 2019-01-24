import unittest
import sys
sys.path.append('../')


# the following imports are for the random string generator
import string
import random

# import the python file to test methods
import lootbag


def string_generator():
  ''' Generates random string to use for testing '''
  return ''.join(random.choice(string.ascii_letters) for letter in range (7))


class lootbagTests(unittest.TestCase):

  def test_getChild(self):
    self.assertIsInstance(lootbag.getChild('Katie'), tuple)

  def test_addToy_existing_child(self):
    self.assertIsInstance(lootbag.addToy('duckie', 'Katie'), int)

  def test_addToy_new_child(self):
    new_child = string_generator()
    self.assertIsInstance(lootbag.addToy('doll', new_child), int)

if __name__=='__main__':
  unittest.main()