"""
script to create a markdown document of FSIII helbredstilstande-data using markup more in the spirit of Markdown 
"""
import json
import textwrap

with open('FSIII_helbredstilstande.json', 'r') as f:
    helbredstilstande = json.load(f)

max_char_width = 128

markdown_string = ""
current_kategori = ""
kategori_counter = 1
beskrivelse_header = "Helbredstilstand"
eksempel_header = "Eksempel"
newlinecharecter = "\n"
indent = 4*' '
for helbredstilstand in helbredstilstande:
    # Note this requires that the dict (thus the json) is sorted with respect to kategori
    if current_kategori != helbredstilstand["kategori"]:
        current_kategori = helbredstilstand["kategori"]
        md_header = '### ' + current_kategori + ('**' if helbredstilstand["medsendes_indlaeggelsesrapporten"] else '') 
        markdown_string = markdown_string + f' {kategori_counter}. {md_header}\n\n'
        kategori_counter = kategori_counter + 1

    markdown_string = markdown_string + indent + f'#### {helbredstilstand["titel"]}\n'

    for paragraph in helbredstilstand["beskrivelse"].split('\n'):
        markdown_string = markdown_string + indent + ('\n' + indent).join(textwrap.wrap(paragraph, max_char_width - 4, break_long_words=False, break_on_hyphens=False)) + '\n\n'

    markdown_string = markdown_string + indent + '> _Eksempel_:\n' + indent + '>\n'
    for paragraph in helbredstilstand["eksempel"].split('\n'):
        markdown_string = markdown_string + indent + '> ' + f'\n{indent}> '.join(textwrap.wrap(paragraph, max_char_width - 6, break_long_words=False, break_on_hyphens=False)) + '\n' + indent + '>\n'

with open('scripts/temp_output_md_helbredstilstande_listed.md', 'w') as f:
    f.write(markdown_string)
