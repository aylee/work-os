#!/bin/bash
# Symlink dotfiles from work-os to their expected locations.
# Run from any directory — paths are absolute.

DOTFILES="$HOME/code/work-os/library/dotfiles"

# Claude Code
mkdir -p "$HOME/.claude"
ln -sf "$DOTFILES/claude/settings.json" "$HOME/.claude/settings.json"

# Ghostty
mkdir -p "$HOME/.config/ghostty"
ln -sf "$DOTFILES/ghostty/config" "$HOME/.config/ghostty/config"

echo "Dotfiles symlinked."
