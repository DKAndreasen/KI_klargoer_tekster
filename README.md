# KI klargør tekster

Her findes intro til at bruge markdown som en måde at gøre tekster 
nemmere for kunstig intelligens at læse/interagere med.

 - [Intro til muligt redigeringsværktøj: MarkText samt markdown](Installer_MarkText.md)
 - [Eksempel på opsætning af dokument](FSIII_helbredstilstande.md) som bibeholder en tabel opsætning
 - [Alternativt eksempel på opsætning](FSIII_helbredstilstande_alternative_markdown_style.md) som er mere i markdowns tiltænkte stil
 - [Endnu et alternativt eksempel på opsætning](FSIII_helbredstilstande_alternative__markdown_listed.md) som bibeholder en oplistningsstil, men ikke benytter tabeller


## Andre ressourcer
Se i øvrigt:
 - [Pandoc: Konverteringsværktøj](https://pandoc.org)
 - [asciidoc](https://asciidoc.org): Et alternativt til markdown, som umiddelbart indeholder flere markup muligheder, men så vidt jeg er orienteret ikke er så udbredt og hvor jeg ikke kender til et ligeså let tilgængeligt redigeringsværktøj som MarkText
 - [Jans fine tekst om markdown og git, som inspirede mig til at foreslå MarkText](
     https://www.os2.eu/blog/nyheder-2/aktiver-vaerdien-af-ai-i-dine-dokumenter-4389
   )
 - [Digitaliseringsstyrelsens anbefalinger til standarder for sprogressourcer](https://sprogteknologi.dk/pages/standarder-for-ressourcer)


## Teksten som "data"
Udover eksemplerne ovenfor, hvor teksten er opsæt som et *dokument* ved brug af markdown formatet i stedet for 
eksempelvis `docx` formatet, så kan teksten og opfattes rent som data, her er et eksempel på tabel indholdet fra 
FSIII helbredstilstande pdf'en gemt i `json` formatet:

 - [eksempel på tekst som data](/FSIII_helbredstilstande.json)
 - [og tilhørende skema](/FSIII_helbredstilstande.schema.json): som er en beskrivelse af data formatet

Når først teksten er tilgængelig i et data-format (eller en database), er det nemt at behandle det programatisk, som 
man kan se eksempler på i [script-mappen](/scripts) 