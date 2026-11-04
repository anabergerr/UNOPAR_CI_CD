#!/usr/bin/env bash
# build.sh - roda testes locais e constroi a imagem Docker.
set -e

echo "[build] Rodando testes..."
python test_app.py

echo "[build] Construindo imagem Docker..."
docker build -t unopar_ci_cd:latest .

echo "[build] Build concluido."
