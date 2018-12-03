from unittest import TestCase, skip
from server import app

class ServerTestCase(TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_index_page(self):
        response = self.client.get('/')
        self.assertIn(b'World', response.data)

    def test_checkForm(self):
        response = self.client.get('/')
        self.assertIn(b'form', response.data)

    def test_checkPlus(self):
        response = self.client.get('/?arg1=3&op=plus&arg2=2')
        self.assertIn(b'<span id="answer">=5', response.data)

    def test_checkMinus(self):
        response = self.client.get('/?arg1=5&op=minus&arg2=3')
        self.assertIn(b'<span id="answer">=2', response.data)

    def test_checkMultiply(self):
        response = self.client.get('/?arg1=5&op=multiply&arg2=3')
        self.assertIn(b'<span id="answer">=15', response.data)

    def test_checkDivide(self):
        response = self.client.get('/?arg1=10&op=divide&arg2=2')
        self.assertIn(b'<span id="answer">=5.0', response.data)

    def test_iskl2(self):
        response = self.client.get('/?arg1=10&op=plus&arg2="5"')
        self.assertIn(b'<span id="answer">=15', response.data)
class ResearchTestCase(TestCase):
    @skip("Тест временно отключен")
    def test_assert_true(self):
        print('-= assertTrue =-')
        self.assertTrue(1 == 1)

    def test_assert_false(self):
        print('-= assertFalse =-')
        self.assertFalse(0 == 1)

    @classmethod
    def setUpClass(cls):
        print('-= setUpClass =-')

    def setUp(self):
        print('-= setUp =-')

    def tearDown(self):
        print('-= tearDown =-')

    @classmethod
    def tearDownClass(cls):
        print('-= tearDownClass =-')

    def testA(self):
        self.assertEqual('foo'.upper(), 'FOO')
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        print('-= testA =-')

    def testB(self):
        n = 50
        self.assertEqual(n, 50)
        self.assertTrue(n == 50)
        self.assertFalse(n != 50)
        print('-= testB =-')

    def testC(self):
        a = True
        self.assertEqual(a, True)
        self.assertTrue(a == True)
        self.assertFalse(a == False)
        print('-= testC =-')