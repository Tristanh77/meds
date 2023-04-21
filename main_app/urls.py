from django.urls import path
from . import views

urlpatterns = [
    # home page (home.html)
    path('', views.home, name='home'),
    # index page that shows all medications within database (index.html)
    path('meds/', views.meds_index, name='index'),
    # details page for each mediction (detail.html)
    path('meds/<int:med_id>/', views.meds_detail, name='detail'),
    # add medication page with a form to save medication (med_form.html)
    path('meds/create/', views.MedCreate.as_view(), name='meds_create'),
    # update page for specific medication using the same form as meds_create (med_form.html)
    path('meds/<int:pk>/update/', views.MedUpdate.as_view(), name='meds_update'),
    # delete page to confirm deleting specific medication (med_confirm_delete.html)
    path('meds/<int:pk>/delete/', views.MedDelete.as_view(), name='meds_delete'),
    # form to add instance of user taking their medication on the detail page (detail.html)
    path('meds/<int:med_id>/add_whentaken/', views.add_whentaken, name='add_whentaken'),
    # sign up page to create new user
    path('accounts/signup/', views.signup, name='signup'),
]
