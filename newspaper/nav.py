from newspaper.models import Category

def navigation(request):
    category = Category.objects.all()[:4]
    return {"categories": category}


    