from django.shortcuts import render, get_object_or_404
from book.models import CreateBook

# Create your views here.

def view_profile(request):
    user_books = request.user.books.filter(author=request.user)
    return render(request, 'profiles/profile.html', {'user_books': user_books})



# def edit_profile(request):
#     profile = request.user.profile

#     if request.method == 'POST':
#         form = ProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     else:
#         form = ProfileForm(instance=profile)

#     return render(request, 'edit_profile.html', {'form': form})