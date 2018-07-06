"""
author : takafumihoriuchi
created in July of 2018
"""

from nltk import Tree


class TreeGenerator(object):
	
	def __init__(self, chart):
		self.chart = chart


	def get_tree(self):
		passive_edges = self.__extract_passive_edges(self.chart)
		return []


	# edge = (rule, dot_progress, begin_idx, dot_idx)
	def __extract_passive_edges(self, chart):
		passive_edges = []
		for edge in chart:
			if (self.__is_complete(edge)):
				passive_edges.append(edge)
		return passive_edges


    # HACK: want to share this function with Parser class
    # returns True if edge is passive, False if active
	def __is_complete(self, edge):
		rhs_length = len(edge[0].rhs())
		dot_progress = edge[1]
		return (rhs_length == dot_progress)



"""

    # returns a list of trees, each in "nltk.tree.Tree" type
    def __make_trees(self, tokens):
        # get a list of passive edges
        passive_edges = []
        for edge in self.chart:
            if (self.__is_complete(edge)):
                passive_edges.append(edge)
        # get rule with start symbol on lhs
        total_arc = None
        for edge in passive_edges:
            s_check = (str(edge[0].lhs()) == str(self.start_symbol)) \
                    and (edge[2] == 0) and (edge[3] == len(tokens))
            if s_check is True:
                total_arc = edge
        if total_arc is None:
            print("failed to find successful parse")
            return
        # total_arc = (S -> NP VP, 2, 0, 7)
        # 'NP'をlhsにもつ規則を見つける。
        # 見つけた各ルールについて、dot_idxで始まって、7で終わる'VP'をlhsにもつ規則を見つける。
        progress = 0
        for rhs_total_arc in total_arc[0].rhs():
            # 'NP','VP'
            for edge in passive_edges:
                # each passive states
                if (edge[0].lhs() == rhs_total_arc) and (edge[2] == progress):
                    pass


    # this back-track method does not suffice the objective of creating a tree
    # history = [{'original': (edge), 'generated': (edge)}, {}, ..., {}]
    # edge = (rule, dot_progress, begin_idx, dot_idx)
    def __back_track_history(self, tokens, find_success=True, original_edge=None):
        if find_success:
            for pair in self.history:
                gen_edge = pair['generated']
                check = (str(gen_edge[0].lhs()) == str(self.start_symbol)) \
                        and (self.__is_complete(gen_edge)) \
                        and (gen_edge[2] == 0) \
                        and (gen_edge[3] == len(tokens))
                if check is True:
                    print("successful parse found:", gen_edge)
                    org_edge = pair['original']
                    print("generated by:", org_edge)
                    self.__back_track_history(tokens, find_success=False, original_edge=org_edge)
                    return
            print("fail to find successful parse")
            return
        # set 'find_success'=False in recursive call
        else:
            for pair in self.history:
                gen_edge = pair['generated']
                if (gen_edge == original_edge):
                    org_edge = pair['original']
                    print("generated by:", org_edge)
                    self.__back_track_history(tokens, find_success=False, original_edge=org_edge)
                    return
            print("back-track terminated")
            return
"""