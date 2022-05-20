import unittest
import function_plotter

class TestFunctionPlotter(unittest.TestCase):
	
	def test_popup_emptyFields(self):
		result = function_plotter.popup_emptyFields();
		self.assertFalse(result)		

		
	def test_popup_validInput(self):
		result = function_plotter.popup_validInput();
		self.assertFalse(result)
		

if __name__ == '__main__':
	unittest.main(_)
