import openai

openai.api_key = "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"

# Peça ao usuário para fornecer o nome do prato
recipe_name = input("Digite o nome do prato: ")

# Crie a solicitação para gerar uma receita
user_input = f"Crie uma receita de {recipe_name}"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": user_input}],
    max_tokens=150  # Limite a resposta para evitar receitas muito longas
)

# Exibir a receita gerada
print(completion.choices[0].message.content)

