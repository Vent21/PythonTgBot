import g4f

g4f.debug.logging = True  # Enable logging
g4f.check_version = False  # Disable automatic version checking
# print(g4f.version)  # Check version
print(g4f.Provider.Ails.params)  # Supported args


async def ask_gpt(promt):
    try:
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.default,
            messages=[{"role": "user", "content": promt}],
        )
        if len(response) > 4095:
            return response[:4092] + "..."
        else:
            return response
    except Exception as ex:
        print(ex)
        return "Ой, я не могу ответить на этот вопрос..."
