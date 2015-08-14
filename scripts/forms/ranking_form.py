import json

class RankingForm(object):

    def __init__(self, ranking_json):
        content = json.loads(ranking_json)   
        self.title = content["title"] 
        self.item_names = content["item_names"]
        self.item_contents = content["item_contents"]
        self.ranks = range(0, len(self.item_names)) #TODO: get ranks from web form
        