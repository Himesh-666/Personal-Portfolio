from django.shortcuts import render
from .models import ContactMessage

def contact_view(request):
    success = False

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        success = True

    return render(request, 'contact.html', {'success': success})