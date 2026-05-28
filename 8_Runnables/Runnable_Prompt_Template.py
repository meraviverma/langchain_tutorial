class Runnable_Prompt_Template:
    def __init__(self,template,input_variables):
        self.template=template
        self.input_variables=input_variables

    def format(self,input_dict):
        return self.template.format(**input_dict)
    
if __name__ == "__main__":
    template=Runnable_Prompt_Template(
        template='write a {length} poem about {topic}',
        input_variables=['length','topic']
    )

    print(template.format({'length':'short','topic':'india'}))