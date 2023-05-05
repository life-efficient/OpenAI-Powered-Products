import openai

# Setting the API key
openai.api_key = "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"


def get_completion(prompt):

    # Getting a completion
    # response = openai.ChatCompletion.create(
    #     engine="gpt-3.5-turbo",
    #     prompt=prompt,
    #     temperature=0,
    #     max_tokens=100,
    #     top_p=1,
    #     frequency_penalty=0,
    #     presence_penalty=0,
    #     # stop=["\n"]
    # )
    # Getting a chat response
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    prediction = completion.choices[0].message["content"]
    return prediction
