import pymupdf as pu

path = "./Convert/Ferramentas_cyber.pdf"
doc = pu.open(path)

def get_pages_from_pdf(path: str)-> None: 
    # Processo logico de abrir o arquivo e extrair as imagens
    doc = pu.open(path)

    # Loop necessario pois quebra o pdf pagina por pagina.
    for page_index in range(len(doc)): 
        page = doc[page_index]
        image_list = page.get_images()

        # Log se achou imagens
        if image_list:
            print(f"Found {len(image_list)} on {page_index} page")
        else:
            print(f"Not found images on {page_index}")
        for image_index, img in enumerate(image_list, start=1):
            xref = img[0]    
            pix = pu.Pixmap(doc,xref)

            if pix.n - pix.alpha > 3:
                pix = pu.Pixmap(pu.csRGB, pix)
            pix.save("Page_%s-image_%s.png" % (page_index, image_index))
            pix = None

get_pages_from_pdf(path)