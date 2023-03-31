import unittest
import json
from api import app, HTTP_OK, HTTP_BAD_REQUEST 

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Test case: overlap is False
    def test_no_overlap(self):
        data = {
            'range1': {
                'start': '2023-01-01 00:00:00',
                'end': '2023-01-01 11:59:59'
            },
            'range2': {
                'start': '2023-01-02 12:00:00',
                'end': '2023-01-02 23:59:59'
            }
        }
        response = self.app.post('/api/isOverlap', json=data)
        self.assertEqual(response.status_code, HTTP_OK) 
        self.assertFalse(response.json[0]['overlap']) 

        data = {
            'range1': {
                'start': '2023-01-02 12:00:00',
                'end': '2023-01-02 23:59:59'
            },
            'range2': {
                'start': '2023-01-01 00:00:00',
                'end': '2023-01-01 11:59:59'
            }
        }
        response = self.app.post('/api/isOverlap', json=data)
        self.assertEqual(response.status_code, HTTP_OK) 
        self.assertFalse(response.json[0]['overlap']) 

    # Test case:  overlap is True 
    def test_overlap(self):
        # partial overlap case: [range1 {range2 range1] range2}
        data = {
            'range1': {
                'start': '2023-01-01 00:00:00',
                'end': '2023-01-01 11:59:59'
            },
            'range2': {
                'start': '2023-01-01 8:00:00',
                'end': '2023-01-01 23:59:59'
            }
        }
        response = self.app.post('/api/isOverlap', json=data)
        self.assertEqual(response.status_code, HTTP_OK) 
        self.assertTrue(response.json[0]['overlap']) 

        # partial overlap case: [range2 {range1 range2] range1}
        data = {
            'range1': {
                'start': '2023-01-02 12:00:00',
                'end': '2023-01-02 23:59:59'
            },
            'range2': {
                'start': '2023-01-01 00:00:00',
                'end': '2023-01-02 13:59:59'
            }
        }
        response = self.app.post('/api/isOverlap', json=data)
        self.assertEqual(response.status_code, HTTP_OK) 
        self.assertTrue(response.json[0]['overlap']) 

        # same range: {[range1 range2]}
        data = {
            'range1': {
                'start': '2023-01-02 12:00:00',
                'end': '2023-01-02 23:59:59'
            },
            'range2': {
                'start': '2023-01-02 12:00:00',
                'end': '2023-01-02 23:59:59'
            }
        }
        response = self.app.post('/api/isOverlap', json=data)
        self.assertEqual(response.status_code, HTTP_OK) 
        self.assertTrue(response.json[0]['overlap']) 

        # fully overlap case: [range1 {range2}] 
        data = {
            'range1': {
                'start': '2023-01-01 12:00:00',
                'end': '2023-01-02 23:59:59'
            },
            'range2': {
                'start': '2023-01-02 12:00:00',
                'end': '2023-01-02 16:59:59'
            }
        }
        response = self.app.post('/api/isOverlap', json=data)
        self.assertEqual(response.status_code, HTTP_OK) 
        self.assertTrue(response.json[0]['overlap']) 

        # fully overlap case: [range2 {range1}]  
        data = {
            'range2': {
                'start': '2023-01-01 12:00:00',
                'end': '2023-01-02 23:59:59'
            },
            'range1': {
                'start': '2023-01-02 12:00:00',
                'end': '2023-01-02 16:59:59'
            }
        }
        response = self.app.post('/api/isOverlap', json=data)
        self.assertEqual(response.status_code, HTTP_OK) 
        self.assertTrue(response.json[0]['overlap']) 


    # Test case: input error
    # TODO: add more test cases for different input errors
    def test_error_input(self):
        data = {
            'range1': {
                'start': '2018-01-01 00:00:00',
                'end': '2018-01-01 23:59:59'
            },
            'range2': {
                'start': '2018-01-02' 
            }
        }
        response = self.app.post('/api/isOverlap', json=data)
        self.assertEqual(response.status_code, HTTP_BAD_REQUEST) 
        
if __name__ == '__main__':
    unittest.main()
