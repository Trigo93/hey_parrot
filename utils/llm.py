import ollama
from utils.load_txt import load_prompt, load_shots
from utils.drone_control import get_tools

def run_llm(user_text):
    system_prompt = load_prompt("models/prompt.txt")
    few_shot_examples = load_shots("models/shots.txt")

    messages = [{"role": "system", "content": system_prompt}] + few_shot_examples
    messages.append({"role": "user", "content": user_text})

    response = ollama.chat(
        model="mistral",
        messages=messages,
        tools=get_tools(),
    )

    if response.message.tool_calls:
        for tool_call in response.message.tool_calls:
            name = tool_call.function.name
            args = tool_call.function.arguments or {}
            print(f"🔧 Tool call: {name}({args})")
    else:
        print("🤷 No valid command detected.")

if __name__ == "__main__":
    # Tests
    user_inputs = ["rise", "land", "move", "takeoff", "go up", "to the ground", "don't move", "hello", "go left", "crash", "stop", "this is amazing", "go forward 10m and rotate 45deg, go up 25m full speed"]
    for input in user_inputs:
        print("input: ", input)
        run_llm(input)
