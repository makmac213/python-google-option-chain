import json
import token, tokenize

from StringIO import StringIO


# using below solution fixes the json output from google
# http://stackoverflow.com/questions/4033633/handling-lazy-json-in-python-expecting-property-name
def fixLazyJson (in_text):
    tokengen = tokenize.generate_tokens(StringIO(in_text).readline)

    result = []
    for tokid, tokval, _, _, _ in tokengen:
        # fix unquoted strings
        if (tokid == token.NAME):
            if tokval not in ['true', 'false', 'null', '-Infinity', 'Infinity', 'NaN']:
                tokid = token.STRING
                tokval = u'"%s"' % tokval

        # fix single-quoted strings
        elif (tokid == token.STRING):
            if tokval.startswith ("'"):
                tokval = u'"%s"' % tokval[1:-1].replace ('"', '\\"')

        # remove invalid commas
        elif (tokid == token.OP) and ((tokval == '}') or (tokval == ']')):
            if (len(result) > 0) and (result[-1][1] == ','):
                result.pop()

        # fix single-quoted strings
        elif (tokid == token.STRING):
            if tokval.startswith ("'"):
                tokval = u'"%s"' % tokval[1:-1].replace ('"', '\\"')

        result.append((tokid, tokval))

    return tokenize.untokenize(result)


def json_decode(json_string):
    try:
        ret = json.loads(json_string)
    except:
        json_string = fixLazyJson(json_string)
        ret = json.loads(json_string)
    return ret