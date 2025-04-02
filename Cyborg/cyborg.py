import os
import time
import streamlit as st

def create_folder(folder_name):
    try:
        os.makedirs(folder_name, exist_ok=True)
        st.success(f"✅ Folder '{folder_name}' created successfully!")
    except Exception as e:
        st.error(f"❌ Error creating folder: {e}")

def main():
    st.title("🤖 Cyborg Assistant")
    st.write("Type your commands and I'll create folders and perform tasks for you.")
    
    command = st.text_input("What would you like me to do? (type 'exit' to quit)")
    
    if command:
        if command.lower() == 'exit':
            st.write("🤖 Goodbye!")
            return
        
        folder_name = command.replace(" ", "_")
        create_folder(folder_name)
        
        st.write(f"\n📁 Created: {folder_name}")
        st.write("You can now use this folder for your tasks!")

if __name__ == "__main__":
    main()