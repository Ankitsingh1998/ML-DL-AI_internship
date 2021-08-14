#Day019 - code challenge titanic
import pandas as pd

file = pd.read_csv('titanic.csv')

list(file.columns)

#total passengers survival-death analysis:
Total_passengers = len(file['Survived'])
percentage_died = file['Survived'].value_counts(normalize=True)[0]
percentage_survived = file['Survived'].value_counts(normalize=True)[1]

print('Number of passengers survived:',int(Total_passengers*percentage_survived))
print('Number of passengers died:',int(Total_passengers*percentage_died))
print('% of passengers survived:',round(100*percentage_survived,2))
print('% of passengers died:',round(100*percentage_died,2))

#male and female passengers survival-death analysis:
total_male_passengers = (file['Sex'] == 'male').value_counts()[1]
total_female_passengers = (file['Sex'] == 'female').value_counts()[1]
male_passengers_survived = file['Survived'][file['Sex'] == 'male'].value_counts(normalize=True)[1]
female_passengers_survived = file['Survived'][file['Sex'] == 'female'].value_counts(normalize=True)[1]
male_passengers_died = file['Survived'][file['Sex'] == 'male'].value_counts(normalize=True)[0]
female_passengers_died = file['Survived'][file['Sex'] == 'female'].value_counts(normalize=True)[0]
print('% of Male passengers survived:',round(male_passengers_survived*100,2))
print('% of Male passengers died:',round(male_passengers_died*100,2))
print('% of Female passengers survived:',round(female_passengers_survived*100,2))
print('% of Female passengers died:',round(female_passengers_died*100,2))

#children survival-death analysis:
def filter_age(age):
    if 0 <= age <= 18:
        return True
    else:
        return False
    
file['children'] = file['Age'].apply(filter_age)
total_children = file['children'].value_counts()[1]
total_children_survived = file['Survived'][file['children'] == True].value_counts(normalize=True)[1]
total_children_died = file['Survived'][file['children'] == True].value_counts(normalize=True)[0]
print('% of children survived:',round(total_children_survived*100,2))
print('% of children died:',round(total_children_died*100,2))

#children survival-death analysis gender comparison:
total_male_children = file['Sex'][file['children'] == True].value_counts()['male']
total_male_children_survived = file['Survived'][file['Sex'] == 'male'][file['children'] == True].value_counts(normalize=True)[1]
total_male_children_died = file['Survived'][file['Sex'] == 'male'][file['children'] == True].value_counts(normalize=True)[0]
total_female_children = file['Sex'][file['children'] == True].value_counts()['female']
total_female_children_survived = file['Survived'][file['Sex'] == 'female'][file['children'] == True].value_counts(normalize=True)[1]
total_female_children_died = file['Survived'][file['Sex'] == 'female'][file['children'] == True].value_counts(normalize=True)[0]
