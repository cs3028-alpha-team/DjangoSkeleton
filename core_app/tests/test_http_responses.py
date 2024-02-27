from django.test import TestCase

# test the HTTP response for each route registered in core_app's URLS
class TestHTTP(TestCase): 

    # homepage tests
    def test_homepage_request(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # sysadmin page tests
    def test_sysadmin_page_request(self):
        response = self.client.get('/sysadmin')
        self.assertEqual(response.status_code, 200)

    # internship form tests
    def test_internship_form_request(self):
        response = self.client.get('/internship')
        self.assertEqual(response.status_code, 200)

    def test_internship_form_submission(self):
        response = self.client.get('/submit-internship')
        self.assertEqual(response.status_code, 200)

    # student form tests
    def test_student_form_request(self):
        response = self.client.get('/student')
        self.assertEqual(response.status_code, 200)

    def test_student_form_submission(self):
        response = self.client.get('/submit-student')
        self.assertEqual(response.status_code, 200)

    # algorithm-related actions tests
    def test_data_cleaning_procedure(self):
        response = self.client.get('/clean-data')
        self.assertEqual(response.status_code, 200)

    def test_matching_procedure(self):
        response = self.client.get('/matching')
        self.assertEqual(response.status_code, 200)

    def test_galeshapley_request(self):
        response = self.client.get('/run_matching_algorithm')
        self.assertEqual(response.status_code, 200)
        
    def test_login_admin_request(self):
        response = self.client.get('/logadmin/')
        self.assertEqual(response.status_code, 200)  
             
    def test_email_request(self):
        response = self.client.get('/send-email')
        self.assertEqual(response.status_code, 200)  
        
    def test_login_page_request(self):
        response = self.client.get('/login_user')
        self.assertEqual(response.status_code, 200)  
    
    def test_logout_page_request(self):
        response = self.client.get('/logout')
        self.assertEqual(response.status_code, 200)
        
    def test_dashboard_request(self):
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)    
          
    # edge cases
    def test_pagenotfound_status_code(self):
        response = self.client.get('/this-page-doesnt-exist')
        self.assertEqual(response.status_code, 404)