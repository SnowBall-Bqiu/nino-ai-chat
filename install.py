import os
os.system('pip install flask openai requests')
open('env.json', mode='w').write('{\n    "ai_api_key": "",\n    "weather_api_key": ""\n}')