from flask import Flask, render_template,jsonify, request
from flask_table import Table,Col
import requests
import json

app = Flask(__name__,static_url_path='/static')

charlist = {}

class ItemTable(Table):
    charid = Col('CharID',show=False)
    charname = Col('Name')
    corporationid = Col('CorporationID',show=False)
    corporation = Col('Corporation')
    allianceid = Col('AllianceID',show=False)
    alliancename = Col('AllianceName')
    factionname = Col('FactionName',show=False)
    weekkills = Col('WklyKills')
    blopskills = Col('BlopsKills')
    secstatus = Col('SecStatus')
    lastkill = Col('LastKill')
    lastloss = Col('LastLoss')
    covertprob = Col("CovertProbability")

    kills = Col('kills')
    losses = Col('Losses')

class Item(object):
    def __init__(self,charid,charname,corporationid,corporation,allianceID, allianceName,factionname,weekkills,blopskills,secstatus,lastkill,lastloss,covertprob,kills,losses):
        self.charid = charid
        self.charname = charname
        self.corporationid = corporationid
        self.corporation = corporation
        self.allianceid = allianceID
        self.alliancename = allianceName
        self.factionname = factionname
        self.weekkills = weekkills
        self.blopskills = blopskills
        self.secstatus = secstatus
        self.lastkill = lastkill
        self.lastloss = lastloss
        self.covertprob = covertprob
        self.kills = kills
        self.losses = losses


items = []


@app.route('/')
def hello_world():  # put application's code here
    system = request.args.get('system')
    print(system)
    items = []
    print(charlist)
    print(type(charlist))
    if system in charlist:
        for c in charlist[system]:
            items.append(Item(
                charid=c[0],
                charname=c[2],
                corporationid=c[3],
                corporation=c[4],
                allianceID=c[5],
                allianceName=c[6],
                factionname=c[7],
                weekkills=c[9],
                blopskills=c[11],
                secstatus=c[15],
                lastkill=c[17],
                lastloss=c[16],
                covertprob=c[19],
                kills=c[10],
                losses=c[13]
            ))
            print(c)
        table = ItemTable(items)
        return render_template('template.html',system=system,tablelist=table.__html__())
    return "No Data!"

@app.route('/postmethod',methods=['POST'])
def postmethod():
    global charlist
    system = request.args.get('system')
    data = request.get_json()
    x = json.loads(data)
    charlist[system] = x[system]
    return(jsonify(data))

if __name__ == '__main__':
    charlist = {}

    app.run()
