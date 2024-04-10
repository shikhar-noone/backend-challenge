from django.http import HttpResponse

def view_test(request):
    return HttpResponse("This is a testing url.")