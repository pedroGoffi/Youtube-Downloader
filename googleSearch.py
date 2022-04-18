from __future__ import annotations
def getUrlFromTextRequest(text:str, idx:int) -> URL:
    from googlesearch import search
    i = 0
    for res in search(f'"{text}" youtube', stop=10):
        # TODO with res
        if i == idx:     return res
        i += 1

