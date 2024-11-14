# from django.shortcuts import render, redirect
#
# from medilabApp.models import Appointment, Contact
#
#
# # Create your views here
# def index(request):
#     return render(request, 'index.html')
#
# def starter(request):
#     return render(request, 'starter-page.html')
# def about(request):
#     return render(request, 'about.html')
#
#
# def appointment(request):
#     success = False
#     if request.method == 'POST':
#
#         appointments = Appointment(
#             name=request.POST.get('name'),
#             email=request.POST.get('email'),
#             phone=request.POST.get('phone'),
#             date=request.POST.get('date'),  # Save the date string or convert to datetime if necessary
#             department=request.POST.get('department'),
#             doctor=request.POST.get('doctor'),
#             message=request.POST.get('message'),
#         )
#         appointments.save()
#         return render(request, 'appointment.html', {'success': True})
#     else:
#
#        return render(request, 'appointment.html', {'success': False})
#
# def contact(request):
#     success = False
#     if request.method == 'POST':
#         contacts = Contact(
#             name=request.POST.get('name'),
#             email=request.POST.get('email'),
#             subject=request.POST.get('subject'),
#             message=request.POST.get('message'),
#         )
#         contacts.save()
#         return render(request, 'contact.html', {'success': True})
#     else:
#         return render(request, 'contact.html', {'success': False})
#
#
# def view_appointment(request):
#     all_appointment = Appointment.objects.all()
#     return render(request, 'view-appointments.html', {'all_appointment': all_appointment})
#
# def delete_appointment(request, appoint_id ):
#     delete_appoint = Appointment.objects.get(id=appoint_id)
#     delete_appoint.delete()
#     return redirect('/view-appointments')
#
#
# def view_contact(request):
#     all_contacts = Contact.objects.all()
#     return render(request, 'view-contact.html', {'all_contacts': all_contacts})
#
# def delete_contact(request, contact_id ):
#     delete_contacts = Contact.objects.get(id=contact_id)
#     delete_contacts.delete()
#     return redirect('/view-contacts')


from django.shortcuts import render, redirect
from django.http import Http404  # Import Http404 for handling not found errors
from medilabApp.models import Appointment, Contact

# Your existing views
def index(request):
    return render(request, 'index.html')

def starter(request):
    return render(request, 'starter-page.html')

def about(request):
    return render(request, 'about.html')

def appointment(request):
    success = False
    if request.method == 'POST':
        appointments = Appointment(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            date=request.POST.get('date'),
            department=request.POST.get('department'),
            doctor=request.POST.get('doctor'),
            message=request.POST.get('message'),
        )
        appointments.save()
        return render(request, 'appointment.html', {'success': True})
    else:
        return render(request, 'appointment.html', {'success': False})

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

# View for viewing appointments
def view_appointment(request):
    all_appointment = Appointment.objects.all()
    return render(request, 'view-appointments.html', {'all_appointment': all_appointment})

# View for deleting an appointment with error handling
def delete_appointment(request, appoint_id):
    try:
        delete_appoint = Appointment.objects.get(id=appoint_id)
        delete_appoint.delete()
        return redirect('/view-appointments')
    except Appointment.DoesNotExist:
        raise Http404("Appointment not found")

# View for viewing contacts
def view_contact(request):
    all_contacts = Contact.objects.all()
    return render(request, 'view-contact.html', {'all_contacts': all_contacts})

# View for deleting a contact with error handling
def delete_contact(request, contact_id):
    try:
        delete_contacts = Contact.objects.get(id=contact_id)
        delete_contacts.delete()
        return redirect('/view-contacts')
    except Contact.DoesNotExist:
        raise Http404("Contact not found")
