from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    context = {"number": 101,
               "isim": "Franz Kafka",
               "diller": ["Python", "Java", "C#", "JavaScript"],
               }
    return render(request, "article/index.html", context)


def about(request):
    return render(request, "about.html")


def detail(request, id):
    return HttpResponse("Detail Page:" + str(id))
