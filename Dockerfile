FROM python:3.11-slim

# Install ClamAV + Supervisor + dependencies
RUN apt-get update && apt-get install -y \
    clamav clamav-daemon clamav-freshclam supervisor curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Update virus definitions (force freshclam to run during build)
RUN freshclam

# Fix permissions (clamav user needs access)
RUN mkdir -p /var/run/clamav && \
    chown clamav:clamav /var/run/clamav && \
    chown -R clamav:clamav /var/lib/clamav

# Set working directory
WORKDIR /app

# Copy code and configs
COPY app.py .
COPY requirements.txt .
COPY clamd.conf /etc/clamav/clamd.conf
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY templates ./templates

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["/usr/bin/supervisord"]
