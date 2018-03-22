from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    packages = [
	{'name':'admindjango-ckeditor-blog', 'url': 'http://pypi.python.org/pypi/admindjango-ckeditor-blog/2.0'},
	{'name':'15five-django-ajax-selects', 'url': 'http://pypi.python.org/pypi/15five-django-ajax-selects/1.5.2.155'},
	{'name':'aa_stripe', 'url': 'http://pypi.python.org/pypi/aa_stripe/0.4.1'},
	{'name':'actionform', 'url': 'http://pypi.python.org/pypi/actionform/0.04'},
    ]
    context = {
        'title': 'anand-crowdbotics-30',
        'packages': packages
    }
    return render(request, 'home/index.html', context)
