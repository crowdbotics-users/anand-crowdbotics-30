from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    packages = [
	{'name':'aa_stripe', 'url': 'http://pypi.python.org/pypi/aa_stripe/0.4.1'},
	{'name':'actionform', 'url': 'http://pypi.python.org/pypi/actionform/0.04'},
    ]
    context = {
        'title': 'anand-crowdbotics-30',
        'packages': packages
    }
    return render(request, 'home/index.html', context)
