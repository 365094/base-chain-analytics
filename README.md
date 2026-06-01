# base-chain-analytics

Analyze Base chain metrics.

## Goal

This repository is a small public-safe starter project for the Base ecosystem.
It is designed to be shared publicly without exposing personal wallets, API keys, emails, Telegram tokens, VPS IPs, or private configuration.

## Category

`analytics`

## Features

- Base-oriented project structure
- Safe `.env.example`
- Real values entered locally only
- No personal wallet committed
- Beginner-friendly Python script

## Installation

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/base-chain-analytics.git
cd base-chain-analytics
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Configuration

Copy the example file locally:

```bash
cp .env.example .env
```

Then edit `.env` locally if needed.

Important: `.env` is ignored by Git and must never be committed.

## Usage

```bash
python main.py
```

## Privacy and safety

This repo intentionally uses a zero address by default:

```text
0x0000000000000000000000000000000000000000
```

Do not commit:

- personal wallets
- API keys
- private keys
- seed phrases
- Telegram tokens
- Discord webhooks
- server IPs
- logs containing private data

## License

MIT
