from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import myPetText, Comment
""" from .forms import pet_form """

# Create your views here.
def home_list(request):
    petTexts = myPetText.objects.filter()

    return render(request, "MyPet_site/home_list.html", {"petTexts" : petTexts})

def pet_list(request):
    petTexts = myPetText.objects.filter()
    pop_pet = myPetText.objects.filter(category = "인기")
    cat_pet = myPetText.objects.filter(category = "고양이")
    dog_pet = myPetText.objects.filter(category = "개")

    return render(request, "MyPet_site/pet_list.html", {"petTexts" : petTexts, "pop_pet" : pop_pet, "cat_pet" : cat_pet, "dog_pet" : dog_pet})

def login(request):

    if (request.method == "POST"):
        email = request.POST["email"]
        password = request.POST["password"]
        user = auth.authenticate(request, username = email, password = password)

        if (user is None):
            print("회원가입안된사람")
            return redirect("/join")
        else:
            auth.login(request, user)
            return redirect("/")
    
    return render(request, "MyPet_site/login.html")

def join(request):

    if (request.method == "POST"):
        email = request.POST["email"]
        password = request.POST["password"]
        
        User.objects.create_user(username = email, password = password)

        return redirect("/")

    return render(request, "MyPet_site/join.html")

def logout(request):
    auth.logout(request)

    return redirect("/")

def pet_list_info(request, pk):
    board_contents = get_object_or_404(myPetText, pk = pk)
    comments = Comment.objects.filter(pet = board_contents)

    if (request.method == "POST"):
        rate = request.POST["rate"]
        comment = request.POST["comment"]

        Comment.objects.create(pet = board_contents, writer = request.user, rate = rate, comments = comment)

        return redirect("/pet_list/" + str(pk))

    return render(request, "MyPet_site/pet_list_info.html", {"board_contents" : board_contents, "comments" : comments})

def comment_remove(request, pk):
    
    if (request.method == "POST"):
        Comment.objects.get(pk = pk).delete()
    
    return redirect("/pet_list")

""" def create_pet(request):
    
    pet_create_form = pet_form()

    return render(request, "MyPet_site/create_pet.html", {"pet_create_form" : pet_create_form}) """

def show_pet_video(request, pk):
    board_contents = get_object_or_404(myPetText, pk = pk)

    return render(request, "MyPet_site/show_pet_video.html", {"board_contents" : board_contents})