./bin:
	mkdir -p ./bin

./bin/${APP}: ./bin ./${APP}.cpp
	clang++ -o ./bin/${APP} ./${APP}.cpp

.PHONY: run
run: ./bin/${APP}
	./bin/${APP}

.PHONY: clean
clean:
	rm -rf ./bin