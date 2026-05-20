import nbformat as nbf
from glob import glob


def process_cell(cell):
    # get tags
    tags = cell['metadata'].get('tags', [])

    if cell['cell_type'] == 'code':
        source = cell['source']

        if 'def download(url):' in source and 'import thinkpython' in source:
            tags = cell['metadata'].setdefault('tags', [])
            for tag in ['remove-cell', 'keep']:
                if tag not in tags:
                    tags.append(tag)

        # remove solutions
        if source.startswith('# Solution') or 'solution' in tags:
            cell['source'] = []

        # remove %%expect cell magic
        if source.startswith('%%expect'):
            t = source.split('\n')[1:]
            cell['source'] = '\n'.join(t)

    # add reference label
    for tag in tags:
        if tag.startswith('chapter') or tag.startswith('section'):
            # print(tag)
            label = f'({tag})=\n'
            cell['source'] = label + cell['source']


def process_notebook(path):
    ntbk = nbf.read(path, nbf.NO_CONVERT)

    for cell in ntbk.cells:
        process_cell(cell)

    nbf.write(ntbk, path)


# Collect a list of the notebooks in the content folder
paths = glob("chap*.ipynb")

for path in sorted(paths):
    print('prepping', path)
    process_notebook(path)
