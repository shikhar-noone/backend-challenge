from django.urls import path, re_path
from new_app.views.test_view import view_test
# urls.py

urlpatterns = [
    re_path('/?$', view_test, name='query'),
]