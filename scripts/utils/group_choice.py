

class Rules(object):

    @staticmethod
    def majority(ranks):
        pass
    
    @staticmethod
    def borda(ranks):
        n = len(ranks[0])
        scores = [0]*n
        for rank in ranks:
            for (i, r) in enumerate(rank):
                scores[i] += n - r
        return sorted(range(len(scores)),key=lambda x:n-scores[x])