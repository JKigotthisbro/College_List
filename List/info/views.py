from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
import requests
from bs4 import BeautifulSoup
from django.urls import reverse

url = 'https://www.niche.com/colleges/search/best-colleges/'
custom_header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
}
response = requests.get(url, headers=custom_header)

soup = BeautifulSoup(response.content, 'html.parser')

college_ranking = []

rank=1

for word in soup.find_all('h2'):
    info = str(rank) + ". " + word.get_text() + "\n"
    college_ranking.append(info)
    rank += 1

def index(request):
    return render(request, "listofcolleges.html",{'college_ranking':college_ranking})

class NewSchoolForm(forms.Form):
    College = forms.CharField(label="College")
    students = forms.IntegerField(label="Students", min_value=100, max_value=10000)

def addSchool(request):
    if request.method == "POST":
        form = NewSchoolForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data["College"]
            request.session["info"] += [a]
            return HttpResponseRedirect(reverse("info:index"))
        else:
            return render(request, "addSchool.html", {
                "schoolForm" : form
            })


    return render(request, "addSchool.html",{
        "schoolForm": NewSchoolForm()
    })

def deleteSchools(request):
    print(request.session["info"])
    del request.session["info"]
    return HttpResponseRedirect(reverse("info:index"))
