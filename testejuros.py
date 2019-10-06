import unittest

#class Testing(unittest.TestCase):
    #def test_string(self):
        #a = 'some'
        #b = 'some'
        #self.assertEqual(a, b)

    #def test_boolean(self):
        #a = True
        #b = True
        #self.assertEqual(a, b)

#if __name__ == '__main__':
    #unittest.main()


def verSenha(senha):
    if len(senha) >= 8:
        return True
    else:
        return False 

class MyTest(unittest.TestCase):
    def testeSenha(self):
        self.assertEqual(verSenha('1223'),True)

if __name__ == '__main__':
    unittest.main()
