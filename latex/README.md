# Latex
something like word or pages that can make pdf through programming. great for making research report, thesis, document with math etc.

## Compile Method
pdflatex [filename].tex

## Install Method
TODO

## Latex Command List
--initialization! always begin with this--
\documentclass[option]{classname}
				(option: 12pt, a4, b5 etc)
				(classname: jarticle article report book etc)
\usepackage{packagename}	(packagename: use below)

--jarticle with english name--
\documentclass[]{jarticle}
\usepackage[english]{babel}

--print document--
\begin{document}
[anything in here is printed]
\end{document}

--include graph from outside--
\usepackage[dvipdfmx]{graphicx}
...
\input{filename}
\hspace{1.6cm} title

--input code--
\usepackage{listings}
\lstset{basicstyle=\scriptsize}
...
\lstinputlisting[language=[option]{filename} (option: C, Java,Python etc.)



--include stuff--
\title[entername]
\date[enterdate]
\author[enterauthor]

--inline equation mode--
$[equation]$

-display equation mode--
$$[equation]$$

--matrix--
\begin{bmatrix}
4 & 5\\
3 & 3\\
\end{bmatrix}

--subscript--
_{name}

--superscript--
^{name}

--fraction--
\frac{numerator}{denominator}

--greek alphabet--
\alpha
\beta
\gamma
(etc).

--comment--
%

--compile tex document--
pdflatex [filename].tex 		(becareful not to use 'latex' !)

--compile tex document with jarticle--
platex [filename].tex
dvipdfmx [filename].dvi

--compile tex document with bibliograpy--
platex -shell-escape [filename].tex
pbibtex [filename].aux
platex [filename].tex
platex [filename].tex
dvipdfmx [filename].tex

--open pdf file--
explorer [filename].pdf(for windows)
evince [filename].pdf (for ubuntu)


