#! /home/rendy/python/env/tdd/bin/python

from selenium import webdriver
import unittest

class DjanjoAppTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Chrome()
		self.browser.implicity_wait(5)

	def tearDown(self):
		self.browser.quit()

	def test_input_and_retrive_a_list(self):
		# user open browser and view the home page of website
		self.browser.get('http://localhost:8000')

		# user notice there is 'To-Do' items in browser title
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')
		# user accept and create first 'To-Do' item

		# user input 'buy PS4' in the text area

		# after user enter, webpage will re-fresh and display 'buy PS4' in the to do list

		# there is another text area for user to input and user input 'buy P5S'

		# after user enter, webpage will re-fresh and display two items

		# webpage generate an unique url to user to show that website remember user's to-do list

		# user click the link and found its to-do list

if __name__ == '__main__':
	unittest.main()
