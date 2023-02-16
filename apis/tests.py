from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from books.models import Book
# Create your tests here.


class APITest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Best Title",
            subtitle="Best Subtitle",
            author="ali raza",
            isbn="1234567891234",

        )

    def test_api_listview(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.book)
        self.assertEqual(Book.objects.count(), 1)
