import argparse
from translate import translate


parser = argparse.ArgumentParser(description='Traductor de texto en linea')
parser.add_argument('text')
parser.add_argument('-t', default='en-es', help='Orden de traduccion')

params = parser.parse_args()
source, target = params.t.split('-')
print('[{}] {}'.format(source, params.text))
print('[{}] {}'.format(target, translate(params.text, source, target)))
