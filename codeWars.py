# find_needle

def find_needle(haystack):
    return 'found the needle at position %d' % haystack.index('needle')

def find_needle(haystack):
    for i in range(0, len(haystack)):
        if haystack[i] == 'needle':
            return "found the needle at position %s" % (i)

