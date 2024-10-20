# Extending apache/airflow Docker image
FROM apache/airflow:2.10.2

# Copy requirements.txt into the container
COPY requirements.txt /requirements.txt

# Upgrade pip and install numpy first, then install the remaining requirements
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /requirements.txt
