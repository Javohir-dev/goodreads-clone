from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from books.models import Book, BookReview
from users.models import CustomUser


class BookReviewAPITestCase(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(username="javohir", first_name="javohir")
        self.user.set_password("somepassword")
        self.user.save()
        self.client.login(username="javohir", password='somepassword')
        
    def test_book_review_detail(self):
        book = Book.objects.create(title="Book1", description="description1", isbn="3215464511")
        br = BookReview.objects.create(book=book, user=self.user, stars_given=5, comment='Very good book.')

        response = self.client.get(reverse('api:review_detail', kwargs={'id': br.id}))
        
        # BookReview
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], br.id)
        self.assertEqual(response.data['stars_given'], 5)
        self.assertEqual(response.data['comment'], 'Very good book.')
        # BookReview's book
        self.assertEqual(response.data['book']['id'], book.id)
        self.assertEqual(response.data['book']['title'], 'Book1')
        self.assertEqual(response.data['book']['description'], 'description1')
        self.assertEqual(response.data['book']['isbn'], '3215464511')
        # BookReview's user
        self.assertEqual(response.data['user']['id'], self.user.id)
        self.assertEqual(response.data['user']['username'], 'javohir')
        self.assertEqual(response.data['user']['first_name'], 'javohir')

    
    def test_delete_review(self):
        book = Book.objects.create(title="Book1", description="description1", isbn="3215464511")
        br = BookReview.objects.create(book=book, user=self.user, stars_given=5, comment='Very good book.')

        response = self.client.delete(reverse('api:review_detail', kwargs={'id': br.id}))

        self.assertEqual(response.status_code, 204)
        self.assertFalse(BookReview.objects.filter(id=br.id).exists())


    def test_patch_review(self):
        book = Book.objects.create(title="Book1", description="description1", isbn="3215464511")
        br = BookReview.objects.create(book=book, user=self.user, stars_given=5, comment='Very good book.')

        response = self.client.patch(reverse('api:review_detail', kwargs={'id': br.id}), data={'stars_given':4})
        br.refresh_from_db()


        self.assertEqual(response.status_code, 200)
        self.assertEqual(br.stars_given, 4)


    def test_put_review(self):
        book = Book.objects.create(title="Book1", description="description1", isbn="3215464511")
        br = BookReview.objects.create(book=book, user=self.user, stars_given=5, comment='Very good book.')

        response = self.client.put(
            reverse('api:review_detail', kwargs={'id': br.id}),
            data={'stars_given':4, 'comment': 'New comment.', 'book_id': book.id, 'user_id': self.user.id}
        )

        br.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(br.stars_given, 4)
    

    def test_create_review(self):
        book = Book.objects.create(title="Book1", description="description1", isbn="3215464511")
        data={
            'stars_given': 4, 
            'comment': 'New comment.', 
            'book_id': book.id, 
            'user_id': self.user.id
        }

        response = self.client.post(reverse('api:review_list'), data=data)
        br = BookReview.objects.get(book=book)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(br.stars_given, 4)
        self.assertEqual(br.comment, 'New comment.')
        



    def test_book_review_list(self):
        user_two = CustomUser.objects.create(username="khojiakbar", first_name="Khojiakbar")
        book = Book.objects.create(title="Book", description="description", isbn="3215464511")
        br = BookReview.objects.create(book=book, user=self.user, stars_given=5, comment='Very good book.')
        br_two = BookReview.objects.create(book=book, user=user_two, stars_given=3, comment='Nice book.')

        response = self.client.get(reverse('api:review_list'))
        br.refresh_from_db()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['count'], 2)
        self.assertIn('next', response.data)
        self.assertIn('previous', response.data)
        # First Review 
        self.assertEqual(response.data['results'][1]['id'], br.id)
        self.assertEqual(response.data['results'][1]['comment'], 'Very good book.')
        self.assertEqual(response.data['results'][1]['stars_given'], 5)
        # First Review's Book
        self.assertEqual(response.data['results'][1]['book']['id'], book.id)
        self.assertEqual(response.data['results'][1]['book']['title'], 'Book')
        self.assertEqual(response.data['results'][1]['book']['description'], 'description')
        self.assertEqual(response.data['results'][1]['book']['isbn'], '3215464511')
        # First Review's User
        self.assertEqual(response.data['results'][1]['user']['id'], self.user.id)
        self.assertEqual(response.data['results'][1]['user']['username'], 'javohir')
        self.assertEqual(response.data['results'][1]['user']['first_name'], 'javohir')
        # Second Review
        self.assertEqual(response.data['results'][0]['id'], br_two.id)
        self.assertEqual(response.data['results'][0]['comment'], 'Nice book.')
        self.assertEqual(response.data['results'][0]['stars_given'], 3)
        # Second Review's Book
        self.assertEqual(response.data['results'][0]['book']['id'], book.id)
        self.assertEqual(response.data['results'][0]['book']['title'], 'Book')
        self.assertEqual(response.data['results'][0]['book']['description'], 'description')
        self.assertEqual(response.data['results'][0]['book']['isbn'], '3215464511')
        # First Review's User
        self.assertEqual(response.data['results'][0]['user']['id'], user_two.id)
        self.assertEqual(response.data['results'][0]['user']['username'], 'khojiakbar')
        self.assertEqual(response.data['results'][0]['user']['first_name'], 'Khojiakbar')

