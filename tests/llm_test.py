from utils.llm_wrapper import query_llm
from utils.load_txt import load_prompt

def test_llm(user_text):

    print("user_input :", user_text)
    
    prompt = load_prompt("prompt.txt", user_text)
    response = query_llm(prompt)
    print("LLM response: ", response)

if __name__ == "__main__":
    user_inputs = ["rise", "land", "move", "takeoff", "go up", "to the ground", "don't move", "hello", "go left", "crash", "stop", "this is amazing", "go forward 10m, go down 1m and rotate 45deg, go up 25m full speed"]
    for input in user_inputs:
        test_llm(input)