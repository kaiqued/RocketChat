badWords = {"cú","merda","foda","caralho","puta","fdp","bosta"};

TextValidator[message_] := {message,
messageEN = TextTranslation[message],
Length[StringPosition[message,badWords]],
Classify["Sentiment",messageEN]};

TextValidator["Não estou bem hoje."]
TextValidator["A aula foi muito boa"]
TextValidator["Eu odeio salada cú foda"]


func = APIFunction[{"inputMsg" -> "String"}, TextValidator[#inputMsg] &];

api = CloudDeploy[func]

CloudObject[
https://www.wolframcloud.com/objects/2aea88f8-57b4-46f7-b0a8-2dff944906cb
]

no python:

r = requests.get("https://www.wolframcloud.com/objects/8bdd110e-181c-48d1-a95f-f376f00e3f12?inputMsg="+ mensagem)