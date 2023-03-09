# Write your code below:
import surfshop
import unittest
import datetime

class SurfShopTest(unittest.TestCase):
  def setUp(self):
    self.cart = surfshop.ShoppingCart()

  #Testing with 1 surfboard
  def test2_add_surfboards(self):
    self.assertEqual(self.cart.add_surfboards(1), 'Successfully added 1 surfboard to cart!')
  
  #Testing with more than one surfboard
  #Parameterization
  def test_add_surfboards(self):
    for val in [2,3,4]:
      with self.subTest(val):
        message = 'Successfully added ' + str(val) + ' surfboards to cart!'
        self.assertEqual(self.cart.add_surfboards(val), message)
        self.cart.num_surfboards = 0

  #Using unittest skip decorator
  @unittest.skip
  def test3_add_surfboards(self):
    self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)
    print(surfshop.TooManyBoardsError())

  #Testing apply_locals_discount function
  def test_apply_locals_discount(self):
    self.cart.apply_locals_discount()
    self.assertTrue(self.cart.locals_discount)

  #Testing set_checkout_date function
  def test_set_checkout_date(self):
    self.assertRaises(surfshop.CheckoutDateError, self.cart.set_checkout_date, datetime.datetime(2022,2,12))

unittest.main()
  