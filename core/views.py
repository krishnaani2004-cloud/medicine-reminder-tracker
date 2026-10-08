#from django.shortcuts import render
#from django.http import HttpResponse

#def home(request):
    #return HttpResponse("<h1>Welcome to Medicine Reminder App 😊</h1>")
# Create your views here.

#from django.shortcuts import HttpResponse
#from .models import Medicine

#def home(request):
    #medicines = Medicine.objects.all()
    
    #output = "<h1>Medicine List 💊</h1>"
    #output += "<ul>"
    
    #for med in medicines:
        #status = "✔ Taken" if med.taken else "❌ Not Taken"
        #output += f"<li>{med.name} - {med.time} - {status}</li>"
    
    #output += "</ul>"
    
    #return HttpResponse(output)

from django.shortcuts import render, redirect
from .models import Medicine, Patient, Caretaker, AdminUser


def home(request):
    medicines = Medicine.objects.all()
    return render(request, 'home.html', {'medicines': medicines})


# --------------------
# PATIENT REGISTER
# --------------------
def patient_register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        Patient.objects.create(
            username=username,
            email=email,
            password=password
        )
        return redirect('patient_login')

    return render(request, 'patient_register.html')


# --------------------
# CARETAKER REGISTER
# --------------------
def caretaker_register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']  
        certificate = request.FILES.get['certificate']  

        Caretaker.objects.create(
            username=username,
            email=email,
            password=password,
            phone=phone,
            certificate=certificate
        )

        return redirect('caretaker_login')

    return render(request, 'caretaker_register.html')


# --------------------
# PATIENT LOGIN
# --------------------
def patient_login(request): 
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = Patient.objects.get(email=email, password=password)
            request.session['patient_id'] = user.id
            return redirect('patient_dashboard')
        except Patient.DoesNotExist:
            return render(request, "patient_login.html", {"error": "Invalid login"})

    return render(request, "patient_login.html")


# --------------------
# CARETAKER LOGIN
# --------------------

def caretaker_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        try:
            caretaker = Caretaker.objects.get(email=email, password=password)

            if not caretaker.approved:
                return render(
                    request,
                    "caretaker_login.html",
                    {"error": "Your account is not approved by the admin yet"}
                )

            request.session['caretaker_id'] = caretaker.id
            return redirect('caretaker_dashboard')

        except Caretaker.DoesNotExist:
            return render(request, "caretaker_login.html", {"error": "Invalid login"})

    return render(request, "caretaker_login.html")

# --------------------
# REGISTER CHOICE PAGE
# --------------------
def register_choice(request):
    return render(request, "register_choice.html")


# --------------------
# ADMIN LOGIN
# --------------------
def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            admin = AdminUser.objects.get(username=username, password=password)
            request.session['admin'] = admin.id
            return redirect('admin_dashboard')
        except AdminUser.DoesNotExist:
            return render(request, 'admin_login.html', {"error": "Invalid Credentials"})

    return render(request, 'admin_login.html')


# --------------------
# ADMIN DASHBOARD
# --------------------
def admin_dashboard(request):
    caretakers = Caretaker.objects.all()
    pending = Caretaker.objects.filter(approved=False)
    approved = Caretaker.objects.filter(approved=True)
    patients = Patient.objects.all()

    return render(request, "admin_dashboard.html", {
        "caretakers": caretakers,
        "pending": pending,
        "approved": approved,
        "patients": patients,
    })


# --------------------
# APPROVE CARETAKER
# --------------------
def approve_caretaker(request, caretaker_id):
    caretaker = Caretaker.objects.get(id=caretaker_id)
    caretaker.approved = True
    caretaker.save()
    return redirect('admin_dashboard')


# --------------------
# DELETE CARETAKER
# --------------------
def delete_caretaker(request, caretaker_id):
    caretaker = Caretaker.objects.get(id=caretaker_id)
    caretaker.delete()
    return redirect('admin_dashboard')

def patient_dashboard(request):
    user_id = request.session.get("patient_id")

    patient = Patient.objects.get(id=user_id)
    medicines = Medicine.objects.all()   # you can filter by patient later

    return render(request, "patient_dashboard.html", {
        "user": patient,
        "medicines": medicines
    })

def caretaker_dashboard(request):
    caretaker_id = request.session.get("caretaker_id")

    if not caretaker_id:
        return redirect("caretaker_login")

    caretaker = Caretaker.objects.get(id=caretaker_id)

    medicines = Medicine.objects.all()

    return render(request, "caretaker_dashboard.html", {
        "user": caretaker,
        "medicines": medicines
    })

def add_medicine(request):
    if request.method == "POST":
        name = request.POST["name"]
        dosage = request.POST["dosage"]
        time = request.POST["time"]

        Medicine.objects.create(
            name=name,
            dosage=dosage,
            time=time
        )

        return redirect("patient_dashboard")

    return render(request, "add_medicine.html")