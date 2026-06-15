# Dyadic-to-Integer Beurling Reduction

**Claim status:** This repository does **not** claim a proof of the Riemann Hypothesis. It contains a preliminary research note proving a structural reduction from a dyadic reciprocal Nyman--Beurling refinement to the integer Beurling / Nyman--Báez-Duarte approximation distance.

## Main result

Let

\[
\mathcal H=L^2((1,\infty),y^{-2}dy),
\]

and

\[
F_\alpha(y)=\alpha\lfloor y\rfloor-\lfloor \alpha y\rfloor.
\]

For an integer denominator \(Q\), set

\[
V_Q=\operatorname{span}\{F_{a/Q}:1\le a\le Q-1\},
\qquad
r_Q=(I-P_Q)1,
\qquad
x_Q=\|r_Q\|^2.
\]

Define the reciprocal subspace

\[
\mathcal R_Q=\operatorname{span}\{F_{1/n}:2\le n\le Q\},
\]

and

\[
d_Q=\operatorname{dist}_{\mathcal H}(1,\mathcal R_Q).
\]

The note proves the dichotomy

\[
x_Q\le 4d_Q^2
\]

or

\[
x_Q-x_{\operatorname{lcm}(1,\dots,Q)}\ge \frac14x_Q^2.
\]

Consequently, if \(d_Q\to0\), then \(x_Q\to0\) along a refinement chain, and RH follows by the Nyman--Beurling criterion.

## Endpoint

Under the isometry \(x=1/y\),

\[
F_{1/n}(1/x)=\left\{\frac1{nx}\right\}-\frac1n\left\{\frac1x\right\}.
\]

Thus the remaining condition \(d_Q\to0\) is the integer Beurling / Nyman--Báez-Duarte approximation endpoint. This is the RH-level obstruction, not a technical lemma supplied by the note.

## Files

- `paper/dyadic_to_integer_beurling_reduction.pdf` - main research note.
- `paper/dyadic_to_integer_beurling_reduction.tex` - LaTeX source.
- `docs/CLAIM_STATUS.md` - exact claim boundary.
- `docs/RELEASE_NOTES.md` - v0.1 release notes.
- `docs/REVIEW_REQUEST.md` - text to send to mathematicians for review.
- `docs/ANNOUNCEMENT.md` - public announcement drafts.
- `docs/POSTING_GUIDE.md` - platform and etiquette notes.
- `docs/REFERENCES.md` - primary references.
- `docs/AUTHOR_NOTE.md` - note explaining the personal afterword included in the PDF.
- `CITATION.cff` - citation metadata.

## Suggested citation

Schultze, Karl. *A Dyadic-to-Integer Beurling Reduction for a Reciprocal Nyman--Beurling Refinement.* Preliminary research note, v0.1.2, 2026.

## Transparency

This draft was prepared with AI assistance. It should be independently verified before citation, redistribution, or formal submission.


## License

This repository uses a dual-license structure:

- Research note and documentation: Creative Commons Attribution 4.0 International (CC BY 4.0), SPDX `CC-BY-4.0`.
- Code and build files: MIT License, SPDX `MIT`.

See `LICENSE.md`, `LICENSE-DOCS.md`, `LICENSE-CODE.md`, and `NOTICE.md` for details.
# dyadic-beurling-reduction
