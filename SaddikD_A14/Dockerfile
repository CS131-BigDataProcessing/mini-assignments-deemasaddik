# Step 1: Specify the base image
FROM python:3.8-slim

# Step 2: Set the working directory
WORKDIR /app

# Step 3: Copy application files
COPY . /app

# Step 4: Install Python dependencies
RUN pip install -r requirements.txt

# Step 5: Specify the command to run the app
CMD ["python", "app.py"]

