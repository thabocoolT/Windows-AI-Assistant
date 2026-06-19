from listener import listen
from commands import execute
from speaker import speak


speak(
    "Nova online"
)


while True:

    command = (
        listen()
    )

    if not command:
        continue


    if (
        "nova"
        in
        command
    ):

        command = (
            command
            .replace(
                "nova",
                ""
            )
            .strip()
        )


    should_close = (
        execute(
            command
        )
    )


    if should_close:

        break


print(
    "Program closed"
)