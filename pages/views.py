from django.shortcuts import render



# Create your views here.

def mainpage(request):
    return render(request, 'pages/mainpage.html')
def company_info(request):
    return render(request, 'pages/company_info.html')
def company_or(request):
    return render(request, 'pages/company_or.html')
def tech_info(request):
    return render(request, 'pages/tech_info.html')
def portfolio_info(request):
    return render(request, 'pages/portfolio_info.html')
def service_info(request):
    return render(request, 'pages/service_info.html')





# Create your views here.
