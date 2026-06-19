import os
import json

from groq import Groq
from dotenv import load_dotenv


load_dotenv()

client = Groq(
    api_key=os.getenv(
        "GROQ_API_KEY"
    )
)


def get_intent(command):

    response = (
        client.chat.completions.create(
            model="llama-3.1-8b-instant",

            messages=[

                {
                    "role": "system",

                    "content": """
You classify Windows assistant commands.

Return JSON only.

Format:

{
 "intent":"greeting|time|open_app|exit|unknown",
 "value":null
}

Examples:

hello
→
{"intent":"greeting","value":null}

what time is it
→
{"intent":"time","value":null}

open chrome
→
{"intent":"open_app","value":"chrome"}

exit
→
{"intent":"exit","value":null}

goodbye
→
{"intent":"exit","value":null}

quit
→
{"intent":"exit","value":null}
"""
                },

                {
                    "role": "user",
                    "content": command
                }

            ]
        )
    )

    output = (
        response
        .choices[0]
        .message
        .content
        .strip()
    )

    output = (
        output
        .replace(
            "```json",
            ""
        )
        .replace(
            "```",
            ""
        )
        .strip()
    )

    return json.loads(output)