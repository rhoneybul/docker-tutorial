import unittest
import app 

class TestDockerapp(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    def testIndex(self):
        response = self.app.get("/")
        response = response.data.decode('utf-8')
        assert(str(response) == "Welcome to the API") 
    
    def testSquare(self):
        testCases = [1, 2, 3, 4, 5]
        for case in testCases:
            response = self.app.get("/" + str(case))
            assert(case * case == int(response.data))
    
if __name__ == "__main__":
    unittest.main()