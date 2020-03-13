from django.shortcuts import render
import random


def home(request):
    return render(request, "generator/home.html")


def password(request):
    chars = list("qwertyuiopasdfghjklzxcvbnm")

    if request.GET.get("uppercase"):
        chars_uppercase = [char.upper() for char in chars]
        chars.extend(chars_uppercase)
    if request.GET.get("numbers"):
        numbers = list("0123456789")
        chars.extend(numbers)
    if request.GET.get("special"):
        special = list("!@#$%^&*()_+=")
        chars.extend(special)

    length = int(request.GET.get("length"))
    gen_password = ''
    for i in range(length):
        gen_password += random.choice(chars)
    return render(request, "generator/password.html", {"password": gen_password})


def about(request):
    return render(request, "generator/about.html")
