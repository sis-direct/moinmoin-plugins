from MoinMoin.wikiutil import get_unicode

Dependencies = []
generates_headings = False

def macro_SipLink(macro,name, alias):
	"""generate a link with a 'sip' protocol"""
	return "<a href='sip:%s>%s</a>" % (get_unicode(name), get_unicode(alias))

