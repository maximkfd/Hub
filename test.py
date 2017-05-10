import hub

hub.set_cosine_border(0.01)
hub.set_number_of_singular_numbers(2)
print(hub.text_markup("text.docx", "Text Tiling"))
print(hub.text_markup_with_parameters("text.docx", 'Text Tiling', 0.01, 2))
print(hub.text_markup("text.docx", "LSA + Text Tiling"))
print(hub.text_markup_with_parameters("text.docx", 'LSA + Text Tiling', 0.01, 2))
