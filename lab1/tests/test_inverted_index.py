import unittest
import inverted
import os


#Test cases to test inverted index methods
class TestInvertedIndex(unittest.TestCase):
  #setUp method
  def setUp(self):
    self.index = inverted.invertedIndex()
    #print(self.index)


  #Check indexes
  def test_add_index(self):
    self.assertEqual(self.index.get('hi'), ['test_file1.txt', 'test_file4.txt'])
    self.assertEqual(self.index.get('sky'), ['test_file1.txt', 'test_file2.txt', 'test_file5.txt'])
    self.assertEqual(self.index.get('hello'), ['test_file2.txt', 'test_file4.txt'])
    self.assertEqual(self.index.get('greetings'), ['test_file3.txt'])
    self.assertEqual(self.index.get('eye'), ['test_file3.txt'])
    self.assertEqual(self.index.get('yes'), ['test_file5.txt'])


  #Check indexes(ignore case)
  def test_check_case(self):
    test = inverted.invertedIndex()
    self.assertEqual(self.index.keys(), test.keys())


  #Check update key-value 
  def test_update_index(self):
    test = inverted.invertedIndex()
    test.update([('file6', 'hello')])
    self.assertNotEqual(test.values(), self.index.values())


  #Check correct writing indexes to file
  def test_check_correct_write_index(self):
    test = inverted.writeToFile(*inverted.createDictionary())
    cwd = os.getcwd()
    test = inverted.writeToFile(test, cwd)
    
    
    with open('D:\\kpi\\magistr\\search\\Information-retrieval-systems\\lab1\\tests\\inverted_index_file.txt', 'r') as FirstFile:
      test1 = FirstFile.read()
    self.assertNotEqual(str(test), test1)
    

# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()