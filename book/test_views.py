from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from book.models import CreateBook, CreateChapter

class AddBookViewTest(TestCase):
    """"
    Check that book has been added
    """
    def setUp(self):
        """
        Create book details
        """"
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_add_book_form_valid_submission(self):
        """
        Checks add book (Book details) submits
        """
        form_data = {
            'title': 'New Test Book',
            'status': 1, 
            'excerpt': 'Test excerpt',
            'synopsis': 'Test synopsis'
        }
        response = self.client.post(reverse('book_details'), form_data)

        # Check if a CreateBook object was created
        new_book = CreateBook.objects.filter(title='New Test Book').first()
        self.assertIsNotNone(new_book)

        # Check if the user is redirected to the 'add_chapter' page for the new book
        self.assertRedirects(response, reverse('add_chapter', kwargs={'book_slug': new_book.slug}))

    
class AddBookChapterTest(TestCase):
    """
    Check Chapter is associated with chapter
    Check chapter submits
    """
    def setUp(self):
        """
        Create chapter details
        """"
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.book = CreateBook.objects.create(title='Test Book', author=self.user, slug='test-book')

    def test_form_valid_submission(self):
        """
        Check if chapter submission is valid 
        """
        # Include all required fields for your form
        form_data = {
            'chapter': 'Test chapter',
            'status': 0,
            'content': 'Test content'
            
        }
        response = self.client.post(reverse('completed_book'))

        # check if a CreateBook object was created
        self.assertFalse(CreateChapter.objects.filter(chapter='Test chapter').exists())
        
    def test_add_chapter_form_valid_submission(self):
        """
        Check Chapter is added to the book 
        """
        form_data = {
            'chapter': 'Chapter 1',
            'content': 'This is the content of the first chapter.',
            'status': 0
        }
        # Submit the form data to the add chapter view
        response = self.client.post(reverse('add_chapter', kwargs={'book_slug': self.book.slug}), form_data)

        # Check if the response redirects
        self.assertRedirects(response, '/book/completed_book/')  

        # Verify that the chapter has been added to the book
        self.assertTrue(CreateChapter.objects.filter(chapter='Chapter 1', book=self.book).exists())


class EditChapterTest(TestCase):
    """"
    Checks chapter is edited and submits
    """

    def setUp(self):
        """
        Create chapter details
        """"
        # Create a test user and log in
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

        # Create a test book and a test chapter
        self.book = CreateBook.objects.create(title='Test Book', author=self.user, slug='test-book')
        self.chapter = CreateChapter.objects.create(chapter='Original Chapter Title', book=self.book, content='Original content')

    def test_edit_chapter(self):
        """
        Test chapter text is edited
        """
        edit_url = reverse('edit_book_chapter', kwargs={'book_slug': self.book.slug, 'pk': self.chapter.pk})
        
        form_data = {
            'chapter': 'Updated Chapter Title',
            'content': 'Updated content',
            'status': 1
        }

        # Submit the form data to the edit chapter view
        response = self.client.post(edit_url, form_data)

        # Check if the response redirects to home
        self.assertRedirects(response, reverse('home'))

        # Verify that the chapter has been updated
        self.chapter.refresh_from_db()
        self.assertEqual(self.chapter.chapter, 'Updated Chapter Title')
        self.assertEqual(self.chapter.content, 'Updated content')


class DeleteChapterTest(TestCase):

    def setUp(self):
        """
        Create book details
        """"
         # Create a test user and log in
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

        # Create a test book and a test chapter
        self.book = CreateBook.objects.create(title='Test Book', author=self.user, slug='test-book')
        self.chapter = CreateChapter.objects.create(chapter='Original Chapter Title', book=self.book, content='Original content')

    def test_delete_chapter(self):
        """
        Check if chapter is deleted and submits
        """
        delete_url = reverse('delete_book_chapter', kwargs={'book_slug': self.book.slug, 'pk': self.chapter.pk})

        form_data = {
            'chapter': 'Updated Chapter Title',
            'content': 'Updated content',
            'status': 1
        }

        # Make a request to the delete chapter view
        response = self.client.post(delete_url, form_data)

        # Check if the response redirects
        self.assertRedirects(response, reverse('home'))

        # Verify that the chapter has been deleted
        self.assertFalse(CreateChapter.objects.filter(pk=self.chapter.pk).exists())


class EditBookDetailsTest(TestCase):
    """"
    Check book is edited
    """

    def setUp(self):
        """
        Create book details
        """"
        # Create a test user and log in
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

        # Create a test book
        self.book = CreateBook.objects.create(title='Test Book', author=self.user, slug='test-book')

    def test_edit_book(self):
        """
        Test Book text is edited
        """
        edit_book = reverse('edit_book', kwargs={'slug': self.book.slug, 'pk': self.book.pk})
        
        form_data = {
            'title': 'Updated book Title',
            'status': 1, 
            'excerpt': 'Updated excerpt',
            'synopsis': 'Updated Chapter synopsis'
        }

        # Submit the form data to the edit book view
        response = self.client.post(edit_book, form_data)

        # Check if the response redirects to home
        self.assertRedirects(response, reverse('home'))

        # Verify that the chapter has been updated
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated book Title')
        self.assertEqual(self.book.synopsis, 'Updated Chapter synopsis')
        self.assertEqual(self.book.excerpt, 'Updated excerpt')




class DeleteBookTest(TestCase):

    def setUp(self):
        """
        Create book details
        """"
         # Create a test user and log in
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

        # Create a test book
        self.book = CreateBook.objects.create(title='Test Book', author=self.user, slug='test-book')
        

    def test_delete_chapter(self):
        """
        Test if book has been deleted
        """
        delete_book = reverse('delete_book', kwargs={'slug': self.book.slug})

        form_data = {
            'title': 'New Test Book',
            'status': 1, 
            'excerpt': 'Test excerpt',
            'synopsis': 'Test synopsis'
        }

        # Make a request to the delete chapter view
        response = self.client.post(delete_book, form_data)

        # Check if the response redirects
        self.assertRedirects(response, reverse('home'))

        # Verify that the book has been deleted
        self.assertFalse(CreateBook.objects.filter(slug=self.book.slug).exists())