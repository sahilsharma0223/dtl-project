import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np  # linear algebra
import warnings
warnings.filterwarnings("ignore")
from django.shortcuts import render



def home(request):
    return render(request, 'index.html')

def recommend(request):
    return render(request, 'recommend.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def faq(request):
    return render(request, 'faq.html')

def services(request):
    return render(request, 'services.html')

def output(request):
    inp1=request.POST.get('p1')
    inp2=request.POST.get('p2')
    inp3=request.POST.get('p3')
    inp4=request.POST.get('p4')
    inp5=request.POST.get('p5')
    inp6=request.POST.get('p6')
    inp7=request.POST.get('p7')
    inp8 = request.POST.get('p8')
    inp1=int(inp1)
    inp2 = int(inp2)
    inp3=int(inp3)
    inp4=int(inp4)
    inp5=int(inp5)
    inp6=int(inp6)
    inp7=int(inp7)
    inp8=int(inp8)
    model = pickle.load(open('classifier.pkl', 'rb'))
    ans = model.predict([[inp1, inp2, inp3,inp4 , inp5, inp6, inp7, inp8]])
    if ans[0] == 0:
        data="10-26-26"
    elif ans[0] == 1:
        data="14-35-14"
    elif ans[0] == 2:
        data="17-17-17	"
    elif ans[0] == 3:
        data="20-20"
    elif ans[0] == 4:
        data="28-28"
    elif ans[0] == 5:
        data="DAP"
    else:
        data="Urea"

    return render(request,'recommend.html',{'data':data})
