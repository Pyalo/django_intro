import scores
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, template_name='homepage.html')

def about(request):
    scores = [{"names":"Jaden Vaughn","english":57,"math":37,"chemistry":48,"biology":56},{"names":"Sigourney Brewer","english":31,"math":21,"chemistry":82,"biology":83},{"names":"Kirestin Goff","english":45,"math":31,"chemistry":58,"biology":75},{"names":"Britanni Ray","english":43,"math":66,"chemistry":41,"biology":67},{"names":"Penelope Clarke","english":40,"math":38,"chemistry":72,"biology":64},{"names":"Imelda Mejia","english":65,"math":36,"chemistry":83,"biology":66},{"names":"Aidan Erickson","english":70,"math":70,"chemistry":46,"biology":84},{"names":"Sebastian West","english":57,"math":29,"chemistry":77,"biology":57},{"names":"Keelie Craig","english":55,"math":62,"chemistry":69,"biology":79},{"names":"Kerry Brown","english":56,"math":32,"chemistry":55,"biology":81}]
    data = {
        'scores': scores,
    }
# for student in scores: student['total'] = (
#     student['english'] + student['math'] + student['chemistry'] + student['biology']
# )
# data = {'scores': scores,}

    return render(request, template_name='about.html', context=data)

def products(request):
    age = 74
    weight = 50
    subjects = ['Math', 'English', 'History', 'French']
    isDisable = False
    name = "Omera James"
    data = {
        'age': age,
        'weight': weight,
        'subject': subjects,
        'isDisable': isDisable,
        'name': 'Omera James'
    }
    return render(request, template_name='products.html', context=data)

# .gitignore tells github not to upload
# requirements.txt


#download a professional Bootstrap template
#convert it to django project by creating new project

