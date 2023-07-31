#!/bin/bash
#chmod +x uninstall_main.sh
# Step 1: Deactivate and remove the virtual environment (if exists)
if [ -d "myenv" ]; then
    source myenv/bin/activate
    deactivate
    rm -rf myenv
fi

# Step 2: Uninstall Streamlit and langchain
pip uninstall -y streamlit langchain

# Step 3: (Optional) Stop the Streamlit app if it's running
# If you deployed the app in the background with 'nohup', you can stop it like this:
# ps aux | grep "streamlit run app.py" | awk '{print $2}' | xargs kill -9

echo "Uninstallation completed."
