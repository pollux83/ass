#!/bin/bash

# Step 1: Install Required Dependencies
sudo apt update
sudo apt install -y python3 python3-pip python3-venv

# Step 2: Create a Virtual Environment
python3 -m venv myenv
source myenv/bin/activate

# Step 3: Prepare your Streamlit app
mkdir my_streamlit_app
cd my_streamlit_app

cat << EOF > main.py
import streamlit as st

def main():
    st.title("My Streamlit App")
    st.write("Welcome to my first Streamlit app!")

if __name__ == "__main__":
    main()
EOF

# Step 4: Create a requirements.txt file
echo "streamlit==1.8.0
langchain==0.0.247" > requirements.txt

# Step 5: Install dependencies
pip install -r requirements.txt

# Step 6: Run the Streamlit app (in the background)
nohup streamlit run main.py &

# Step 7: (Optional) Set up a reverse proxy using Nginx
# Replace "your_domain.com" with your actual domain name
# sudo apt install -y nginx
# cat << EOF | sudo tee /etc/nginx/sites-available/my_streamlit_app
# server {
#     listen 80;
#     server_name your_domain.com;

#     location / {
#         proxy_pass http://localhost:8501;
#         proxy_set_header Host \$host;
#         proxy_set_header X-Real-IP \$remote_addr;
#         proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
#     }
# }
# sudo ln -s /etc/nginx/sites-available/my_streamlit_app /etc/nginx/sites-enabled/
# sudo nginx -t
# sudo systemctl restart nginx

# Step 8: Access the App
echo "Your Streamlit app should be accessible at http://localhost:8501"
