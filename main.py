import io
# import yara
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()
db=[]

@app.get("/users/me")
def read_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    return {"hireme": credentials.username, "plz": credentials.password}

##Creacion de modelo de los datos
class Rulescreated(BaseModel):
    name:str="Rule name"
    rule:str="rule"
    ##no agrego ID aca porque tiene que ser un campo oculto del body request y autogenerarse secuencialmente
@app.post('/api/rule')
def create_rule(rules: Rulescreated):
    db.append(rules.dict() )
    db[(len(db)-1)]["id_rules"]=int(len(db)-1)
    return db[-1]
            

@app.get('/api/rulescreated/')
def rulescreatedbyuser():
    return db

##obtener informacion sobre regla especifica
@app.get('/api/{rule_id}')
def specific_id(rule_id=str):
    for rules in db:
        if rules["id_rules"]==rule_id:
            return rules
    raise HTTPException(status_code=404, detail="the rule doesnt exist, or maybe i cant figure it out. But if you hired me i could do it")

##eliminar regla especifica
@app.delete("/api/rulescreated/{rule_id}")
def delete_rule(rule_id:int):
    for index, rules in enumerate(db):
        if rules["id_rules"]==rule_id:
            db.pop(index)
            return {"message":"successfully eliminated the target, maybe he comes back MUAJAJAJAJAJAJAJA"}
    raise HTTPException(status_code=404, detail="Keanu Reeves cant be eliminated, because i cant find where he is #sad_Ravioli")

class Stringtoanalyze(BaseModel):
    text:str="String to analyze"
    rule_id:int="Regla a aplicar"
              
    
# @app.post('/api/analyze/text/')
# def analizadordetext(strings: Stringtoanalyze):
    # textoacargar=db[strings.rule_id]['rule']
    # rules=yara.compile(source=textoacargar)
    # f=io.StringIO(rules)
    # rules=yara.load(file=f) 
    # matches=rules.match(data=strings.text)

##no pude completarlo :C, no logre entender el funcionamiento de la extension yara para python, aunque haya leido la documentacion y preguntado en foros o en discord

