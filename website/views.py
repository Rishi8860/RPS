from dataclasses import Field
from email.message import Message
from django.shortcuts import render
from django.core.mail import send_mail
from website import models


# Create your views here.
def index(request):
    depart=models.department.objects.all()[:4]
    var=models.Doctor.objects.all()
    fields=models.field.objects.all()
    slider=models.Slider.objects.all()
    About_us=models.about_u.objects.all()
    return render(request,'website\index.html',{'data':var,'doct':fields,'slider':slider,'depart':depart,'About_us':About_us})
def contact(request):
    fields=models.field.objects.all()
    return render(request,'website\contact.html',{'doct':fields})
def department(request):
    depart=models.department.objects.all()
    fields=models.field.objects.all()
    return render(request,'website\departments.html',{'doct':fields,'depart':depart})
def doctor(request):
    if request.method=="POST":
        a=models.Doctor.objects.filter(Field=request.POST["Doctor"])
        fields=models.field.objects.all()
        return render(request,'website\doctors.html',{'data':a,'doct':fields})
    else:              
        var=models.Doctor.objects.all()
        fields=models.field.objects.all()
        return render(request,'website\doctors.html',{'data':var,'doct':fields})
def about(request):
    fields=models.field.objects.all()
    About_us=models.about_u.objects.all()
    return render(request,'website\About.html',{'doct':fields,'About_us':About_us})
def carriers(request):
    var=models.Doctor.objects.all()
    fields=models.field.objects.all()
    return render(request,'website\carriers.html',{'data':var,'doct':fields})
def Resume(request):
    if request.method=="POST":
        name=request.POST["Name"]
        Department=request.POST['Department']
        contact=request.POST["contact"]
        email=request.POST["email"]
        About_You=request.POST["About_You"]
        # Resume=request.FILES.get("Resume")
        # print(Resume)
        var=models.resume(Name=name,Contact=contact,Department=Department,Email=email,About_You=About_You,Resume=request.FILES.get('Resume'))
        var.save()
        h=f"Thank You {name}"
        p="For reaching out to us we will get to you shortly"
        fields=models.field.objects.all()
        return render(request,'website/Resume.html',{'doct':fields,'h':h,'p':p})
    else:
        fields=models.field.objects.all()
        h="Error"
        p="Due to some reasons your Resume is not registered with us, Please Try again or mail us as 'xyz@gmail.com' "
        return render(request,'website/touch.html',{'doct':fields,'h':h,'p':p})
def get_in_touch(request):
    if request.method=="POST":
        name=request.POST["Name"]
        Subject='RPL Global'
        Subject=request.POST['sub']
        contact=request.POST["contact"]
        email=request.POST["email"]
        message=request.POST["message"]
        var=models.Query(Name=name,Contact=contact,Sub=Subject,Email=email,Message=message)
        var.save()
        h=f"Thank You {name}"
        p="For reaching out to us we will get to you shortly"
        fields=models.field.objects.all()
        return render(request,'website/touch.html',{'doct':fields,'h':h,'p':p})
    else:
        fields=models.field.objects.all()
        h="Error"
        p="Due to some reasons your query is not registered with us, Please Try again or mail us as 'xyz@gmail.com' "
        return render(request,'website/touch.html',{'doct':fields,'h':h,'p':p})
def founders(request):
    fields=models.field.objects.all()
    founder=models.Know_Your_Founder.objects.all()
    return render(request,'website/Founders.html',{'doct':fields,'founder':founder})   
    