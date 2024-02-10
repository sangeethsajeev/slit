readonly REQUIREMENTS_DIRECTORY="/slit/"
readonly SCRIPT_DIRECTORY=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)

function main() {
  echo "Install Slit Service environment."
  echo "Install dependencies from ${REQUIREMENTS_DIRECTORY}"

  set -o errexit
  set -o pipefail
  set -o nounset
  set -o errtrace

  install_env

}

function install_env() {

  echo "[***] Printing Python Version..."
  python -V

  ls

  echo "[***] Run the Application..."
  streamlit run slit/slit.py --server.port 80

}

main