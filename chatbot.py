from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
model_name = "Qwen/Qwen2.5-1.5B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float32,
    device_map="cpu"
)
def generate_bot_reply(user_input):
    messages = [
        {"role": "system", "content": "You are a helpful intelligent chatbot."},
        {"role": "user", "content": user_input}
    ]
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_new_tokens=200,
        do_sample=True,
        temperature=0.7,
        top_p=0.9
    )
    reply = tokenizer.decode(outputs[0], skip_special_tokens=True)
    if "assistant" in reply.lower():
        reply = reply.split("assistant")[-1].replace(":", "").strip()
    return reply
