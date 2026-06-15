PDF=paper/dyadic_to_integer_beurling_reduction.pdf
TEX=paper/dyadic_to_integer_beurling_reduction.tex

all: $(PDF)

$(PDF): $(TEX)
	cd paper && pdflatex -interaction=nonstopmode dyadic_to_integer_beurling_reduction.tex && pdflatex -interaction=nonstopmode dyadic_to_integer_beurling_reduction.tex

clean:
	rm -f paper/*.aux paper/*.log paper/*.out paper/*.toc
