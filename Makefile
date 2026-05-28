.PHONY: proto build run test clean

ifneq (,$(wildcard .env))
  -include .env
  export
endif

DB_URL := postgres://$(DB_USER):$(DB_PASSWORD)@$(DB_HOST):$(DB_PORT)/$(DB_NAME)
ADMIN_DB_URL := postgres://$(DB_USER):$(DB_PASSWORD)@$(DB_HOST):$(DB_PORT)/postgres

proto:
	protoc \
		--proto_path=services/auth/proto \
		--go_out=services/auth/gen/go/ \
		--go_opt=paths=source_relative \
		--go-grpc_out=services/auth/gen/go/ \
		--go-grpc_opt=paths=source_relative \
		services/auth/proto/auth.proto

build:
	go build -o bin/auth-server ./services/auth/cmd/migrate/

run: build
	./bin/auth-server

create-db:
	go run ./services/auth/cmd/migrate/ create-db

migrate-up:
	go run ./services/auth/cmd/migrate/ migrate-up

test:
	go test -v ./services/auth/testing/

clean:
	rm -rf bin/
