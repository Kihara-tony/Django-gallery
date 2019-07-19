from django.shortcuts import render

# Create your views here.
def gallery(request):
    all_pic = Image.all_pics()
    print(all_pics)
    return render(request,'gallery.html',{"all_pics":all_pics})
def search_results(request):
    if 'image' in request.GET and request.GET['image']:
        search_input =request.GET.get('image')
        searched_images =Image.search_by_category(search_input)
        message = f"{search_input}"
        return render(request,'search.html',{"message":message,"images":searched_images})
    else:
        message = "Please input something in the search field"
        return render(request,"search.html",{"message":message})
