def proxy_reader(fileWithPath):
        proxy_list = []
        with open(fileWithPath, 'r', newline='', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                proxy_list.append(line)
        return proxy_list