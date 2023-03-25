
from django.shortcuts import render
# Create your views here.
def Home(request):
    return render(request,'post/home.html')

def Login(request):
    return render(request,'post/login.html')

def Register(request):
    return render(request,'post/register.html')



# def Register(request):
#     if request.method =="POST":
#         fm =Signup(request.POST)
#         if fm.is_valid():
#             messages.success(request,"Account Create Successfully !!")
#             fm.save()
#     else:
#         fm = Signup()
#     return render(request,"post/register.html",{'form':fm})


# ## login view
# def Login(request):
#     if not request.user.is_authenticated:
#         if request.method=="POST":
#             fm = AuthenticationForm(request=request, data=request.POST)
#             if fm.is_valid():
#                 uname = fm.cleaned_data['username']
#                 upass = fm.cleaned_data['password']
#                 user =authenticate(username=uname, password=upass)
#                 if user is not None:
#                     login(request, user)
#                     messages.success(request,"Your are Successfully login !!")
#                     return HttpResponseRedirect('')
#         else:
#             fm =AuthenticationForm()        
#         return render(request,'enroll/login.html',{'form':fm})
#     else:
#         return HttpResponseRedirect("")