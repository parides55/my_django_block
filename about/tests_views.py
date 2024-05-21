from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import CollaborateForm


class TestAboutViews(TestCase):

    def setUp(self):
        """Creates about me content"""
        self.about_content = About.objects.create(
            title="About me", content="This is a test about me content",)
        self.about_content.save()

    def test_renders_about_page_with_collaborate_form(self):
        """Verifies get request for about me containing a collaboration form"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About me", response.content)
        self.assertIn(b"This is a test about me content", response.content) #optional
        self.assertIsInstance(response.context['collaborate_form'], CollaborateForm)

    def test_successful_collaboration_request_submission(self):
        """Test for posting a collaboration request"""
        post_data = {
            'name': 'John Doe',
            'email': 'test@test.com',
            'message': 'This is a test collaboration request.'
        }
        response = self.client.post(reverse('about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Collaboration request received! I endeavour to respond within 2 working days.", response.content)