# Sonnet Class
# All processing involving an individual sonnet can be done here.

class Sonnet(object):

    def __init__(self, sonnet_text):
        self.sonnet_text = sonnet_text  #sonnet_text is a list of len 14
        self.first_twelve = sonnet_text[:-2] # list of first 12 lines
        self.couplet = map(lambda txt: txt.strip(), sonnet_text[-2:]) # rhyming couplet
