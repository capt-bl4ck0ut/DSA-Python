# Hàm Tìm Kiếm Node
    # def find_node(self, input_number):
    #     if input_number < self.parent_node:
    #         if self.left_child is None:
    #             return str(input_number) + "is not found"
    #         return self.left_child.find_node(input_number)
    #     elif input_number > self.parent_node:
    #         if self.left_right is None:
    #             return str(input_number) + "is not found"
    #         return self.left_right.find_node(input_number)
    #     else:
    #         return str(self.parent_node) + "is found"