#!/usr/bin/env bash

cd "$(dirname "$0")" || exit

NAME_SESSION="data_analysis"

if command -v nvim >/dev/null 2>&1; then
	EDITOR="nvim"
else
	EDITOR="vim"
fi

if [ ! -f .venv/bin/activate ]; then
	python -m venv .venv && python -m pip install -r requirements.txt
fi

if tmux has-session -t "$NAME_SESSION"; then
	tmux kill-session -t "$NAME_SESSION"
fi

tmux new-session -d -s "$NAME_SESSION"

tmux set-option -t "$NAME_SESSION" base-index 1
tmux set-option -t "$NAME_SESSION" pane-base-index 1

tmux set-hook -t "$NAME_SESSION" after-new-window "send-keys \"source $(pwd)/.venv/bin/activate\" Enter "clear" Enter"
tmux set-hook -t "$NAME_SESSION" after-split-window "send-keys \"source $(pwd)/.venv/bin/activate\" Enter "clear" Enter"
tmux send-keys -t "$NAME_SESSION:1.1" "source $(pwd)/.venv/bin/activate" Enter "clear" Enter

tmux send-keys -t "$NAME_SESSION:1.1" "$EDITOR" Enter
tmux new-window

tmux attach -t "$NAME_SESSION:1.1"
