# ГИПОТЕЗА: Уровень образования родителей не влияет на результат теста учащихся по математике

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('StudentsPerformance .csv')

parents = df['parental level of education'].value_counts()
print(parents)
college_mh = df[df['parental level of education'] == 'some college']['math score'].mean()
associate_mh = df[df['parental level of education'] == "associate's degree"]['math score'].mean()
highsc_mh = df[df['parental level of education'] == 'high school']['math score'].mean()
smhighsc_mh = df[df['parental level of education'] == "some high school"]['math score'].mean()
bachelor_mh = df[df['parental level of education'] == "bachelor's degree"]['math score'].mean()
master_mh = df[df['parental level of education'] == "master's degree"]['math score'].mean()

print('Родители с образованием some college:', round(college_mh, 2))
print("Родители с образованием associate's degree:", round(associate_mh, 2))
print('Родители с образованием high school:', round(highsc_mh, 2))
print('Родители с образованием some high school:', round(smhighsc_mh, 2))
print("Родители с образованием bachelor's degree:", round(bachelor_mh, 2))
print("Родители с образованием master's degree:", round(master_mh, 2))

s = pd.Series(data = [ highsc_mh, smhighsc_mh, college_mh, associate_mh, bachelor_mh, master_mh],
index = [ 'Ср. школа', "Некоторые школы", 'Колледж', 'Специалист', "Степень бакалавра", "Степень магистра" ])
s.plot(kind = 'barh')
plt.show()


# Гипотеза была опровержена