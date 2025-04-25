from app.core.config import settings
# Import necessary Langchain/LLM libraries
# from langchain.llms import OpenAI
# from langchain.chains import LLMChain
# from langchain.prompts import PromptTemplate

# Example using OpenAI (replace with your chosen LLM/framework)
# if settings.OPENAI_API_KEY:
#     llm = OpenAI(openai_api_key=settings.OPENAI_API_KEY, temperature=0.7)
# else:
#     llm = None # Handle cases where API key is not set

# Define a prompt template for project generation
PROJECT_PROMPT_TEMPLATE = """
You are an AI assistant helping an Instagram tutor generate project ideas based on follower comments.

The follower commented: "{comment_text}"

Based on this comment, generate a concise project brief suitable for a beginner/intermediate learner in the tutor's field (assume general tech/creative field if unspecified). The brief should include:
1. A clear Project Title.
2. A short Project Description (2-4 sentences).
3. Key Features/Tasks (3-5 bullet points).
4. Optional: Suggested Technologies/Tools.

Format the output clearly.

Project Brief:
"""

# project_prompt = PromptTemplate(input_variables=["comment_text"], template=PROJECT_PROMPT_TEMPLATE)
# project_chain = LLMChain(llm=llm, prompt=project_prompt) if llm else None

def generate_project_brief(comment_text: str) -> str:
    """Generates a project brief using an LLM based on the user's comment."""
    # if not project_chain:
    #     return "Error: AI Service not configured. Missing API Key?"
    try:
        # response = project_chain.run(comment_text=comment_text)

        # --- Placeholder Response --- 
        # Replace this with actual LLM call
        print(f"[AI Service] Generating brief for: {comment_text}")
        response = f"""
        Project Title: Simple Spotify Clone UI

        Project Description: Create a basic visual clone of the Spotify web player's main interface. Focus on layout and static elements. This helps practice HTML structure and CSS styling.

        Key Features/Tasks:
        *   Build the header section with logo and navigation.
        *   Create the sidebar with playlist links.
        *   Design the main content area for albums/tracks (static).
        *   Implement the bottom player controls section.

        Suggested Technologies: HTML, CSS
        """
        # --- End Placeholder --- 

        return response
    except Exception as e:
        print(f"Error generating project brief: {e}")
        # Consider more robust error handling/logging
        return f"Error: Could not generate project brief. Details: {e}" 