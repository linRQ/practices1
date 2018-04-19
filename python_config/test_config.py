from configparser import ConfigParser

CONFIGFILE = 'python.txt'
config = ConfigParser()
config.read(CONFIGFILE)

print(config.get('messages', 'greeting'))

messages = config['messages']
print(messages)
for i in messages:
    print(i)
    print(messages[i])