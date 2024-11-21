import openai
import json


class AIChatGenerator:
    def __init__(self, model="gpt-3.5-turbo", api_key=None):
        if api_key:
            openai.api_key = api_key
        self.model = model
        self.__output = None

    def generate_transformations(self, user_input: str):
        prompt = f"""You are a data analysis assistant. Based on the user's request, generate a structured sequence of Pandas DataFrame transformations in JSON format.
        Each transformation should have:
        - action: (filter_by_predicate, select_columns, add_computed_column)
        - parameters: JSON object with relevant keys for the action.

        User Request: {user_input}

        Example output:
        [
            {{
                'action': 'filter_by_predicate',
                'parameters': {{'column': 'age', 'predicate': 'gt', 'value': 30}}
            }},
            {{
                'action': 'select_columns',
                'parameters': {{'columns': ['name', 'age']}}
            }}
        ]

        Provide only the JSON output."""

        response = openai.chat.completions.create(
            model=self.model,
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": prompt}]
        )

        try:
            output = response.choices[0].message.content.strip()
            self.__output = output
            transformations = json.loads(output)
            return transformations
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse the response as JSON: {self.__output}") from e
