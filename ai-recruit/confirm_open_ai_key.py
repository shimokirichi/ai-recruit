from openai import OpenAI


def verify_openai_key(api_key):
    try:
        client = OpenAI(api_key=api_key)
        response = client.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt="Write a tagline for an ice cream shop."
                )
        print(response)
        print("OpenAI key is valid.")
    except Exception as e:
        print("OpenAI key is invalid:", str(e))


# Replace 'YOUR_API_KEY' with your actual OpenAI API key
verify_openai_key('YOUR_API_KEY')
