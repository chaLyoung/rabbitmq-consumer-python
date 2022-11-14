import json

ttt = {"result":True,"code":None,"message":"api response success","data":[{"resortCode":"R0001","resortName":"지산포레스트","status":"N","fetchStatus":"O"},{"resortCode":"R0002","resortName":"비발디파크","status":"N","fetchStatus":"O"},{"resortCode":"R0003","resortName":"오크밸리","status":"N","fetchStatus":"O"},{"resortCode":"R0004","resortName":"하이원","status":"N","fetchStatus":"O"},{"resortCode":"R0005","resortName":"엘리시안 강촌","status":"N","fetchStatus":"O"},{"resortCode":"R0006","resortName":"용평","status":"N","fetchStatus":"O"},{"resortCode":"R0007","resortName":"덕유산","status":"N","fetchStatus":"O"},{"resortCode":"R0008","resortName":"오투리조트","status":"N","fetchStatus":"O"}],"authError":False}


print(json.dumps(ttt, indent="\t", ensure_ascii=False))