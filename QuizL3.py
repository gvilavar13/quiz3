import requests
import  json
import  sqlite3
name=input("cocktail name: ")
##Harvey Wallbanger ,Martini,Horse's Neck,margarita...
url = f'https://thecocktaildb.com/api/json/v1/1/search.php?s={name}'
r = requests.get(url)


result_json = r.text
res = json.loads(result_json)
res_structured = json.dumps(res, indent=4)
# print(r)
# print(r.headers)
print(res_structured)
# print(res)

b=res['drinks']
a=b[0]
fname=a['strDrink']
instr=a['strInstructions']
photo=a['strDrinkThumb']

strIngredient1=a['strIngredient1']
strIngredient2=a['strIngredient2']
strIngredient3=a['strIngredient3']


print("cocktail name: " ,fname)
print(instr)
print("photo link :",photo)



conn = sqlite3.connect("cocktail.sqlite")
cursor = conn.cursor()


cursor.execute('''CREATE TABLE cocktaill

(id INTEGER PRIMARY KEY AUTOINCREMENT,
fname VARCHAR(50),
ingredient1 VARCHAR(50),
ingredient2 VARCHAR(50),
ingredient3 VARCHAR(50),
photolink varchar(50));''')




cursor.execute("INSERT INTO cocktaill ( fname, ingredient1, ingredient2,ingredient3,photolink) VALUES ( ?,?,?,?,?)",(fname,strIngredient1,strIngredient2,strIngredient3,photo))


conn.commit()
conn.close()