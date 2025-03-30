from openai import OpenAI
ollama_via_openai = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')
def summarize(url):
    website = Website(url)
    response = ollama_via_openai.chat.completions.create(
        model="deepseek-r1:1.5b",
        messages = messages_for(website)
    )
    return response.choices[0].message.content
def display_summary(url):
    summary = summarize(url)
    display(Markdown(summary))
display_summary("https://en.wikipedia.org/wiki/Novak_Djokovic")
