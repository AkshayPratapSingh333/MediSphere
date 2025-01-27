from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from .models import Doctor, Patient, Appointment, Item  # Import necessary models
from .forms import ItemForm  # Import the ItemForm for managing Item


# About page
def About(request):
    return render(request, 'about.html')

# Contact page
def Contact(request):
    return render(request, 'contact.html')

# Home page
def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    appointments = Appointment.objects.all()

    d_count = doctors.count()
    p_count = patients.count()
    a_count = appointments.count()

    context = {
        'd': d_count,
        'p': p_count,
        'a': a_count,
    }

    return render(request, 'index.html', context)

# Login view
def Login(request):
    error = ""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('home')
        else:
            error = "Invalid credentials or not authorized."
    
    return render(request, 'login.html', {'error': error})

# Logout view
def Logout_admin(request):
    logout(request)
    return redirect('login')

# View all doctors
def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    
    doctors = Doctor.objects.all()
    return render(request, 'view_doctor.html', {'doctors': doctors})

# Add a new doctor
def Add_Doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    
    if request.method == 'POST':
        name = request.POST['names']
        department = request.POST['department']
        contact = request.POST['contact']
        try:
            Doctor.objects.create(name=name, department=department, mobile=contact)
            return redirect('view_doctor')  # Redirect to view doctors after success
        except:
            error = "Error adding doctor."
    
    return render(request, 'add_doctor.html', {'error': error})

# Delete a doctor
def Delete_Doctor(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')

# View all patients
def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    
    patients = Patient.objects.all()
    return render(request, 'view_patient.html', {'patients': patients})

# Add a new patient
def Add_Patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    
    if request.method == 'POST':
        name = request.POST['name']
        gender = request.POST['gender']
        age = request.POST['age']
        reason = request.POST['reason']
        mobile = request.POST['mobile']
        admission = request.POST['admission']
        discharge = request.POST['discharge']
        doc_name = request.POST['docname']
        prescription = request.POST['prescription']
        bill = request.POST['bill']
        
        try:
            Patient.objects.create(
                name=name, gender=gender, age=age,
                reason=reason, mobile=mobile,
                admission=admission, discharge=discharge,
                docname=doc_name, prescription=prescription,
                bill=bill
            )
            return redirect('view_patient')  # Redirect to view patients after success
        except:
            error = "Error adding patient."
    
    return render(request, 'add_patient.html', {'error': error})

# Delete a patient
def Delete_Patient(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')

# View all appointments
def View_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    
    appointments = Appointment.objects.all()
    return render(request, 'view_appointment.html', {'appointments': appointments})

# Add a new appointment
def Add_Appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    
    if request.method == 'POST':
        doctor_name = request.POST['doctor']
        patient_name = request.POST['patient']
        date = request.POST['date']
        time = request.POST['time']

        doctor = Doctor.objects.filter(name=doctor_name).first()
        patient = Patient.objects.filter(name=patient_name).first()

        if doctor and patient:
            try:
                Appointment.objects.create(
                    doctor=doctor, patient=patient, date1=date, time1=time
                )
                return redirect('view_appointment')  # Redirect after successful add
            except Exception as e:
                error = "Error creating appointment."
                print(f"Error: {e}")
        else:
            error = "Invalid doctor or patient."

    return render(request, 'add_appointment.html', {
        'doctors': doctors,
        'patients': patients,
        'error': error
    })

# Delete an appointment
def Delete_Appointment(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    
    appointment = Appointment.objects.get(id=pid)
    appointment.delete()
    return redirect('view_appointment')

# Add an item
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_items')  # Redirect after successful add
    else:
        form = ItemForm()  # Create an empty form instance
    return render(request, 'add_item.html', {'form': form})  # Render the add item template

# View all items
def view_items(request):
    items = Item.objects.all()
    return render(request, 'view_items.html', {'items': items})

# Edit an item
def edit_item(request, id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('view_items')
    else:
        form = ItemForm(instance=item)  # Pre-fill the form with existing item data
    return render(request, 'edit_item.html', {'form': form, 'item': item})

# Delete an item
def delete_item(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return redirect('view_items')
