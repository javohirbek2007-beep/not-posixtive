FROM python:3.11-slim

# Ish papkasi
WORKDIR /app

# Fayllarni copy qilish
COPY misc_not_posixtive/server.py /app/server.py
COPY flag.txt /app/flag.txt

# Port ochish
EXPOSE 1337

# Socat orqali service qilish
RUN apt update && apt install -y socat && rm -rf /var/lib/apt/lists/*

# Run
CMD socat TCP-LISTEN:1337,reuseaddr,fork EXEC:"python3 /app/server.py",pty,stderr
