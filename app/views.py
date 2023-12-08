from django.shortcuts import render

# Create your views here.
def generic_bootstrap_download(request):
    return render(request,'generic_bootstrap_download.html')