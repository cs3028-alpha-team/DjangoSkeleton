from django.test import Client, TestCase
from django.urls import reverse

#currently seems to be errors with syntax and static files 

class Test_login_admin_Template(TestCase): # test login page
    def test_login_page_rendering(self):
        response = self.client.get(reverse('logadmin'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'logadmin.html')

    def test_login_form_submission(self): # test login submission
        login_data = {'user_name': 'admin', 'password': '12435687abdn'}
        response = self.client.post(reverse('login_user'), login_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('dashboard'))
    
    def test_login__error_messages_incorrect_details(self): #test error message for incorrect details
        login_data = {'user_name': 'ooo', 'password': '123'}
        response = self.client.post(reverse('login_user'), login_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid username or password")

    def test_login_error_messages_unfilled_field(self): # test error mesasage for empty field
        response = self.client.post(reverse('login_user'), {})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please fill in this field.")

class Test_Homepage_Template(TestCase): # test homepage
    def test_homepage_rendering(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepage.html')

    def test_homepage_static_files_loading(self): # test homepage static files
        response = self.client.get(reverse('homepage'))
        self.assertContains(response, '<link rel="stylesheet" href="/static/css/styles.css" />')
        self.assertContains(response, '<img class="rb" src="/static/images/return-button.jpg" alt="return button" />')
        self.assertContains(response, '<img class="smallimg" src="/static/images/unilogo.png" alt="University of Aberdeen logo" />')

    def test_homepage_links_generation(self): # test links
        response = self.client.get(reverse('homepage'))
        self.assertContains(response, f'href="{reverse("homepage")}"')
        self.assertContains(response, f'href="{reverse("internship")}"')
        self.assertContains(response, f'href="{reverse("student")}"')
        self.assertContains(response, f'href="{reverse("logadmin")}"')

class Test_Student_Template(TestCase): #test student form page
    def test_student_template_rendering(self):
        response = self.client.get(reverse('student'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student.html')

    def test_student_static_files_loading(self): # test static files
        response = self.client.get(reverse('student'))
        self.assertContains(response, '<link rel="stylesheet" href="/static/css/styles.css">')

    def test_student_form_rendering(self): # test if form renders correctly
        response = self.client.get(reverse('student'))
        self.assertContains(response, '<form method="post" action="{% url \'submit-student\' %}">')
        self.assertContains(response, '<input type="text" name="Fullname" id="Fullname" placeholder="Enter your answer" required />')
        self.assertContains(response, '<input type="text" name="Course" id="Course" placeholder="Enter your answer" required />')
        self.assertContains(response, '<input type="number" name="Score" id="Score" placeholder="Enter your answer" required />')
        self.assertContains(response, '<input type="text" name="Experience" id="Experience" placeholder="Enter your answer" required />')
        self.assertContains(response, '<input type="text" name="StudyMode" id="StudyMode" placeholder="Enter your answer" required />')
        self.assertContains(response, '<input type="text" name="StudyPattern" id="StudyPattern" placeholder="Enter your answer" required />')
    
    def test_student_go_back_javascript_function(self): # test 'gp back' function
        response = self.client.get(reverse('student'))
        self.assertContains(response, 'function goBack() { window.history.back(); }')

class Test_Internship_Template(TestCase): # test internship form page
    
    def test_internship_template_rendering(self): #test if template renders correctly
        response = self.client.get(reverse('internship'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'internship.html')

    def test_internship_static_files_loading(self): # test if css static files load
        response = self.client.get(reverse('internship'))
        self.assertContains(response, '<link rel="stylesheet" href="/static/css/styles.css">')

    def test_internship_form_rendering(self): # test if form renders correctly
        response = self.client.get(reverse('internship'))
        self.assertContains(response, '<form method="post" action="{% url \'submit-internship\' %}">')
        self.assertContains(response, '<input type="text" name="Title" id="Title" placeholder="Enter title" required />')
        self.assertContains(response, '<input type="text" name="Company" id="Company" placeholder="Enter company" required />')
        self.assertContains(response, '<input type="text" name="Field" id="Field" placeholder="Enter field" required />')
        self.assertContains(response, '<input type="number" name="MinScore" id="MinScore" placeholder="Enter minimum score" required />')
        self.assertContains(response, '<input type="number" name="Positions" id="Positions" placeholder="Enter positions" required />')

    def test_internship_go_back_javascript_function(self): # test 'go back' button
        response = self.client.get(reverse('internship'))
        self.assertContains(response, 'function goBack() { window.history.back(); }')
