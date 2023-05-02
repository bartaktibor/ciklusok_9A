import pandas as pd

if __name__ == '__main__':
    diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
    ##print(diamonds)

    ##print(diamonds['carat'])

    sum = 0
    for i in diamonds['carat']:
        sum += i
    print('karát összesen: ' + str(sum))

    darabszam = diamonds['carat'].count()
    print('darabszám: '+ str(darabszam))

    lista = []


    atlag = sum / darabszam
    print('átlag: ' + str(atlag))
    ##for i in diamonds['carat']:
    ##    if atlag > i:
    ##        result = diamonds.loc[diamonds['carat'] == i]
    ##        print(result)

    ##for gyemant in diamonds.iterrows():
    ##  carat = gyemant[1]['carat']
    ##  if (carat > atlag):
    ##      print("")

    szam = 0

    for gyemant in diamonds.iterrows():
        color = gyemant[1]['color']
        price = gyemant[1]['price']
        if color == 'H':
            szam += price
            #print(gyemant)

    print("Összes ára: " + str(szam))

