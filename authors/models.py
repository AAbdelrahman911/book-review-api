from django.db import models
from django.contrib.auth.models import User

class GenreChoices(models.TextChoices):
    BIOGRAPHY = 'biography', 'Biography'
    FICTION = 'fiction', 'Fiction'
    FANTASY = 'fantasy', 'Fantasy'
    MYSTERY = 'mystery', 'Mystery'
    HORROR = 'horror', 'Horror'
    ROMANCE = 'romance', 'Romance'
    HISTORY = 'history', 'History'

class Profile(models.Model):
    bio = models.TextField(max_length=150)
    date_of_birth = models.DateField(blank=True, null=True)
    user = models.OneToOneField(User,unique= True, on_delete=models.CASCADE, related_name='profile') 
    is_author = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank= True, null= True)
    
    def __str__(self):
        return f"Profile of {self.user.username}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    genre = models.CharField(max_length=50, choices=GenreChoices.choices)
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='author_books')

    def __str__(self):
        return self.title
    

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    comment = models.TextField(blank= True, null= True)
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f'Review by {self.user.username} for {self.book.title}'

