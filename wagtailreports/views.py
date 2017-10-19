from django.shortcuts import redirect, render

def reports(request):
    return render(request, 'reports/dashboard.html', {
    })

def settings(request):
    return render(request, 'reports/settings.html', {
    })