import os
import argparse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image, Frame
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.platypus.doctemplate import NextPageTemplate
from reportlab.platypus.tableofcontents import TableOfContents
from markdown import markdown
from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT, TA_CENTER, TA_LEFT
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from datetime import datetime
import re

# Nuova classe per la gestione del PDF
class MyDocTemplate(SimpleDocTemplate):
    def __init__(self, filename, **kw):
        self.allowSplitting = 0
        SimpleDocTemplate.__init__(self, filename, **kw)
        #template = PageTemplate('normal', [Frame(2.5*cm, 2.5*cm, 15*cm, 25*cm, id='F1')])
        #self.addPageTemplates(template)

    def afterFlowable(self, flowable):
        "Registers TOC entries."
        if flowable.__class__.__name__ == 'Paragraph':
            text = flowable.getPlainText()
            style = flowable.style.name
            if style == 'Header1':
                self.notify('TOCEntry', (0, text, self.page))
            if style == 'Header2':
                self.notify('TOCEntry', (1, text, self.page))
            if style == 'Header3':
                self.notify('TOCEntry', (2, text, self.page))

def convert_markdown_to_pdf():
    # File di output
    output_file = 'Path to senior developer.pdf'

    # Registra i font personalizzati
    pdfmetrics.registerFont(TTFont('Quicksand'      , 'fonts/Quicksand-Regular.ttf'))
    pdfmetrics.registerFont(TTFont('Roboto'         , 'fonts/Roboto-Regular.ttf'))
    pdfmetrics.registerFont(TTFont('Roboto-Bold'    , 'fonts/Roboto-Bold.ttf'))
    pdfmetrics.registerFont(TTFont('SourceCodePro'  , 'fonts/SourceCodePro-Regular.ttf'))

    # Stili personalizzati per i paragrafi
    custom_styles = {
        'header1'   : ParagraphStyle(name='Header1'     , fontName='Roboto-Bold'    , fontSize=16,                  spaceAfter=16   , leading=24                    ),
        'header2'   : ParagraphStyle(name='Header2'     , fontName='Roboto-Bold'    , fontSize=14,                  spaceAfter=8    , leading=16                    ),
        'header3'   : ParagraphStyle(name='Header3'     , fontName='Roboto-Bold'    , fontSize=12,                  spaceAfter=8    , leading=14                    ),
        'paragraph' : ParagraphStyle(name='Paragraph'   , fontName='Quicksand'      , fontSize=12, spaceBefore=10,  spaceAfter=10   , leading=18    , alignment=TA_JUSTIFY ),
        'toc_entry' : ParagraphStyle(name='TOCEntry'    , fontName='Roboto'         , fontSize=14, spaceBefore=6,   spaceAfter=6    , leading=14                    ),
        'code'      : ParagraphStyle(name='Code'        , fontName='SourceCodePro'  , fontSize=12, spaceBefore=10,  spaceAfter=10   , leading=14    , # leftIndent=12,
            textColor=colors.black,
            backColor=colors.Color(0.93, 0.93, 0.93),  # Grigio estremamente tenue
            borderColor=colors.Color(0.8, 0.8, 0.8),   # Bordo quasi invisibile
            borderWidth=0.3,
            borderPadding=5,
            borderRadius=2,  # Angoli arrotondati )
        )
    }

    # Stile con sfondo e bordo
    boxed_style = ParagraphStyle(
        'BoxedStyle',
        fontName='Helvetica',
        fontSize=10,
        textColor=colors.black,
        backColor=colors.lightgrey,  # Sfondo grigio chiaro
        borderColor=colors.darkgrey,  # Colore bordo
        borderWidth=1,  # Spessore bordo
        borderPadding=5,  # Padding interno
        borderRadius=3,  # Angoli arrotondati
    )

    # Lista dei capitoli con i rispettivi file markdown
    capitoli = [
        # Fondamenta della Professionalità
        ('01- fondamenta della professionalità.md', ''),
        ('../01-ProgrammatoriA40Anni-articolo-it.md', 'Programmatori a 40 Anni', '../foto/01-ProgrammatoriA40Anni-articolo-1-leonardo-ia.jpg'),
        ('../02-FinireIPropriTask-articolo-it.md', 'Finire i Propri Task', '../foto/02-FinireIPropriTask-articolo-1-leonardo-ai.jpg'),
        ('../12-SoftSkills-per-Sviluppatori.md', 'Soft Skills per Sviluppatori', '../foto/.jpg'),
        ('../12-Comunicazione Efficace in Team Tecnici.md', 'Comunicazione Efficace in Team Tecnici', '../foto/.jpg'),

        # Eccellenza Tecnica
        ('02- eccellenza tecnica.md', ''),
        ('../04-CondizioneNelCodice-articolo-it.md', 'Cambia quella condizione nel codice', '../foto/04-CondizioneNelCodice-articolo-3-leonardo-ai.jpg'),
        ('../06-EsplorareNuoviFramework-articolo-it.md', 'Esplorando nuovi framework', '../foto/06-EsplorareNuoviFramework-articolo-4-leonardo-ai.jpg'),
        ('../03-IlMitodelFullStackDeveloper-articolo-it.md', 'Il mito del FullStack developer', '../foto/03-DALL·E 2024-04-15 15.23.18 - A wide aspect image of a mythical version of a fullstack developer as Medusa. This scene blends ancient and modern elements_ Medusa, with a crown of v.webp'),
        ('../11-CodeReview-articolo-it.md', 'Code Review', '../foto/11-CodeReview-articolo-1-leonardo-ai.jpg'),

        # Dimensione Professionale
        ('03- dimensione professionale.md', ''),
        ('../05-CelodurismoDeiProgrammatori-articolo-it.md', 'Celodurismo dei programmatori', '../foto/05-CelodurismoDeiProgrammatori-articolo-1-leonardo-ai.jpg'),
        ('../07-ProgrammatoriMercenari-articolo-it.md', 'Programmatori mercenari', '../foto/07-ProgrammatoriMercenari-articolo-2-leonardo-ai.jpg'),
        ('../09-LaRALMotivaAlCambiamento-articolo-it.md', 'La RAL non motiva al cambiamento', '../foto/09-LaRALMotivaAlCambiamento-articolo-2-leonardo-ai.jpg'),
        ('../10-ChiPerdeUnProgrammatorePerdeUnTesoro-articolo-it.md', 'Chi perde un programmatore perde un tesoro', '../foto/10-ChiPerdeUnProgrammatorePerdeUnTesoro-articolo-2-dall-e.png'),

        # Dimensioni Personali e Sistemiche
        ('04- dimensioni personali e sistemiche.md', ''),
        ('../56-Gestione-del-Burnout-e-Salute-Mentale.md', 'Gestione del Burnout e Salute Mentale', '../foto/.jpg'),
        ('../58-Etica e Responsabilità nella Programmazione.md', 'Etica e Responsabilità nella Programmazione', '../foto/.jpg')
    ]
    
    h1 = ParagraphStyle(name = 'h1',
       fontSize = 14,
       leading = 16)

    h2 = ParagraphStyle(name = 'h2',
       fontSize = 12,
       leading = 14,
       leftIndent = 10)

    h3 = ParagraphStyle(name = 'h3',
       fontSize = 12,
       leading = 14,
       leftIndent = 10)

    # Creazione del PDF
    doc = MyDocTemplate(output_file,
                            pagesize=letter,
                            bottomMargin=100) # Lascia spazio per il footer

    page_width, page_height = letter
    frame_no_margins = Frame(0, 0, page_width, page_height, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    frame_with_margins = Frame(inch, inch, page_width - 2*inch, page_height - 2*inch, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)

    first_page_template = PageTemplate(id="FirstPage", frames=[frame_no_margins])
    following_pages_template = PageTemplate(id="FollowingPages", frames=[frame_with_margins])
    doc.addPageTemplates([first_page_template, following_pages_template])

    elements = []

    # Crea l'oggetto TOC
    toc = TableOfContents()
    toc.levelStyles = [h1, h2, h3]

    # Copertina
    cover_image = Image(os.path.join('covers/Path to senior developer - alternative 3.png'), width=9*inch, height=11*inch)    
    elements.append(cover_image)
    add_page(elements)

    # Prefazione dell'autore
    f = open('../00-prefazione-it.md', 'r', encoding='utf-8');
    markdown_content = f.read()
    elements.extend(process_markdown_content(markdown_content, custom_styles))
    add_page(elements)

    # Ringraziamenti
    ringraziamenti = Paragraph('Ringraziamenti', custom_styles['header1'])
    elements.append(ringraziamenti)
    elements.append(Paragraph('Grazie alla mia famiglia, che con il suo amore e il suo supporto mi ha permesso di realizzare questo progetto.', custom_styles['paragraph']))
    add_page(elements)

    # Introduzione
    f = open('../00-introduzione-it.md', 'r', encoding='utf-8');
    markdown_content = f.read()
    elements.extend(process_markdown_content(markdown_content, custom_styles))
    add_page(elements)

    # Elaborazione capitoli
    for chapter_info in capitoli:
        # Gestisci la possibilità di avere 2 o 3 elementi nella tupla
        if len(chapter_info) == 3:
            filename, title, image_path = chapter_info
        else:
            if len(chapter_info) == 2:
                filename, title = chapter_info
                image_path = None
            else:            
                filename= chapter_info
                title = None
                image_path = None

        # Aggiungi l'intestazione del capitolo
        if title:
            elements.append(Paragraph(title, custom_styles['header1']))

            # Aggiungi l'immagine se presente
            if image_path and os.path.exists(image_path):
                print(f'Leggo MD {image_path}')
                try:
                    img = Image(image_path, width=400*1.2, height=300*1.2)  # Regola dimensioni secondo necessità
                    img.hAlign = 'CENTER'
                    elements.append(img)                
                except Exception as e:
                    print(f"Errore nel caricamento dell'immagine {image_path}: {e}")

            add_page(elements)

        # Leggi il contenuto del file markdown
        print(f'Leggo MD {filename}')
        with open(filename, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
            chapter_elements = process_markdown_content(markdown_content, custom_styles)
            elements.extend(chapter_elements)
    
            add_page(elements)

    # Biografia
    f = open('../00-biografia-it.md', 'r', encoding='utf-8');
    markdown_content = f.read()
    elements.extend(process_markdown_content(markdown_content, custom_styles))
    add_page(elements)

    # Inserisci la TOC prima della biografia
    elements.append(Paragraph('Indice', custom_styles['header1']))
    elements.append(toc)    
    add_page(elements)

    # Dati aziendali personalizzati 
    now = datetime.now()
    custom_data = {
        'oggi': now.strftime("%d/%m/%Y %H:%M")
    }

    # Genera PDF
    doc.multiBuild(elements, 
          onLaterPages=lambda canvas, doc: (
              add_footer(canvas, doc, custom_data)
          ))

    # Stampa a video il percorso del file creato
    print(f'PDF creato: {output_file}')

# Resto del codice rimane invariato
def main():
    convert_markdown_to_pdf()

def process_markdown_content(content, custom_styles):
    blocks = []
    in_code_block = False
    code_lines = []    

    for line in content.splitlines():
        if line.strip().startswith("```"):
            if not in_code_block:
                in_code_block = True
                code_lines = []
            else:
                in_code_block = False
                code_text = "\n".join(code_lines)
                blocks.append(Paragraph(code_text, custom_styles['code']))
                code_lines = []
        elif in_code_block:
            code_lines.append(line)
        else:
            # Riconosce le intestazioni
            if line.startswith("# "):
                blocks.append(Paragraph(line[2:], custom_styles['header1']))
            elif line.startswith("## "):
                # Aggiungi un PageBreak prima delle conclusioni
                if line.startswith("## Conclusioni"):
                    blocks.append(PageBreak())

                blocks.append(Paragraph(line[3:], custom_styles['header2']))
            elif line.startswith("### "):
                blocks.append(Paragraph(line[3:], custom_styles['header3']))
            else:
                # Linea normale trattata come paragrafo
                blocks.append(Paragraph(line, custom_styles['paragraph']))

    if code_lines:
        code_text = "\n".join(code_lines)
        blocks.append(Paragraph(code_text, custom_styles['code']))

    return blocks

def add_footer(canvas, doc, custom_data):
    print(f'Footer per pagina {doc.page}')
   
    canvas.saveState()

    # Disegna una riga orizzontale
    canvas.setStrokeColor(colors.grey)
    canvas.setLineWidth(0.5)  # Spessore della riga
    canvas.line(
        doc.leftMargin,  # Punto x iniziale 
        doc.bottomMargin - 65,  # Punto y (leggermente sopra il testo del footer)
        doc.width + doc.leftMargin,  # Punto x finale (larghezza totale)
        doc.bottomMargin - 65  # Punto y finale (stesso y iniziale)
    )

    footer_styleR = ParagraphStyle(
        'footer',
        fontSize=12,
        textColor=colors.grey,
        alignment=TA_RIGHT,  # Allineamento a destra per il numero di pagina
        #borderColor=colors.darkgrey,  # Colore bordo
        #borderWidth=1,  # Spessore bordo
    )

    footer_styleC = ParagraphStyle(
        'footer',
        fontSize=12,
        textColor=colors.grey,
        alignment=TA_CENTER,  # Allineamento a destra per il numero di pagina
        #borderColor=colors.darkgrey,  # Colore bordo
        #borderWidth=3,  # Spessore bordo
    )

    footer_styleL = ParagraphStyle(
        'footer',
        fontSize=12,
        textColor=colors.grey,
        alignment=TA_LEFT,  # Allineamento a destra per il numero di pagina
        #borderColor=colors.darkgrey,  # Colore bordo
        #borderWidth=5,  # Spessore bordo
    )

    # Footer sinistro
    left_footer = Paragraph("Matteo Baccan", footer_styleL)
    w, h = left_footer.wrap(doc.width, doc.bottomMargin)
    left_footer.drawOn(canvas, doc.leftMargin, h)
    
    # Footer centrale
    center_footer = Paragraph( custom_data['oggi'], footer_styleC)
    w, h = center_footer.wrap(doc.width, doc.bottomMargin)
    center_footer.drawOn(canvas, doc.leftMargin, h)
    
    # Footer destro (numero pagina)
    right_footer = Paragraph(f"Pagina {doc.page}", footer_styleR)
    w, h = right_footer.wrap(doc.width, doc.bottomMargin)
    right_footer.drawOn(canvas, doc.leftMargin, h)
    
    canvas.restoreState()

def add_page(elements):
    elements.append(PageBreak())

if __name__ == "__main__":
    main()