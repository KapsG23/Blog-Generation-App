from src.states.blog_state import BlogState
from langchain_core.messages import SystemMessage,HumanMessage
from src.states.blog_state import Blog   ## My llm should structure in the form which is given in the Blog method in blog_state.

class BlogNode:
    """
    A class to represent the blog node.
    """

    def __init__(self,llm):
        self.llm = llm
    
    def title_creation(self,state:BlogState):
        """
        Create the title for the blog.
        """
        if "topic" in state and state["topic"]:
            prompt = """You are expert blog content writer. Use markdown formatting. Generate a blog title for the {topic}. This title should be creative and SEO friendly."""

            ## In the prompt we are giving to the system or LLM has the topic based on the state["topic"] or which we give in our appn.
            system_message = prompt.format(topic = state["topic"])
            ## now we invoked the llm with the system_message.
            response = self.llm.invoke(system_message)
            ## return it to the title in blog_state.
            return {"blog":{"title":response.content}}
        
    ## output will be generated from the title creation.
    def content_generation(self,state:BlogState):
        if "topic" in state and state["topic"]:
            system_prompt = """You are an expert blog writer. Use markdown formatting. Generate a detailed blog content with detailed breakdown for the {topic}."""
            system_message = system_prompt.format(topic = state["topic"])
            response = self.llm.invoke(system_message)
            ## with respect to title and content.
            return {"blog":{"title":state["blog"]["title"],"content":response.content}}
    
    def route(self,state:BlogState):
        return {"current_language":state["current_language"]}
    
    def route_decision(self,state:BlogState):
        """Route the content to the respective translation function."""
        if state["current_language"] == "hindi":
            return "hindi"
        elif state["current_language"] == "french":
            return "french"
        else:
            return state["current_language"]
    
    def translation(self,state:BlogState):
        """Translate the content to the specified language."""
        translation_prompt = """Translate the following content into {current_language}.
        - Maintain the original tone, style, and formatting.
        - Adapt cultural references and idioms to be appropriate for {current_language}.
        ORIGINAL CONTENT:{blog_content}"""

        print(state["current_language"])
        blog_content = state["blog"]["content"]
        messages = [HumanMessage(translation_prompt.format(current_language = state["current_language"], blog_content = blog_content))]
        translation_content = self.llm.with_structured_output(Blog).invoke(messages)
        return {"blog":{"content":translation_content}}
        ### whatever the llm gives it will be in the form of structure which is defined or given in the Blog and all of it will be invoked from the messages in the format given above.
        ### It is going to convert the messages from above and convert it into a structured output in the format given in Blog (in blog_state) and will be stored in translation_content.
        