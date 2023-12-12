import arxiv2bib 

with open("./input.txt",mode="r") as f:
    l = f.readlines()

refs = arxiv2bib.arxiv2bib(
    [s.rstrip().removeprefix("https://arxiv.org/abs/") for s in l]
)

with open("./output.bib",mode="w", encoding="utf-8") as g:
    for r in refs:
        g.write(r.bibtex()+"\n\n")
    
   