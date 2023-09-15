from django.urls import path
from .views import All, Detail, All2, Detail2, CreateHeadphoneView, CreatePhoneView, UpdateHeadphone, UpdatePhone, DeleteHeadphone, DeletePhone

urlpatterns = [
    path('detail/<int:pk>', Detail.as_view()),
    path('all/', All.as_view()),
    path('detail2/<int:pk>', Detail2.as_view()),
    path('all2/', All2.as_view()),
    path('create1/', CreatePhoneView.as_view()),
    path('create2/', CreateHeadphoneView.as_view()),
    path('update/<int:pk>', UpdatePhone.as_view()),
    path('update2/<int:pk>', UpdateHeadphone.as_view()),
    path('delete/<int:pk>', DeletePhone.as_view()),
    path('delete2/<int:pk>', DeleteHeadphone.as_view()),
]