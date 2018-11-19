CXX      := -c++
CXXFLAGS := -pedantic-errors -Wall -Wextra -Werror
LDFLAGS  := -L/usr/lib -lstdc++ -lm 
BUILD    := ./build
OBJ_DIR  := $(BUILD)/sobjects
APP_DIR  := $(BUILD)/apps
TARGET   := hello 
INCLUDE  := -Iinc/
SRC      := $(wildcard src/*.cpp) 
TEST_SRC := $(wildcard src/test/*.cpp) 
OBJECTS := $(SRC:%.cpp=$(OBJ_DIR)/%.o)
TEST_OBJECTS := $(TEST_SRC:%.cpp=$(OBJ_DIR)/%.o) $(filter-out $(OBJ_DIR)/src/main.o, $(OBJECTS))

$(info VAR="$(TEST_OBJECTS)")

all: build $(APP_DIR)/$(TARGET) $(APP_DIR)/unit_test

$(OBJ_DIR)/%.o: %.cpp
	@mkdir -p $(@D)
	$(CXX) $(CXXFLAGS) $(INCLUDE) -o $@ -c $<

$(APP_DIR)/$(TARGET): $(OBJECTS)
	@mkdir -p $(@D)
	$(CXX) $(CXXFLAGS) $(INCLUDE) $(LDFLAGS) -o $(APP_DIR)/$(TARGET) $(OBJECTS)

$(APP_DIR)/unit_test: $(TEST_OBJECTS)
	@mkdir -p $(@D)
	$(CXX) $(CXXFLAGS) $(INCLUDE) $(LDFLAGS) -o $(APP_DIR)/unit_test $(TEST_OBJECTS) -lboost_unit_test_framework

.PHONY: all build clean debug release

build:
	@mkdir -p $(APP_DIR)
	@mkdir -p $(OBJ_DIR)

debug: CXXFLAGS += -DDEBUG -g
debug: all

release: CXXFLAGS += -O2
release: all

clean:
	-@rm -rvf $(OBJ_DIR)/*
	-@rm -rvf $(APP_DIR)/*
