jupyter nbconvert --to python *.ipynb --output-dir ./src
jupyter nbconvert --to markdown --TemplateExporter.exclude_input=True price_check.ipynb