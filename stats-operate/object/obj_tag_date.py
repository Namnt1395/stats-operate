class ObjTagDate:
    cpm7 = 0
    ctr7 = 0.0
    tagId = 0
    adId = 0
    revReal = 0
    click = 0
    imp = 0
    date = ""

    def __init__(self, tagId, adId, revReal, click, imp):
        self.tagId = tagId
        self.adId = adId
        self.revReal = revReal
        self.click = click
        self.imp = imp
