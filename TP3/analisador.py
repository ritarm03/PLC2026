import re 

tokens = {
    'SELECT': r'\bSELECT\b',
    'WHERE': r'\bWHERE\b',
    'LIMIT': r'\bLIMIT\b',
    'VAR': r'\?\w+',
    'PUNT': r'[{},.:]',
    'NUM': r'\d+',
    'SKIP': r'[ \t\r]+',
    'NEWLINE': r'\n',
    'STRING': r'"[^"]*"',
    'TAG': r'@[a-z]+',
    'PREFIX': r'[A-Za-z_]\w*',
    'ERRO': r'.',
}

def tokenize(input_string):
    reconhecidos = []
    linha = 1

    tokens_regex = '|'.join(f'(?P<{t}>{e})' for t, e in tokens.items())

    for m in re.finditer(tokens_regex, input_string, re.IGNORECASE):
        dic = m.groupdict()
        for tipo, valor in dic.items():
            if valor is not None:
                break

        if tipo == 'SKIP':
            continue
        elif tipo == 'NEWLINE':
            linha += 1
        else:
            reconhecidos.append((tipo, valor, linha, m.span()))
    return reconhecidos

if __name__ == '__main__':
    query1 = '''
SELECT ?nome ?desc WHERE {
 ?s a dbo:MusicalArtist.
 ?s foaf:name "Chuck Berry"@en .
 ?w dbo:artist ?s.
 ?w foaf:name ?nome.
 ?w dbo:abstract ?desc
} LIMIT 1000
'''

    query2 = '''select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000'''
 
    for i, q in enumerate((query1, query2), start=1):
        print(f'--- query{i} ---')
        for tok in tokenize(q):
            print(tok)
        print()