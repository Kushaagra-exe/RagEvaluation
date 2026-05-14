from helper import get_llm
from langchain_core.prompts import PromptTemplate
from structure import Generated_qna


class Queries:
    def __init__(self) -> None:
        
        self.llm = get_llm(model='gemini').with_structured_output(Generated_qna)

        self.prompt = PromptTemplate(
            input_variables=["information"],
            template="""
            You are a teacher expert at creating questions for a test.
            Your job is to generate questions for a test.
            You will be given some information about a certain topic.
            Your job is to create a question and an answer.
            Make sure the question and the answer is grounded from the information provided to you.
            Do not use any information in the question and answer that is not present in the given information.
            Grounded Information:
            {information}
            """
        )

    def generate(self, info):
        formatted_prompt = self.prompt.format(information=info) 
        # print(formatted_prompt, '\n--------')       
        response = self.llm.invoke(formatted_prompt)
        # print(response,'\n--------')
        # print(response)
        return response


if __name__== '__main__':
    a = Queries()
    doc = '''Quantum computing, defined
Quantum computing is an emergent field of computer science and engineering that harnesses the unique qualities of quantum mechanics to solve problems beyond the ability of even the most powerful classical computers.

The field of quantum computing includes a range of disciplines, including quantum hardware and quantum algorithms. While still in development, quantum technology will soon be able to solve complex problems that classical supercomputers can’t solve (or can’t solve fast enough).

By taking advantage of quantum physics, large-scale quantum computers would be able to tackle certain complex problems many times faster than modern classical machines. Quantum computers have the potential to solve certain problems in minutes or hours that would otherwise take conventional machines millennia to complete.

Quantum mechanics, the study of physics at small scales, reveals surprising fundamental natural principles. Quantum computers specifically harness these phenomena to access mathematical methods of solving problems not available with classical computing alone.

Practical applications for quantum computing
In practice, quantum computers are expected to be broadly useful for two types of tasks: modeling the behavior of physical systems and identifying patterns and structures in information.

Quantum mechanics is a bit like the operating system of the universe. A computer that uses quantum mechanical principles to process information has certain advantages in modeling physical systems. Therefore, quantum computing is of particular interest for chemistry and material science applications. For example, quantum computers might help researchers seeking useful molecules for pharmaceutical or engineering applications identify candidates more quickly and efficiently.
'''
    a.generate(doc)
    # print(a)