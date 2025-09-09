FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run the application on port 8000
CMD ["adk", "web", "--port", "8000", "--host", "0.0.0.0"]