from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
import re

# Create your views here.
class Home(generic.TemplateView):
    template_name='base/calculadora.html'

def calculation(request):
    if request.method=="POST":
        values=request.POST['values'] #string having whole ques
        print("STEP 1-",values)
        vals=re.findall(r"(\d+)",values) #extrect values
        print("STEP 2- ",re.findall(r"(\d+)",values))
        operators=['+','x','÷','-','.','%']
        opr=[]  
        for v in values:
            for o in operators:
                if v==o:
                    print("STEP 3-", o)
                    opr.append(o)
        print(opr)                      #extrect operators
        #print(re.findall(r"(\d+)",values))

        for o in opr:
            if o=='.':
                i=opr.index(o)
                print("Step4- ", i)
                res=vals[i]+"."+vals[i+1]
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=res
                print(vals)
                print(opr)
                
            elif o=='%':
                i=opr.index(o)
                res=(float(vals[i])/100)*float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=res
                print(vals)
                print(opr)   
                
            elif o=='÷':
                i=opr.index(o)
                res=float(vals[i])/float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=str(res)
                print(vals)
                print(opr)
                
            elif o=='x':
                i=opr.index(o)
                print("Step4- ", i)
                res=float(vals[i])*float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=str(res)
                print(vals)
                print(opr)
                
            elif o=='+':
                i=opr.index(o)
                res=float(vals[i])+float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=str(res)
                print(vals)
                print(opr)
                
            elif o=='-':
                i=opr.index(o)
                res=float(vals[i])-float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=str(res)
                print(vals)
                print(opr)

        # print(opr)
        if len(opr)!=0:
            if opr[0]=='÷':
                result = float(vals[0])/float(vals[1])
            elif opr[0]=='x':
                result = float(vals[0])*float(vals[1])
            elif opr[0]=='+':
                result = float(vals[0])+float(vals[1])
            #error
            elif opr[0]=='%':
                conv_dec=float(vals[1]/100)
                valor_porc=float(vals[0])*conv_dec
                result = float(vals[0] + valor_porc)    
            else :
                result = float(vals[0])-float(vals[1])
                
        else:
            result = float(vals[0])

        final_result=round(result,2)
        print(final_result)
        # result = int(vals[0])+int(vals[1])

        # i=0
        # res=int(vals[i])
        # for operator in values:
        #     if not operator.isdigit():
        #         # print(type(int(vals[1])))
        #         # print(value)
        #         if operator=='+':
        #             res=res+int(vals[i+1])
        #         i=i+1
    res=render(request,'base/calculadora.html',{'result':final_result,'values':values})
    return res
