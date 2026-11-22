#!/usr/bin/env bash
set -euo pipefail

# --- Functions ---

pretty_print() {
  local message="$1"
  printf "\n%s\n\n" "$message"
}

detect_os() {
  case "$OSTYPE" in
    darwin*)
      echo "macos"
      ;;
    linux-gnu*)
      echo "linux"
      ;;
    *)
      echo "unsupported"
      ;;
  esac
}

ensure_python3() {
  local os_type="$1"

  if command -v python3 >/dev/null 2>&1; then
    pretty_print "Python 3 is already installed: $(python3 --version)"
  else
    pretty_print "Python 3 not found. Installing..."
    if [[ "$os_type" == "macos" ]]; then
      brew install python
    elif [[ "$os_type" == "linux" ]]; then
      sudo apt-get update && sudo apt-get install -y python3 python3-pip
    else
      pretty_print "Unsupported OS ($OSTYPE); cannot auto-install Python 3."
      return 1
    fi
  fi
}

verify_pip() {
  if python3 -m pip --version >/dev/null 2>&1; then
    pretty_print "pip is available: $(python3 -m pip --version)"
  else
    pretty_print "pip not found. Attempting installation..."
    python3 -m ensurepip --upgrade || true
    python3 -m pip --version
  fi
}

install_jupyter() {
  local os_type="$1"

  if command -v jupyter >/dev/null 2>&1; then
    pretty_print "Jupyter is already installed: $(jupyter --version | head -n 1)"
    return 0
  fi

  pretty_print "Installing Jupyter Notebook..."
  if [[ "$os_type" == "macos" ]]; then
    if command -v pipx >/dev/null 2>&1; then
      pipx install notebook
    else
      python3 -m pip install --break-system-packages notebook
    fi
  elif [[ "$os_type" == "linux" ]]; then
    python3 -m pip install --break-system-packages notebook || sudo apt-get install -y jupyter-notebook
  fi
}

run_macos_health_check() {
  local os_type="$1"

  if [[ "$os_type" == "macos" ]]; then
    pretty_print "Running Homebrew health check (brew doctor)..."
    brew doctor || true
  fi
}

# --- Main Logic ---

main() {
  local os_type
  os_type="$(detect_os)"

  pretty_print "Starting environment setup on detected OS: $os_type"
  ensure_python3 "$os_type"
  verify_pip
  install_jupyter "$os_type"
  run_macos_health_check "$os_type"
  pretty_print "Environment setup finished!"
}

main "$@"
