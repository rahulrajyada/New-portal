# from django.shortcuts import render

# # Create your views here.
import csv

from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.views.generic import View

User = get_user_model()

# yo chai user ko kun format ma data haru jaos bhanera
COLUMNS = [
    "first_name",
    "last_name",
    "username",
    "email",
    "is_staff",
    "is_active",
    "is_superuser",
    "last_login",
    "date_joined",
] 

class UserReportView(View):
    
    def get(self, request):
        response = HttpResponse(content_type="text/csv") # yo chai kun type ma download garnu parxa bhanera lekhnu parxa
        response["Content-Disposition"] = "attachment; filename=users.csv" # yo chai download hos bhanera lekhnu parxa / ani filename chai users.csv ho
        
        users = User.objects.all().only(*COLUMNS).values(*COLUMNS) #colum lai call garnu ani colums ko value call garnu
        
        writer = csv.DictWriter(response, fieldnames=COLUMNS) # yo chai csv.DictWrite use gardai response ma pathau xa and fieldname chai COLUMNS 
        writer.writeheader() # yo chai header aru pathau xa
        writer.writerows(users) # yo chai user ko data pathau xa
        
        return response  
