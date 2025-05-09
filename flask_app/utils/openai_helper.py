## Coding Dojo - Python Bootcamp Ene 2025
## Proyecto final
## Wavely

print("🧠 Using openai_helper.py — RELOADED!")

import openai  # Using openai 0.28.1 instead of the newer version
import os
import json

# ✅ Configure OpenAI API key (older version style)
api_key = os.getenv("OPENAI")
if not api_key:
    print("⚠️ Warning: OPENAI environment variable not found")
else:
    openai.api_key = api_key

def call_openai_with_tool(prompt: str, function_schema: list, tool_name: str) -> dict:
    """
    Calls the OpenAI ChatCompletion API using a specific tool/function.

    Parameters:
    ----------
    prompt : str
        The natural language prompt to send to the model.
    function_schema : list
        A list containing the tool/function definition following OpenAI's function calling structure.
    tool_name : str
        The name of the function/tool to explicitly call from the schema.

    Returns:
    -------
    dict
        On success: { "result": parsed_arguments_dict }
        On error:   { "error": error_message_string }
    """

    try:
        # Step 1: Send the prompt and function schema to the OpenAI chat completion endpoint
        # Using the older format for openai 0.28.1
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Using gpt-4 instead of gpt-4o since we're using an older library version
            messages=[{"role": "user", "content": prompt}],
            functions=function_schema,
            function_call={"name": tool_name}
        )

        # Step 2: Get the function call from the response (older format)
        function_call = response.choices[0].message.get("function_call")

        if not function_call:
            # If no function_call is returned, this is unexpected
            return {"error": "No function call returned by the model."}

        # Step 3: Extract and parse the arguments of the function call
        arguments_json = function_call.get("arguments", "{}")

        try:
            parsed_args = json.loads(arguments_json)
        except json.JSONDecodeError:
            return {"error": "Could not parse the function call arguments as JSON."}

        return {"result": parsed_args}

    except Exception as e:
        # Catch unexpected errors (e.g., network, auth, format issues)
        return {"error": f"OpenAI API error: {str(e)}"}
