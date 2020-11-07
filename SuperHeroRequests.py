import requests

def search_param(name, parameter ):
    reponse = requests.get('https://superheroapi.com/api/2619421814940190/search/' + name)
    data = reponse.json()['results']
    return data[0]['powerstats'][parameter]

def max_stats(all_name,parameters):
    a = dict()
    for names in all_name:
        if search_param(names, parameters) == 'null': #Добавлено, так как у некоторых персонажей не заданы характеристики
            a[names] = 0
        else:
            a[names] = search_param(names, parameters)

    def sortbyparam(inputdata):
        return int(inputdata[1])

    a = list(a.items())
    a.sort(key=sortbyparam)
    return print(f'Самая большая характеристика {parameters} у {a[-1][0]} и равна {a[-1][1]}')

max_stats(['Hulk', 'Captain America', 'Thanos', 'Green Goblin IV'  ], 'intelligence')

# Parameters var:
# intelligence
# strength
# speed
# durability
# power
# combat
