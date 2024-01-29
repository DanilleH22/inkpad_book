import unittest
from django.test import TestCase
from .forms import  CreateBookForm, CreateChapterForm
from .models import Categories


class CreateBookFormTest(TestCase):
    """
    Test For CreateBook Form
    """

    def setUp(self):
        # Create a category instance
        self.category = Categories.objects.create(genre='Fiction')

    def test_createbook_form_valid(self):
        """
        Test if all data input is valid
        """
        # Complete and correct data
        complete_data = {
            'title': 'Test Title',
            'genre': self.category.id,
            'status': 0,
            'excerpt': 'Test excerpt',
            'synopsis': 'Test synopsis'
        }
        form = CreateBookForm(data=complete_data)
        self.assertTrue(form.is_valid(), 'Form should be valid with complete and correct data')

    def test_createbook_form_invalid(self):
        """
        Check if the form is invalid with incomplete data
        """
        # Incomplete data
        incomplete_data = {
            'title': 'Test Title',
            'genre': self.category.id,  
            'status': 2,
            'excerpt': 'Test excerpt',
            'synopsis': 'Test synopsis'
        }
        form = CreateBookForm(data=incomplete_data)
        self.assertFalse(form.is_valid(), 'Form should be invalid with incomplete data')



class CreateChapterFormTest(TestCase):
    """
    Tests for Create chapter form.
    """
    def test_createbook_form_valid(self):
        """
        Check if all data is given for chapter creation
        """
        # Chapter data
        chapter = {
            'chapter': 'Test chapter',
            'status': 0,
            'content': 'Test content'
        }
        form = CreateChapterForm(data=chapter)
        self.assertTrue(form.is_valid(), 'Form should be valid with complete and correct data')

    def test_createbook_form_invalid(self):
        """
        Check if form is invalid when necessary data is missing.
        """
        # Chapter data
        chapter = {
            'chapter': 'Test chapter',
            'status': 0,
            'content': ''
        }
        form = CreateChapterForm(data=chapter)
        self.assertFalse(form.is_valid(), 'Form is valid with but missing data')
