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
        markdown_string = markdown_string + '### ' + str(kategori_counter) + '. ' + current_kategori + ('**' if helbredstilstand["medsendes_indlaeggelsesrapporten"] else '') + '\n\n'
        kategori_counter = kategori_counter + 1

    markdown_string = markdown_string + f'#### {helbredstilstand["titel"]}\n'

    for paragraph in helbredstilstand["beskrivelse"].split('\n'):
        markdown_string = markdown_string + '\n'.join(textwrap.wrap(paragraph, max_char_width, break_long_words=False, break_on_hyphens=False)) + '\n\n'

    markdown_string = markdown_string + '> _Eksempel_:\n>\n'
    for paragraph in helbredstilstand["eksempel"].split('\n'):
        markdown_string = markdown_string + '> ' + '\n> '.join(textwrap.wrap(paragraph, max_char_width - 2, break_long_words=False, break_on_hyphens=False)) + '\n>\n'

with open('scripts/temp_output_md_helbredstilstande.md', 'w') as f:
    f.write(markdown_string)
