#!/usr/bin/python3

import unittest
Customer = __import__('2-customer_class').Customer

""" remember this imports the Customer class from the file "2-customer_class". 
This is also same as write "from 2-customer_class import Customer" , but this will
be invalid cause a module cant be named with '-' in its name.  
"""

class TestCustomer(unittest.TestCase):

    def setUp(self): # this creates a first code to run before each test. Here customers instances is created, instead of creating  an instance in each test segment
        self.customer_1 = Customer('John', 'Brad', 5000)
        self.customer_2 = Customer('Tina', 'Smith', 3000)
    
    def tearDown(self): # this creates another instruction for after each test, and can be used to delete files created during testing if such testing occured
        pass
    """setUp and tearDown method can be made to run just once before all tests and once after all tests
    respectively, by making them a class method"""

    def test_customer_mail(self):
        self.assertEqual(self.customer_1.customer_mail, 'John.Brad@email.com')
        self.assertEqual(self.customer_2.customer_mail, 'Tina.Smith@email.com')

    def test_customer_fullname(self):
        self.assertEqual(self.customer_1.customer_fullname, 'John Brad')
        self.assertEqual(self.customer_2.customer_fullname, 'Tina Smith')

    def test_apply_discount(self):
        self.customer_1.apply_discount()
        self.customer_2.apply_discount()

        self.assertEqual(self.customer_1.purchase, 4750)
        self.assertEqual(self.customer_2.purchase, 2850)


if __name__ == '__main__':
    unittest.main()