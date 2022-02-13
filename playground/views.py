from django.shortcuts import render
from django.http import HttpResponse


def products(request):
    context = {
        "data": {
            "iphone 13": 28000000,
            "samsung s22 ultra": 25000000,
            "samsung A52": 8000000,
            "poco x3": 6000000,
            "iphone se 2020": 13000000,
        },
        "picture": {
            "iphone 13": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-13-starlight-select-2021?wid=940&hei=1112&fmt=png-alpha&.v=1629907845000",
            "samsung s22 ultra": "https://s.yimg.com/uu/api/res/1.2/G9XX5TntpTUD0PqfjSvF8Q--~B/aD0xNDQwO3c9MjU2MDthcHBpZD15dGFjaHlvbg--/https://s.yimg.com/os/creatr-uploaded-images/2022-02/229d23a0-892d-11ec-bb7f-9590b8e9d16b.cf.jpg",
            "A52": "https://image-us.samsung.com/SamsungUS/home/mobile/phones/galaxy-a52-5g/PDP-GALLERY-A52-lockup-1600x1200.jpg?$product-details-jpg$",
            "poco x3": "https://www.technolife.ir/image/color_image_TLP-2565_000000.png",
            "iphone se 2020": "https://dkstatics-public.digikala.com/digikala-products/122045214.jpg?x-oss-process=image/resize,h_1600/quality,q_80",
        }
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
