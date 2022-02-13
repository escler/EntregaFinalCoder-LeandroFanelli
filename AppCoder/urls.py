from django.urls import path

from AppCoder.views import Page_DeleteView, Page_DetailView, Page_ListView, Page_UpdateView, create_page

urlpatterns = [
    path('pages/', Page_ListView.as_view(), name='pages'),
    path('pages/add/', create_page, name='page_add'),
    path('pages/update/<pk>', Page_UpdateView.as_view(), name='page_update'),
    path('pages/delete/<pk>', Page_DeleteView.as_view(), name='page_delete'),
    path('pages/view/<pk>', Page_DetailView.as_view(), name='page_view')
]