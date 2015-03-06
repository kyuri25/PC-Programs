# code = utf-8


def how_similar(this, that):
    import difflib
    if this is None:
        this = ''
    if that is None:
        that = ''
    return difflib.SequenceMatcher(None, this.lower(), that.lower()).ratio()


def similarity(items, text, min_ratio=0):
    r = {}
    for item in items:
        rate = how_similar(item, text)
        if rate > min_ratio:
            if not rate in r.keys():
                r[rate] = []
            r[rate].append(item)
    return r


def most_similar(similarity):
    r = []
    ratio_list = similarity.keys()
    if len(ratio_list) > 0:
        ratio_list = sorted(ratio_list)
        ratio_list.reverse()
        highiest = ratio_list[0]
        r = similarity[highiest]

    return r