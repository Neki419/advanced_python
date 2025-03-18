FROM python:3.12

RUN apt-get update && apt-get install -y \
    texlive-latex-base \
    texlive-fonts-recommended \
    texlive-fonts-extra \
    texlive-latex-extra \
    && apt-get clean

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml /app/

COPY hw2/ /app/hw2/

WORKDIR /app/hw2

RUN poetry install --no-root

CMD ["bash"]
