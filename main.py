import os

from dotenv import load_dotenv
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI

load_dotenv()


def main():
    print("Hello from langchain-course!")
    information = """
Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a businessman and entrepreneur known for his leadership of Tesla, SpaceX, Twitter, and xAI. Musk has been the wealthiest person in the world since 2021; as of October 2025, Forbes estimates his net worth to be US$500 billion.

Born into a wealthy family in Pretoria, South Africa, Musk emigrated in 1989 to Canada; he had obtained Canadian citizenship at birth through his Canadian-born mother. He received bachelor's degrees in 1997 from the University of Pennsylvania in Philadelphia, United States, before moving to California to pursue business ventures. In 1995, Musk co-founded the software company Zip2. Following its sale in 1999, he co-founded X.com, an online payment company that later merged to form PayPal, which was acquired by eBay in 2002. That year, Musk also became an American citizen.
"""
    summary_template = """
    given the information {information} about a person, I want you to create:
    1. A short summary
    2. two interesting facts about the person
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
)
    
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo", 
        temperature=0
        ) # type: ignore
    chain = summary_prompt_template | llm
    response = chain.invoke({"information": information})
    print(response.content)


if __name__ == "__main__":
    main()
