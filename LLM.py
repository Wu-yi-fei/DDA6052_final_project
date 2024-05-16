from uniai import deepseekChatLLM

chatLLM = deepseekChatLLM(api_key='sk-xxxx') # use your own key

if __name__ == "__main__":

    content = "请用一个成语介绍你自己"
    messages = [{"role": "user", "content": content}]

    resp = chatLLM(messages)
    print(resp)

    for resp in chatLLM(messages, stream=True):
        print(resp)
