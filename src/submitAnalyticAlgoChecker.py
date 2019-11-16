import os
import json
import warnings
from tokenize import generate_tokens
from params import params
import logging

def algoChecker(jsonName,pyName):
    jsonFile=os.path.join("tmp",jsonName)
    pyFile=os.path.join("tmp",pyName)
    param=params()
    result=""
    acceptableType=param.dataProjectType
    acceptableLib=["sklearn","keras"]
    acceptableParamType=["int","float","bool","enum","string"]
    acceptableIOType=["float","classifiable","string","path"]
    # jsonFile=os.path.join(param.analyticServiceRoot,"core","analyticCore",dl,pl,filename+".json")
    # pyFile=os.path.join(param.analyticServiceRoot,"core","analyticCore",dl,pl,filename+".py")
    if not os.path.isfile(jsonFile):
        return f"{jsonFile} not found"
    if not os.path.isfile(pyFile):
        return f"{pyFile} not found"
    j=json.load(open(jsonFile))
    if not ("dataType" in j):
        return "dataType not defined in json"
    if not (j["dataType"] in acceptableType):
        return "dataType not supported. Check spelling"
    if not ("projectType" in j):
        return "projectType not defined in json"
    if not (j["projectType"] in acceptableType[j["dataType"]]):
        return "projectType not supported. Check spelling"
    if not ("algoName" in j):
        return "algoName not defined in json"
    if not (j["algoName"]==jsonName[:jsonName.rfind(".")]):
        return "algoName defined in json must be identical with filename"
    if not ("description" in j):
        return "description not defined in json"
    if not ("lib" in j):
        return "lib not defined in json"
    if not (j["lib"] in acceptableLib):
        return "lib not supported, Check spelling"
    if not ("param" in j):
        return "param not defined in json"
    if not (type(j["param"]) is list):
        return "param must be a list"
    for p in j["param"]:
        if not ("name" in p):
            return f"attribute 'name' missing <br>In parameter:<br>{p}"
        if not ("description" in p):
            return f"attribute 'description' missing <br>In parameter:<br>{p}"
        if not ("type" in p):
            return f"attribute 'type' missing <br>In parameter:<br>{p}"
        if not (p["type"] in acceptableParamType):
            return f"type {p['type']} not supported, check spelling.<br>In parameter:<br>{p}"
        if not ("default" in p):
            return f"attribute 'default' missing <br>In parameter:<br>{p}"
        if p["type"]=="int":
            if not ("upperBound" in p):
                return f"attribute 'upperBound' not found <br>In parameter:<br>{p}"
            if not ("lowerBound" in p):
                return f"attribute 'lowerBound' not found <br>In parameter:<br>{p}"
            if int(p["upperBound"])!=p["upperBound"]:
                return f"upperBound must be int <br>In parameter:<br>{p}"
            if int(p["lowerBound"])!=p["lowerBound"]:
                return f"lowerBound must be int <br>In parameter:<br>{p}"
            if int(p["default"])!=p["default"]:
                return f"default must be int <br>In parameter:<br>{p}"
            if p['upperBound']<=p['lowerBound']:
                return f"upperBound must be greater than lowerBound <br>In parameter:<br>{p}"
        if p["type"]=="float":
            if not ("upperBound" in p):
                return f"attribute 'upperBound' not found <br>In parameter:<br>{p}"
            if not ("lowerBound" in p):
                return f"attribute 'lowerBound' not found <br>In parameter:<br>{p}"
            if float(p["upperBound"])!=p["upperBound"]:
                return f"upperBound must be float <br>In parameter:<br>{p}"
            if float(p["lowerBound"])!=p["lowerBound"]:
                return f"lowerBound must be float <br>In parameter:<br>{p}"
            if float(p["default"])!=p["default"]:
                return f"default must be float <br>In parameter:<br>{p}"
            if not p['upperBound']>p['lowerBound']:
                return f"upperBound must be greater than lowerBound <br>In parameter:<br>{p}"
        if p["type"]=="bool":
            if not (p["default"]==1 or p["default"]==0):
                return f"default must be 0 or 1 <br>In parameter:<br>{p}"
        if p["type"]=="enum":
            if not ("list" in p):
                return f"attribute 'list' not found <br>In parameter:<br>{p}"
            if not (p["default"] in p["list"]):
                return f"default value not in list<br>In parameter:<br>{p}"
    if not ("input" in j):
        return f"input not defined in json"
    for p in j["input"]:
        if not ("name" in p):
            return f"attribute 'name' not found <br>In input:<br>{p}"
        if not ("description" in p):
            return f"attribute 'description' not found <br>In input:<br>{p}"
        if not ("type" in p):
            return f"attribure 'type' not found <br>In input:<br>{p}"
        if not (p["type"] in acceptableIOType):
            return f"type {p['type']} is not acceptable <br>In input:<br>{p}"
        if not ("amount" in p):
            return f"attribute 'amount' not found<br>In input:<br>{p}"
        if not (p["amount"] in ["multiple","single"]):
            return f"amount {p['amount']} is not acceptable<br>In input:<br>{p}"
    if not ("output" in j):
        return "output not defined in json"
    for p in j["output"]:
        if not ("name" in p):
            return f"attribute 'name' not found <br>In output:<br>{p}"
        if not ("description" in p):
            return f"attribute 'description' not found <br>In output:<br>{p}"
        if not ("type" in p):
            return f"attribure 'type' not found <br>In output:<br>{p}"
        if not (p["type"] in acceptableIOType):
            return f"type {p['type']} is not acceptable<br>In output:<br>{p}"
        if not ("amount" not in p):
            return f"output has no attribute 'amount'<br>In output:<br>{p}"
    paramList=[p["name"] for p in j["param"]]
    inputList=[p["name"] for p in j["input"]]
    outputList=[p["name"] for p in j["output"]]
    name=pyFile.replace(".py","").replace("tmp/","")
    if not(name in open(pyFile).read()):
        return f"Class name of algorithm should be identical with filename: {name}"
    g=generate_tokens(open(pyFile).readline)
    record=[]
    for typ,syn,start,end,line in g:
        if typ==1 or typ==53 or typ==3:
            record.append((typ,syn,start,end,line))
    p=[]
    i=[]
    o=[]
    for ii in range(len(record[:-3])):
        if record[ii][0]==1 and record[ii+1][0]==53 and record[ii+2][0]==3 and record[ii+3][0]==53:
            if record[ii][1]=='param':
                p.append(record[ii+2])
            if record[ii][1]=='inputData':
                i.append(record[ii+2])
            if record[ii][1]=='outputData':
                o.append(record[ii+2])
    pWarn=[]
    iWarn=[]
    oWarn=[]
    notUsedWarn=[]
    usedParam=[]
    for pp in p:
        usedParam.append(pp[1].replace(" ","").replace("'","").replace('"',""))
        if pp[1].replace(" ","").replace("'","").replace('"',"") not in paramList:
            pWarn.append(f"[Syntax] param key error at {pp[2]}~{pp[3]}: {pp[1]}<br>")
    for ii in i:
        if ii[1].replace(" ","").replace("'","").replace('"',"") not in inputList:
            iWarn.append(f"[Syntax] inputData key error at {ii[2]}~{ii[3]}: {ii[1]}<br>")
    for oo in o:
        if oo[1].replace(" ","").replace("'","").replace('"',"") not in outputList:
            oWarn.append(f"[Syntax] outputData key error at {oo[2]}~{oo[3]}: {oo[1]}<br>")
    for pp in paramList:
        if pp not in usedParam:
            notUsedWarn.append(f"[Not used] param '{pp}' defined in json is not used in python<br>")
    if len(iWarn)==0 and len(oWarn)==0 and len(pWarn)==0 and len(notUsedWarn)==0:
        import shutil
        #remove previos file
        shutil.move(jsonFile,os.path.join("src","service","analyticService","core","analyticCore",j["dataType"],j["projectType"],jsonName))
        shutil.move(pyFile,os.path.join("src","service","analyticService","core","analyticCore",j["dataType"],j["projectType"],pyName))        
        with open(param.analyticAlgoReg,"r") as file:
            reg=json.load(file)
        if j["algoName"] not in reg[j["dataType"]][j["projectType"]]:
            reg[j["dataType"]][j["projectType"]].append(j["algoName"])
        with open(param.analyticAlgoReg,"w") as file:
            json.dump(reg,file, indent=4)
        return (f"success")
    else:
        result+=(f"Algo [{j['dataType']}.{j['projectType']}.{j['algoName']}] checked with result:<br>")
        result+=(f"&nbsp;&nbsp;>&nbsp;JSON&nbsp;&nbsp;&nbsp;:&nbsp;OK<br>")
        result+=(f"&nbsp;&nbsp;>&nbsp;Python&nbsp;:&nbsp;<br>")
        result+=(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{len(pWarn)} param key warning<br>")
        for pw in pWarn:
            result+=(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-{pw}<br>")
        result+=(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{len(iWarn)} inputData key warning<br>")
        for iw in iWarn:
            result+=(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-{iw}<br>")
        result+=(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{len(oWarn)} outputData key warning<br>")
        for ow in oWarn:
            result+=(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-{ow}<br>")
        result+=(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{len(notUsedWarn)} not used param warning<br>")
        for nw in notUsedWarn:
            result+=(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-{nw}<br>")
    # result+=("---------------------------------------------------<br>")
    return result
if __name__=="__main__":
    algoChecker()