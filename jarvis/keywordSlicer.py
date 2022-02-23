def identifier(txt, keyword='jarvis'):
    con = txt.find(keyword)
    print(con)
    if con != -1:  # if con (condition for 'jarvis' in string) == true then,
        print(txt)
        print(type(txt))
        print()
        txt = txt.replace(keyword, '')
        print(txt)
        print(type(txt))
        print()
        txt = list(txt)
        print(txt)
        print(type(txt))
        print()
        if txt[0] == ' ':
            txt[0] = ''
        print(txt)
        print(type(txt))
        print()
        if txt[-1] == ' ':
            txt[-1] = ''
        print(txt)
        print(type(txt))
        print()
        # txt = ' '.join([str(elem) for elem in txt]) # Letters with space in between
        txt = ''.join([str(elem) for elem in txt])
        print(txt)
        print(type(txt))
        print()
        return txt

    elif con == -1:
        pass
        return False
    else:  # It only return 0 or 1, so this will almost never be needed
        print('ERROR... MISINTERPRETTING SPEECH')
        return False


if __name__ == '__main__':
    v = identifier('jarvis run chrome')
    print(v)
