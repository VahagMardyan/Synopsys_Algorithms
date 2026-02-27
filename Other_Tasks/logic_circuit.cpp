#include <iostream>
#include <memory>

struct Node {
    std::shared_ptr <Node> parent;
    std::shared_ptr <Node> left;
    std::shared_ptr <Node> right;

    virtual ~Node() {};
    virtual bool get_value() const = 0;
};

struct Leaf : public Node {
    private:
        bool value;
    public:
        Leaf(bool val) : value(val) {}
        bool get_value() const override {
            return value;
        }
};

struct And_Node : public Node {
    bool get_value() const override {
        return left->get_value() && right->get_value();
    }
};

struct Or_Node : public Node {
    bool get_value() const override {
        return left->get_value() || right->get_value();
    }
};

template <typename T>
bool evaluate(const T& node) {
    return node->get_value();
};

int main() {
    auto e4 = std::make_shared<And_Node>();
    e4 -> left = std::make_shared<Leaf>(true);
    e4 -> right = std::make_shared<Leaf>(false);

    auto e2 = std::make_shared<Or_Node>();
    e2 -> left = e4;
    e2 -> right = std::make_shared<Leaf>(true);

    auto e5 = std::make_shared<Or_Node>();
    e5 -> left = std::make_shared<Leaf>(false);
    e5 -> right = std::make_shared<Leaf>(false);
    
    auto e6 = std::make_shared<Or_Node>();
    e6 -> left = std::make_shared<Leaf>(true);
    e6 -> right = std::make_shared<Leaf>(false);

    auto e3 = std::make_shared<And_Node>();
    e3 -> left = e5;
    e3 -> right = e6;

    auto e1 = std::make_shared<And_Node>();
    e1 -> left = e2;
    e1 -> right = e3;

    std::cout << "Output: " << evaluate(e1) << std::endl;

    return 0;
}