import requests

endorsement_template= '''{
        "principal":"",
        "otherValues": ["%s", "%s", "%s"]
    }'''


def endorse(safe_url, target, key, value):
    # leave the principal field empty since MDS uses IP:port to authenticate
    return requests.post(safe_url + "/postEndorsement", data=
     endorsement_template % ('', target, key, value))


def define_tag(safe_url, speaker, tag, policy):
    # define a tag with access policy by the speaker
    return requests.post(safe_url + "/postEndorsement", data=
     endorsement_template % (speaker, tag, 'policy', policy))

