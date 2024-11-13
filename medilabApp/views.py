from django.shortcuts import render, redirect

from medilabApp.models import Appointment, Contact


# Create your views here
def index(request):
    return render(request, 'index.html')

def starter(request):
    return render(request, 'starter-page.html')
def about(request):
    return render(request, 'about.html')


def appointment(request):
    if request.method == 'POST':

        appointments = Appointment(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            date=request.POST.get('date'),  # Save the date string or convert to datetime if necessary
            department=request.POST.get('department'),
            doctor=request.POST.get('doctor'),
            message=request.POST.get('message'),
        )
        appointments.save()
        return redirect('about')
    else:

       return render(request, 'appointment.html')
def contact(request):
    success = False
    if request.method == 'POST':
        contacts = Contact(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message'),
        )
        contacts.save()
        return render(request, 'contact.html', {'success': True})
    else:
        return render(request, 'contact.html', {'success': False})





