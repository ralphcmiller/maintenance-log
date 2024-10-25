#Python runtime as a parent image
FROM python:3.13

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable for Flask
ENV FLASK_APP=app.py

# Run Flask when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]
