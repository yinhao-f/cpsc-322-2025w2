from searchGeneric import Searcher, FrontierPQ, test

class LCFSearcher(Searcher):
    """Uniform Cost Searcher for a problem.
    Paths can be found by repeatedly calling search().
    """
    frontier: FrontierPQ

    def initialize_frontier(self):
        self.frontier = FrontierPQ()

    def empty_frontier(self):
        return self.frontier.empty()

    def add_to_frontier(self, path):
        """add path to the frontier with the appropriate cost"""
        self.frontier.add(path, path.cost)

def test_lcf_searcher():
    test(LCFSearcher)

if __name__ == "__main__":
    test_lcf_searcher()
