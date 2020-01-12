from django.shortcuts import render

# Create your views here.
def helloworld(request):
	context = {
			"msg": "Hello World!"
	}
	return render(request, "start.html", context)