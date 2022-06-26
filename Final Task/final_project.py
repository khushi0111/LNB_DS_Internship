# -*- coding: utf-8 -*-
"""Final Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Cfy4YuEosI9iNfJz-nNYsg8D_H7eVYck

DS404 Khushi Agarwal

Implementing n number of features in the application
"""

import pickle
from pip import main

def menu():
    print("---------------------------------------------------")
    print("*****MENU BAR*****")
    print("[1] Flower species prediction")
    print("[2] Medical cost prediction")
    print("[3] Profit prediction")
    print("[4] Breast cancer prediction")
    print("[0] EXIT")
    print("---------------------------------------------------")

    choice=int(input("\nEnter your Choice : "))
    while(check(choice)):
        if(choice==1):
            flower()
        elif(choice==2):
            medical()
        elif(choice==3):
            profit()
        elif(choice==4):
            cancer()
        else:
            print("\nAPPLICATION CLOSED")
            print("\n****THANK YOU FOR YOUR VISIT****\n")
            exit()

# checking for valid choice choosed by user
def check(choice):
    if(choice >= 0 and choice <= 4):
        return True
    else:
        print("\n******INVALID CHOICE******\n")
        return False


# below will load all saved model one by one as per asked by user
# ask for required input paramter for making prediction

#================================================================================

#======================FLOWER SPECIES PREDICTION=================================
def flower():
    sepal_length=float(input("Enter sepal length: "))
    sepal_width=float(input("Enter sepal width: "))
    petal_length=float(input("Enter petal length: "))
    petal_width=float(input("Enter sepal width: "))
    lst=[[sepal_length,sepal_width,petal_length,petal_width]]
    with open("model1","rb") as f:
        m1=pickle.load(f)
    value=m1.predict(lst)
    print("Prediction: ",value)
    menu()
#================================================================================

#==============MEDICAL INSURANCE PREDICTION======================================
def medical():
    age=int(input("Enter Age: "))
    sex=int(input("Enter sex(Male = 1, Female = 0): "))
    bmi=float(input("Enter BMI: "))
    child=int(input("Enter no. of child: "))
    smoker=int(input("Press [1] if you smoke, else Press [0]: "))
    reg=int(input("Enter region(South-west=3, South-east=2, North-west=1, North-east=0): "))
    lst=[[age,sex,bmi,child,smoker,reg]]

    with open("model2","rb") as f:
        m2=pickle.load(f)
    value=m2.predict(lst)
    print("Prediction: ",value)
    menu()
#================================================================================

#================PROFIT PREDICTION===============================================
def profit():
    spend1=float(input("Enter R&D spend : "))
    admr=float(input("Enter Administration : "))
    spend2=float(input("Enter Marketing Spend : "))
    print("press[0] for California, press[1] for Florida, press[2] for New York")
    state=int(input("Enter State : "))
    test=[[spend1,admr,spend2,state]]

    with open("model3","rb") as f:
        m3=pickle.load(f)
    value=m3.predict(test)
    print("Prediction: ",value)
    menu()
#================================================================================

#=======================BREAST CANCER PREDICTION=================================
def cancer():
    mr=float(input("Enter mean radius: "))
    mt=float(input("Enter mean texture: "))
    mp=float(input("Enter mean perimeter: "))
    ma=float(input("Enter mean area: "))
    ms=float(input("Enter mean smoothness: "))
    
    lst=[[mr,mt,mp,ma,ms]]
    with open("model4","rb") as f:
        m4=pickle.load(f)
    value=m4.predict(lst)
    if value==1:
        print("Prediction: Yes")
    else:
        print("Prediction: No")
    menu()
#================================================================================

#===========END============END==============END=================END==============
if __name__ == "__main__":
    menu()

#==================THANK YOU=====================================================