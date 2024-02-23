from django.test import TestCase
from .models import Content
from django.utils import timezone
from django.urls.base import reverse

# Create your tests here.
class ContentTestCase(TestCase):
    """Unit tests for Content model"""
    def setUp(self):
        """Creates a test instance"""
        self.content = Content.objects.create(
                title="Business News",
                description="Top business news across Africa",
                link="https://some-link.com",
                pub_date=timezone.now(),
                guid="odbdnn-mndhnk-nnsjc",
                site_name="Business Center",
                )

    def test_model_fields(self):
        """Tests that model fields values are correctly assigned"""
        self.assertEqual(self.content.link, "https://some-link.com")
        self.assertEqual(self.content.title, "Business News")
        self.assertEqual(self.content.description, "Top business news across Africa")

    def test_to_string(self):
        """Test model string representation"""
        self.assertEqual(
                str(self.content), "Business Center: Business News"
                )

    def test_index_page_status(self):
        """Tests that index page returs Http OK"""
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status(self):
        """Test about page returns OK"""
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_index_template(self):
        """Test correct template used to render index"""
        response = self.client.get(reverse('news_content:index'))
        self.assertTemplateUsed(response, 'index.html')
