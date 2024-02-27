FROM python:3

RUN python3 -m pip install --upgrade pip

RUN python3 -m venv .venv

RUN python3 .venv/bin/activate

RUN python3 -m pip install pendulum telebot supabase flet httpx

WORKDIR /app

EXPOSE 8501

COPY . .

CMD ["python", "main.py"]
