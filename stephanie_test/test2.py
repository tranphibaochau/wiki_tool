import nltk
import mwapi
from revscoring.features import wikitext,revision_oriented,temporal,bytes
from revscoring.languages import english
from revscoring.extractors import api

session = mwapi.Session("https://en.wikipedia.org", user_agent="Research")

reverts = [820742102, 774370639, 797413078, 801466533, 765152913,
           820176845, 766956242, 773811199, 793358328, 808039556,
           805594987, 771430234, 813173973, 776775255, 768624607,
           786143672, 789885168, 802629289, 818211525, 767402392,
           809827513, 784991109, 819633817, 817970846, 773585253,
           798939904, 795204082, 780283639, 778482797, 771362918,
           768917631, 776000162, 787089298, 788527166, 815973673,
           776741422, 780063603, 822536336, 771364768, 811131140,
           802488558, 805418121]



features = [revision_oriented.revision.user.is_anon]

reverts_num=len(reverts)
anon = 0
registered = 0
api_extractor = api.Extractor(session)
for rev_id in reverts:
    # print("https://en.wikipedia.org/wiki/?diff={0}".format(rev_id))
    res = list(api_extractor.extract(rev_id, features))
    # print(res)

    if res[0]==True:
        anon+=1
    else:
        registered+=1

percent_anon = round((anon/reverts_num),4)*100
percent_registered = round((registered/reverts_num),4)*100
print('Percent of reverts from an anonymous editor:',anon,'/',reverts_num,'(%',percent_anon,')')
print('Percent of reverts from an registered editor:',registered,'/',reverts_num,'(%',percent_registered,')')
