from django.test import TestCase
from django.test import SimpleTestCase,TestCase
from django.urls import reverse
from .models import Post
# Create your tests here.


# class PagesTests(SimpleTestCase):
#     def test_home_page_status_code(self):
#         response=self.client.get('/')
#         self.assertEqual(response.status_code,200)
#
#     def test_about_page_status_code(self):
#         response=self.client.get('/about/')
#         self.assertEqual(response.status_code,200)

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text="just a test")

    def test_text_content(self):
        post=Post.objects.get(id=1)
        expected_object_name=f'{post.text}'
        self.assertEqual(expected_object_name,'just a test')

class HomePageViewTest(TestCase):
    def setup(self):
        Post.objects.create(text="This is another test")

    def test_view_url_exists_at_proper_location(self):
        response=self.client.get("/")
        self.assertEqual(response.status_code,200)

    def test_view_url_by_name(self):
            response=self.client.get(reverse('home'))
            self.assertEqual(response.status_code,200)

    def test_view_uses_correct_template(self):
            response=self.client.get(reverse("home"))
            self.assertEqual(response.status_code,200)
            self.assertTemplateUsed(response,'home.html')


