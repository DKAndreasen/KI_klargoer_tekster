import json

with open('FSIII_helbredstilstande.json', 'r') as f:
    helbredstilstande = json.load(f)

# Count max number of characters in respectively "beskrivelse" and "eksempel" for each "kategori":
max_number_char = {}
for helbredstilstand in helbredstilstande:
    if helbredstilstand["kategori"] not in max_number_char:
        max_number_char[helbredstilstand["kategori"]] = {
            "beskrivelse": len(helbredstilstand["titel"])+ 10 + len(helbredstilstand["beskrivelse"]) + 4*helbredstilstand["beskrivelse"].count('\n'),
            "eksempel": len(helbredstilstand["eksempel"]) + 4*helbredstilstand["eksempel"].count('\n')
        }
    else:
        cell_len_beskrivelse = len(helbredstilstand["titel"])+ 10 + len(helbredstilstand["beskrivelse"]) + 4*helbredstilstand["beskrivelse"].count('\n')
        cell_len_eksempel = len(helbredstilstand["eksempel"]) + 4*helbredstilstand["eksempel"].count('\n')
        if max_number_char[helbredstilstand["kategori"]]["beskrivelse"] < cell_len_beskrivelse:
            max_number_char[helbredstilstand["kategori"]]["beskrivelse"] = cell_len_beskrivelse
        if max_number_char[helbredstilstand["kategori"]]["eksempel"] < cell_len_eksempel:
            max_number_char[helbredstilstand["kategori"]]["eksempel"] = cell_len_eksempel


markdown_table_string = ""
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
        markdown_table_string = markdown_table_string + f'\n {kategori_counter}. {md_header}\n\n'
        md_table_header = f'| {beskrivelse_header + (max_number_char[current_kategori]["beskrivelse"] - len(beskrivelse_header))*" "} | {eksempel_header + (max_number_char[current_kategori]["eksempel"] - len(eksempel_header))*" "} |'
        markdown_table_string = markdown_table_string + indent + md_table_header + "\n"

        md_table_sep = f'|-{max_number_char[current_kategori]["beskrivelse"]*"-"}-|-{max_number_char[current_kategori]["eksempel"]*"-"}-|'
        markdown_table_string = markdown_table_string + indent + md_table_sep + "\n"

        kategori_counter = kategori_counter + 1

    text_len_beskrivelse = len(helbredstilstand["titel"]) + 10 + len(helbredstilstand["beskrivelse"]) + 4 * helbredstilstand["beskrivelse"].count('\n')
    text_len_eksempel = len(helbredstilstand["eksempel"]) + 4*helbredstilstand["eksempel"].count('\n')
    md_table_row = f'| __{helbredstilstand["titel"]}:__<br/>{helbredstilstand["beskrivelse"].replace(newlinecharecter,"<br/>") + " "*(max_number_char[current_kategori]["beskrivelse"] - text_len_beskrivelse)} | {helbredstilstand["eksempel"].replace(newlinecharecter,"<br/>") + " "*(max_number_char[current_kategori]["eksempel"] - text_len_eksempel)} |'
    markdown_table_string = markdown_table_string + indent + md_table_row + "\n"

with open('scripts/temp_output_md_table_helbredstilstande.md', 'w') as f:
    f.write(markdown_table_string)
