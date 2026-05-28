import random
class Runnable_Dummy:
    def __init__(self):
        print("Runnable_Dummy initialized.")

    def predict(self,prompt):
        response_list=[
            'Delhi is the capital of India.',
            'The Great Wall of China is visible from space.',
            'The Earth is flat.',
        ]
        return random.choice(response_list)

if __name__ == "__main__":
    dummy = Runnable_Dummy()
    prompt = "What is the capital of India?"
    response = dummy.predict(prompt)
    print(f"Prompt: {prompt}")
    print(f"Response: {response}")