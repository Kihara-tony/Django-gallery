from django.shortcuts import render

# Create your views here.
def gallery(request):
    all_pic = Image.all_pics()
    print(all_pics)
    return render(request,'gallery.html',{"all_pics":all_pics})
