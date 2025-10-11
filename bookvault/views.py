from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Book
from .forms import BookForm, RegisterForm

# ==== Home Page (All Books) ====
def home_view(request):
    books = Book.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'books': books})

# ==== My Collection (User's Books) ====
@login_required
def my_collection_view(request):
    books = Book.objects.filter(user=request.user)
    return render(request, 'my_collection.html', {'books': books})

# ==== Book Detail ====
def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})

# ==== Add New Book ====
@login_required
def book_create_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('my_collection')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form, 'title': 'Add Book'})

# ==== Edit Book ====
@login_required
def book_update_view(request, pk):
    book = get_object_or_404(Book, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('my_collection')
    else:
        form = BookForm(instance=book)
    return render(request, 'book_form.html', {'form': form, 'title': 'Edit Book'})

# ==== Delete Book ====
@login_required
def book_delete_view(request, pk):
    book = get_object_or_404(Book, pk=pk, user=request.user)
    if request.method == 'POST':
        book.delete()
        return redirect('my_collection')
    return render(request, 'book_confirm_delete.html', {'book': book})

# ==== Register ====
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

# ==== Login ====
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# ==== Logout ====
def logout_view(request):
    logout(request)
    return redirect('home')
