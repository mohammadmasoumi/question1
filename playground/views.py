from django.shortcuts import render
from django.http import HttpResponse


def products(request):
    context = {
        "data1": [
            {
                "name": "iphone 13",
                "price":  28000000,
                "img": "./iphone13.jpg"
            },
                        {
                "name": "iphone 13",
                "price":  28000000,
                "img": "a52.jpg"
            },
        ]
    }

    return render(request, "products.html", context=context)


def welcome(request):
    return HttpResponse("welcome to the Online Shop ! ")

# data = {
#     "iphone 13": 28000000,
#     "samsung s22 ultra": 25000000,
#     "samsung A52": 8000000,
#     "poco x3": 6000000,
#     "iphone se 2020": 13000000,
# }
# for x in data.values():
#     print(x)
