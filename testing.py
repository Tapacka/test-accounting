import unittest
from main import *

class def_testing(unittest.TestCase):
 
  def test_get_doc_owner_name(self):
    
    self.assertEqual(get_doc_owner_name('11-2'), 'Геннадий Покемонов')
    self.assertEqual(get_doc_owner_name('2207 876234'), 'Василий Гупкин')

  def test_delete_doc(self):
    self.assertEqual(delete_doc('10006'), ('10006', True))

  def test_add_new_doc(self):
    self.assertEqual(add_new_doc('11', 'passport', 'Иван', '3'), '3')
      


unittest.main()