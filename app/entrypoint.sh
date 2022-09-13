#!/bin/bash
set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

python3.8 ${DIR}/main.py || (curl -sf -XPOST http://127.0.0.1:15020/quitquitquit && exit 1)


# Quit the proxy
curl -sf -XPOST http://127.0.0.1:15020/quitquitquit