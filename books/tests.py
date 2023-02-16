from django.test import TestCase
from .models import Book
from django.urls import reverse
# Create your tests here.


class BookTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="A Good title",
            subtitle="An Excellent subtitle",
            author="Ali Raza",
            isbn="0000000000000"
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "A Good title")
        self.assertEqual(self.book.subtitle, "An Excellent subtitle")
        self.assertEqual(self.book.author, "Ali Raza")
        self.assertEqual(self.book.isbn, "0000000000000")

    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Excellent subtitle")
        self.assertTemplateUsed(response, "book_list.html")
