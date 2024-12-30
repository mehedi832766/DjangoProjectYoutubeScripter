#!/bin/bash

SESSION_NAME="venv"


# Check if the session already exists
if tmux has-session -t $SESSION_NAME 2>/dev/null; then
    echo "Session $SESSION_NAME already exists. Attaching to it."
    tmux attach-session -t $SESSION_NAME
else
    # Create a new session and name it
    tmux new-session -d -s $SESSION_NAME -n "django-server"
    
    #activate the environment
    tmux send-keys 'source .ytScripter/bin/activate' C-m
    
    #enter django directory
    tmux send-keys 'cd ytScripterApp/' C-m
    
    #activate django server
    tmux send-keys 'python manage.py runserver' C-m
    
    # Split the window horizontally
    tmux split-window -h
    
    #activate django server
    tmux send-keys -t 1 'code .' C-m

    # Attach to the created session
    #tmux attach-session -t $SESSION_NAME
    
    
fi


