import objgraph
from pympler import tracker
if __name__=="__main__":
    x = []
    y = [x, [x], dict(x=x)]
    objgraph.show_refs([y], filename='sample-graph.png')
    objgraph.show_backrefs([x], filename='sample-backref-graph.png')
    objgraph.show_most_common_types(limit=20)
    tr = tracker.SummaryTracker()
    tr.print_diff()
