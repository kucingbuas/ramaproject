from django.urls import path
from .views import *

urlpatterns = [
    path('', users, name='tabel_user'),
    path('detail/<int:id>',user_detail, name='detail_user'),
    path('edit/<int:id>',user_edit, name='edit_user'),
    path('delete/<int:id>', user_hapus, name='hapus_user'),

     
]
