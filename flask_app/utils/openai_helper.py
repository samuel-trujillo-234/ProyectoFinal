import openai
import os
import json

# ✅ Create OpenAI client using your API key from environment variables
client = openai.OpenAI(api_key=os.getenv("OPENAI"))

def call_openai_with_tool(prompt: str, function_schema: list, tool_name: str) -> dict:
    """
    Calls the OpenAI ChatCompletion API using a specific tool/function.

    Parameters:
    ----------
    prompt : str
        The natural language prompt to send to the model.
    function_schema : list
        A list containing the tool/function definition following OpenAI's new function calling structure.
    tool_name : str
        The name of the function/tool to explicitly call from the schema.

    Returns:
    -------
    dict
        On success: { "result": parsed_arguments_dict }
        On error:   { "error": error_message_string }

    Example return:
    {
        "result": {
            "score": 1,
            "explanation": "The article contains purely factual information with clear sources."
        }
    }

    Or:
    {
        "error": "No tool call returned."
    }
    """

    try:
        # Step 1: Send the prompt and tool schema to the OpenAI chat completion endpoint
        response = client.chat.completions.create(
            model="gpt-4o",  # You can parameterize this if needed
            messages=[{"role": "user", "content": prompt}],
            tools=function_schema,
            tool_choice={"type": "function", "function": {"name": tool_name}}
        )

        # Step 2: Get the tool calls from the first response choice
        tool_calls = response.choices[0].message.tool_calls

        if not tool_calls:
            # If no tool_call is returned, this is unexpected
            return {"error": "No tool call returned by the model."}

        # Step 3: Extract and parse the arguments of the tool call
        arguments_json = tool_calls[0].function.arguments

        try:
            parsed_args = json.loads(arguments_json)
        except json.JSONDecodeError:
            return {"error": "Could not parse the tool call arguments as JSON."}

        return {"result": parsed_args}

    except Exception as e:
        # Catch unexpected errors (e.g., network, auth, format issues)
        return {"error": f"OpenAI API error: {str(e)}"}
