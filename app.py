from flask import Flask, request, jsonify
from retriever import query_discovery
from translator import translate_to_english, translate_from_english
from dotenv import load_dotenv
import os
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.auth import IAMTokenManager

app = Flask(__name__)
load_dotenv()

# IBM Watsonx Granite Setup
api_key = os.getenv("IBM_API_KEY")
project_id = os.getenv("DISCOVERY_PROJECT_ID")

token_manager = IAMTokenManager(
    api_key=api_key,
    url="https://iam.cloud.ibm.com/identity/token"
)

model = ModelInference(
    model_id="ibm/granite-13b-chat-v1",
    project_id=project_id,
    url="https://us-south.ml.cloud.ibm.com",
    token_manager=token_manager
)

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    question = data.get("question", "")
    lang = data.get("language", "en")

    if not question:
        return jsonify({"error": "Question is required"}), 400

    # Translate question to English
    translated_q = translate_to_english(question) if lang != 'en' else question

    # Retrieve relevant context
    context = query_discovery(translated_q)

    # Format prompt
    with open("prompt_template.txt") as f:
        prompt_template = f.read()
    final_prompt = prompt_template.format(context=context, question=translated_q)

    # Generate answer
    response = model.generate(prompt=final_prompt, decoding_method="greedy", max_new_tokens=200)
    answer = response['results'][0]['generated_text'].strip()

    # Translate answer back if needed
    final_answer = translate_from_english(answer, lang) if lang != 'en' else answer

    return jsonify({
        "question": question,
        "answer": final_answer,
        "language": lang
    })

if __name__ == '__main__':
    app.run(debug=True)
