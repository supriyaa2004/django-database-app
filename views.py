# # # from django.shortcuts import render 

 

# # # # def hello_world(request):
# # #     # return HttpResponse("Hello, World!")
# # # def about(request):
# # #     return render(request,'index.html')
# # # def child(request):
# # #     return render(request,'child.html')
# # # def child1(request):
# # #     return render(request,'child1.html')

# # from django.shortcuts import render
# # from .forms import bookForm

# # def create_book(request):
# #     if request.method == 'POST':
# #         form = bookForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             # Redirect or perform other actions
# #     else:
# #         form = bookForm()
# #     return render(request, 'book.html', {'form': form})
# from django.shortcuts import render
# from .forms import ProductForm

# def create_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             # Process form data
#             name = form.cleaned_data['name']
#             tittle = form.cleaned_data['title']
#             publisher = form.cleaned_data['description']
#             year=form.cleaned_data['year']
#             status=form.cleaned_data['status']
#             roll=form.cleaned_data['roll']
#             # Save data to the database or perform other actions
#     else:
#         form = ProductForm()
#     return render(request, 'book.html', {'form': form})


from django.shortcuts import render, redirect
from .forms import AddRecordForm, DeleteRecordForm
from .models import book

def add_record(request):
    if request.method == 'POST':
        form = AddRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('your_app_name:display_records')
    else:
        form = AddRecordForm()
    return render(request, 'add_record.html', {'form': form})

def delete_record(request):
    if request.method == 'POST':
        form = DeleteRecordForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['Author_first_name']
            book.objects.filter(Author_first_name=first_name).delete()
            return redirect('your_app_name:display_records')
    else:
        form = DeleteRecordForm()
    return render(request, 'delete_record.html', {'form': form})

def display_records(request):
    records = book.objects.all()
    return render(request, 'display_records.html', {'records': records})
