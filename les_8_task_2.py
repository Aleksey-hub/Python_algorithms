# Закодируйте любую строку по алгоритму Хаффмана.
from collections import Counter


class MyNode:
    def __init__(self, value, left=None, right=None, data=None):
        self.value = value
        self.left = left
        self.right = right
        self.data = data

    def __gt__(self, other):
        if self.value < other.value:
            return 1
        else:
            return 0

    def __repr__(self):
        return f'MyNode[{self.data}, {self.value}]'


def code_node(node_, path='', path_dict={}):
    if node_.data is not None:
        path_dict[node_.data] = path
        return path_dict
    else:
        temp_path_left = path + '0'
        temp_path_right = path + '1'
        return dict(list(code_node(node_.left, temp_path_left).items()) +
                    list(code_node(node_.right, temp_path_right).items()))


my_str = "прошу прощения за позднюю сдачу домашнего задания)"

a = Counter(my_str)
print(a)

list_node = list()
for key, value in sorted(a.items(), key=lambda x: x[1], reverse=True):
    list_node.append(MyNode(value, data=key))
print(list_node)

while len(list_node) != 1:
    node_buf_left = list_node.pop()
    node_buf_right = list_node.pop()
    list_node.append(MyNode(node_buf_left.value + node_buf_right.value, node_buf_left, node_buf_right))
    list_node.sort()

print('*' * 150)
root_node = list_node[0]

dict_code = code_node(root_node)
print(f'Коды символов:\n{dict_code}')
my_str_code = []
for word in my_str:
    my_str_code.append(dict_code[word])
print(f'Исходная строка:\n{my_str}')
my_str_code = ' '.join(my_str_code)
print(f'Закодированная строка:\n{my_str_code}')