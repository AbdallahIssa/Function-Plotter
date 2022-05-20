#python -m unittest test_function_plotter.py

import unittest
import function_plotter

class TestFunctionPlotter(unittest.TestCase):
	
	def test_popup_emptyFields(self):
		result = function_plotter.popup_emptyFields();
		self.assertFalse(result)		

		
	def test_popup_validInput(self):
		result = function_plotter.popup_validInput();
		self.assertFalse(result)

	
	def test_plot(self):
		result = function_plotter.plot();
		self.assertFalse(result)
		

if __name__ == '__main__':
	unittest.main(_)