from scripts.handlers import handler
from scripts.models.ranking import Ranking

'''
RankBlock
{
    type: short | full,
    id: ''
    user:''
    created: datetime
    title: '',
    description: '',
    img: 'address',
    like: 'num',
    votes: '',
    rank_items: [];
}

RankItem
{
    id: '',
    type: '',
    name: '',
    score: ''
    content: '' (for type full)
    
}
'''

TYPES = ["full", "short"]

class RankBlock(handler.Handler):

    def get(self):
        type = self.request.get("type")
        if (type not in TYPES):
            self.error(400)
            return
        fetch = int(self.request.get("fetch"))
        offset = int(self.request.get("offset"))
        rankings = Ranking.all().order('-created').fetch(limit=fetch, offset=offset)
        response = []
        for ranking in rankings:
            response_rank = {}
            response_rank["type"] = type
            response_rank["user"] = ranking.user.name
            response_rank["created"] = ranking.created.strftime("%Y-%m-%d %H:%M:%S")
            response_rank["id"] = ranking.get_id()
            response_rank["title"] = ranking.title
            response_rank["description"] = ranking.description
            response_rank["likes"] = ranking.number_of_likes
            response_rank["votes"] = ranking.number_of_votes
            response_rank["rank_items"] = []
            items = ranking.get_items()
            for (i, item) in enumerate(items):
                response_item = {}
                response_item["id"] = item.get_id()
                response_item["type"] = type
                response_item["title"] = item.name
                response_item["score"] = i
                if type == "full":
                    response_item["content"] = item.content
                response_rank["rank_items"].append(response_item)
                    
            response.append(response_rank)
        self.write(response)
        