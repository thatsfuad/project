from django.test import TestCase
from django.urls import reverse
from django.test.client import Client

class TemplateRenderingTest(TestCase):
    def test_template_rendering(self):
        # Simulate a request to the page where the rendering issue occurs
        url = reverse('mhe_31_school_supplies_image_quiz')  # Adjust the URL name based on your project's URLs configuration
        client = Client()
        response = client.get(url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Print response content
        print("Response content:", response.content.decode('utf-8'))

        # Additional checks can be added here to inspect the response content
        # For example, you can check if certain elements are present in the response content

        # If there are specific errors or unexpected behavior you're looking for, you can add assertions for those as well
