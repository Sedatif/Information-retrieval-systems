import unittest
import forward
import os


#Test cases to test forward index methods
class TestForwardIndex(unittest.TestCase):
  #setUp method
  def setUp(self):
    self.index = forward.forwardIndex()
    #print(self.index)


  #Check indexes
  def test_add_index(self):
    self.assertEqual(self.index.get('test_file1.txt'), ['hi', 'sky'])
    self.assertEqual(self.index.get('test_file2.txt'), ['sky'])
    self.assertEqual(self.index.get('test_file3.txt'), ['eye'])
    self.assertEqual(self.index.get('test_file4.txt'), ['hi'])
    self.assertEqual(self.index.get('test_file5.txt'), ['sky'])


  #Check indexes(ignore case)
  def test_check_case(self):
    test = forward.forwardIndex()
    self.assertEqual(self.index.keys(), test.keys())


  #Check update key-value 
  def test_update_index(self):
    test = forward.forwardIndex()
    test.update([('hello', 'file6')])
    self.assertNotEqual(test.values(), self.index.values())


  #Check correct writing indexes to file
  def test_check_correct_write_index(self):
    test = forward.writeToFile(*forward.createDictionary())
    cwd = os.getcwd()
    test = forward.writeToFile(test, cwd)
    

    with open('D:\\kpi\\magistr\\search\\Information-retrieval-systems\\lab1\\tests\\forward_index_file.txt', 'r') as FirstFile:
      test1 = FirstFile.read()
    self.assertNotEqual(str(test), test1)
    

# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()