import nltk
import mwapi
from revscoring.features import wikitext,revision_oriented,temporal
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


features = [
    # Catches long key mashes like kkkkkkkkkkkk
    wikitext.revision.diff.longest_repeated_char_added,
    # Measures the size of the change in added words
    wikitext.revision.diff.words_added,
    # Measures the size of the change in removed words
    wikitext.revision.diff.words_removed,
    # Measures the proportional change in "badwords"
    english.badwords.revision.diff.match_prop_delta_sum,
    # Measures the proportional change in "informals"
    english.informals.revision.diff.match_prop_delta_sum,
    # Measures the proportional change meaningful words
    english.stopwords.revision.diff.non_stopword_prop_delta_sum,
    # Is the user anonymous
    revision_oriented.revision.user.is_anon,
    # Is the user a bot or a sysop
    revision_oriented.revision.user.in_group({'bot', 'sysop'}),
    # How long ago did the user register?
    temporal.revision.user.seconds_since_registration
]


api_extractor = api.Extractor(session)
for rev_id in reverts:
    print("https://en.wikipedia.org/wiki/?diff={0}".format(rev_id))
    print(list(api_extractor.extract(rev_id, features)))

print('test')
