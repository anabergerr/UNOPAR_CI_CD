#!/usr/bin/env bash
# deploy.sh - sobe o container localmente para validacao manual.
set -e

echo "[deploy] Removendo container anterior (se existir)..."
docker rm -f unopar_ci_cd 2>/dev/null || true

echo "[deploy] Iniciando container..."
docker run -d -p 8000:8000 --name unopar_ci_cd unopar_ci_cd:latest

echo "[deploy] App disponivel em http://localhost:8000/health"
