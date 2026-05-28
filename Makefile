create-db:
	go run ./services/auth/cmd/migrate/ create-db

migrate-up:
	go run ./services/auth/cmd/migrate/ migrate-up

test:
	go test -v ./services/auth/testing/config_test.go
