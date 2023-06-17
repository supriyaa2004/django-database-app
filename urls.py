# # # from django.urls import path
# # # from . import views

# # # urlpatterns = [
# # #     path('about/', views.about),
# # #     path('child/', views.child),
# # #      path('child1/', views.child1),
# # # 
# # from django.urls import path
# # from .views import create_book

# # urlpatterns = [
# #     path('create/', create_book, name='create_book'),
# # 
# from django.urls import path
# from .views import create_product

# urlpatterns = [
#     path('create/', create_product, name='create_product'),
# ]
from django.urls import path
from . import views

app_name = 'hello'

urlpatterns = [
    path('add/', views.add_record, name='add_record'),
    path('delete/', views.delete_record, name='delete_record'),
    path('disp/', views.display_records, name='display_records'),
]
