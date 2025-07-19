# Dockerfile
FROM redhat/ubi8

# Install Python and pip (assuming it's not already there or needs updating)
RUN yum update -y && yum install python3 -y

# Install Flask
RUN pip3 install flask

# Copy your Flask application code into the container
COPY app.py /app.py

# Expose port 5000 (documentation for the user)
EXPOSE 5000

# This is the ONLY CMD instruction that should be present.
# It tells Docker to run your Flask application when the container starts.
CMD ["python3", "/app.py"]