memory=[]

def add_memory(role,text):

    memory.append(
        {
            "role":role,
            "content": text
        }
    )

    #keep only last 10 message
    if len(memory)>10:
        memory.pop(0)

def get_memory():

    return memory