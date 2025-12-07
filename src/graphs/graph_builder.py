from langgraph.graph import StateGraph, START, END
from src.llms.groqllm import GroqLLM
from src.states.blog_state import BlogState
from src.nodes.blog_node import BlogNode


class GraphBuilder:
    def __init__(self,llm):
        self.llm = llm
        self.graph = StateGraph(BlogState)

    def build_topic_graph(self):
        """
        Build a graph to generate blogs based on topic.
        """

        self.blog_node_obj = BlogNode(self.llm)
        print(self.llm)

        ## Nodes
        self.graph.add_node("Title_Creation", self.blog_node_obj.title_creation)
        self.graph.add_node("Content_Generation",self.blog_node_obj.content_generation)

        ## Edges
        self.graph.add_edge(START, "Title_Creation")
        self.graph.add_edge("Title_Creation", "Content_Generation")
        self.graph.add_edge("Content_Generation", END)

        return self.graph
    
    def build_language_graph(self):
        """
        Build a graph for blog generation based on topic and language as inputs.
        """
        ## Nodes
        self.blog_node_obj = BlogNode(self.llm)
        print(self.llm)

        ## Nodes
        self.graph.add_node("Title_Creation", self.blog_node_obj.title_creation)
        self.graph.add_node("Content_Generation",self.blog_node_obj.content_generation)
        self.graph.add_node("Route",self.blog_node_obj.route)
        ## we are giving the state as our input.
        self.graph.add_node("Hindi_Translation", lambda state:self.blog_node_obj.translation({**state,"current_language":"hindi"}))
        self.graph.add_node("French_Translation", lambda state:self.blog_node_obj.translation({**state,"current_language":"french"}))

        ## Edges
        self.graph.add_edge(START, "Title_Creation")
        self.graph.add_edge("Title_Creation", "Content_Generation")
        self.graph.add_edge("Content_Generation", "Route")
        self.graph.add_conditional_edges("Route", self.blog_node_obj.route_decision,{"hindi":"Hindi_Translation","french":"French_Translation"})
        self.graph.add_edge("Hindi_Translation", END)
        self.graph.add_edge("French_Translation", END)

        return self.graph


    def setup_graph(self,usecase):
        if usecase == "topic":
            ## the above given function will be called.
            self.build_topic_graph()
            
        if usecase == "language":
            self.build_language_graph()
        
        return self.graph.compile()
    

## If you want to run this graph builder then you need to have and use LLM.
## Below code is for LangSmith LangGraph Studio.
llm = GroqLLM().get_llm()

## get the graph
graph_builder = GraphBuilder(llm)
graph = graph_builder.build_language_graph().compile()