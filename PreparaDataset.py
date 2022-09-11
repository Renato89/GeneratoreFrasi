import MyHTMLParser

def getCorpus():

    path_to_file = '/Risorse/paisa.raw.utf8'

    text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
    print(f'Length of text: {len(text)} characters')

    # Il corpus è suddiviso in porzioni contrasegnate da tag HTML <text>. 
    # Si estraggono e si accorpano.
    #  Vengono presi solo i contenuti che contengono un dato insieme di caratteri,
    #   quei caratteri che si trovano normalmente in frasi in lingua italiana.
    parser = MyHTMLParser()
    parser.feed(text)
    text = " ".join(parser.contents)

    # The unique characters in the file
    vocab = sorted(set(text))
    print(f'{len(vocab)} unique characters')

    return (text, vocab)