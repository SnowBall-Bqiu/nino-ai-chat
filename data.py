import json

def load_data() -> dict[str]:
    '''
    从数据库和环境变量加载数据。
    '''
    return {
        'context': json.load(open('data/context.json', encoding='UTF-8')),
        'memory':  json.load(open('data/memory.json', encoding='UTF-8')),
        'config':  json.load(open('data/config.json', encoding='UTF-8')),
        'env':     json.load(open('env.json', encoding='UTF-8'))
    }

def add_data(mode: str, new_data: str) -> None:
    '''
    添加新数据到数据库。
    
    :param mode: 添加到哪个数据库？（取值`'context'`、`'memory'`）
    :param new_data: 要添加的数据。

    注意：修改config数据库请使用`update_config()`
    '''
    if mode == 'context':
        context_list = load_data()['context']
        if len(context_list) == 30:
            del context_list[0]
        context_list.append(new_data)
        json.dump(context_list, open('data/context.json', mode='w', encoding='UTF-8'))
    elif mode == 'memory':
        memory_list = load_data()['memory']
        memory_list.append(new_data)
        json.dump(memory_list, open('data/memory.json', mode='w', encoding='UTF-8'))
    else:
        raise TypeError('Can only accept the string "context" and "memory"')

def remove_data(mode: str, target: str | None = None) -> None:
    '''
    从数据库删除数据。
    
    :param mode: 删除哪个数据库里的数据？（取值`'context'`、`'memory'`）\n
    :param target: 需要删除的数据的完整字符串。（当mode为`'context'`时无需传入，**因为会删除所有上下文数据**。）

    注意：修改config数据库请使用`update_config()`
    '''
    if mode == 'context':
        context_list = load_data()['context']
        context_list = []
        json.dump(context_list, open('data/context.json', mode='w', encoding='UTF-8'))
    elif mode == 'memory':
        memory_list = load_data()['memory']
        memory_list.remove(target)
        json.dump(memory_list, open('data/memory.json', mode='w', encoding='UTF-8'))
    else:
        raise TypeError('Can only accept the string "context" and "memory"')

def update_config(key: str, value: str) -> None:
    '''
    修改config数据库里的数据。
    
    :param key: 需要修改的键。
    :param value: 需要修改的值。
    '''
    config = load_data()['config']
    if key not in config:
        raise KeyError('Key not found')
    config[key] = value
    json.dump(config, open('data/config.json', mode='w', encoding='UTF-8'))