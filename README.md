# dpm

Monorepo for the dpm app (Dance Player Manager).

## Services

| Service | Description |
|---------|-------------|
| `services/auth` | gRPC authentication service with PostgreSQL — [dpm-auth-service](https://github.com/llawn/dpm-auth-service) |

## Prerequisites

- Go 1.26+
- PostgreSQL 18+
- protobuf 34+

## Quick Start

```sh
cp .env.example .env    # configure database credentials
make create-db          # create the database
make migrate-up         # run migrations
make proto              # generate protobuf code
make test               # run tests
```

## Development

```sh
make build   # compile the binary
make run     # build and run
make clean   # remove build artifacts
```
