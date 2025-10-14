from django import forms
from .models import Book, Comment  # ← أضفنا Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# ==== BookForm ====
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'description', 'cover_image']


# ==== RegisterForm ====
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# ==== CommentForm ====
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Write your comment here...',
                'class': 'comment-textarea',  
                'style': 'width: 100%; padding: 12px; border-radius: 10px; border: 1px solid #ccc; resize: vertical; min-height: 100px; font-size: 1rem; color: #333; outline: none; transition: border 0.3s ease;'
            })
        }
