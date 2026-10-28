class Node:	
		def __init__(self,key):
			self.key = key
			self.left = None
			self.right = None
			
class BST:
	def __init__(self):
		self.root = None
		
	def insert(self,root,key):
		if root is None:
			return Node(key)
		if key < root.key:
			root.left = self.insert(rot.left, key)
		elif key > root.key:
			root.right = self.insert(root.right,key)
		else:
			print(f"duplicate entry {key} ignored.")
		return root
		
	def search(self,root,key):
		if root is None or root.key == key:
			return root
		if key < root.key:
			return self.search(root.left, key)
		return self.search(root.right, key)
		
	def minvalueNode(self,node):
		current = node
		while current.left is not None:
			current = current.left
		return current
		
	def delete(self, root, key):
		if root is None:
			return root
		if key < root.key:
			root.left = self.delete(root.left, key)
		elif key > root.key:
			root.right = self.delete(root.right, key)
		else:
			if root.left is None:
				return root.right
			elif root.right is None:
				return root.left
				
			temp = self.minvalueNode(root.right)
			root.key = temp.key
			root.right = self.delete(root.right, temp.key)
		return root
		
	def inorder(self, root):
		if root:
			self.inorder(root.left)
			print(root.key, end="")
			self.inorder(root.right)
			
	def preorder(self, root):
		if root:
			print(root.key, ends="")
			self.preorder(root.left)
			self.preorder(root.right)
			
	def postorder(self, root):
		if root:
			self.postorder(root.left)
			self.postorder(root.right)
			print(root.key, end="")
			
	def depth(self, root):
		if root is None:
			return 0
		return 1 + max(self.depth(root.left), self.depth(root.right))
		
	def mirror(self, root):
		if root:
			root.left, root.right = root.right, root.left
			self.mirror(root.left)
			self.mirror(root.right)
			
	def copy(self, root):
		if root is None:
			return None
		new_node = Node(root.key)
		new_node.left = self.copy(root.left)
		new_node.right = self.copy(root.right)
		return new_node
		
	def display_parents(self, root):
		if root:
			if root.left or root.right:
				print(f"parent {root.key}: ", end= "")
				
				if root.left:
					print(f"left child = {root.left.key}:", end= "")
				if root.right:
					print(f"right child = {root.right.key}", end= "")
				print()
		self.display_parents(root.left)
		self.display_parents(root.right)
	
	def display_leaves(self, root):
		if root:
			if root.left is None and root.right is None:
				print(root.key, end= "")
			self.display_leaves(root.left)
			self.display_leaves(root.right)
			
	def level_order(self,root):
		if root is None:
			return
		queue = [root]
		while queue:
			current = queue.pop()
			print(current.key, end="")
			if current.left:
				queue.append(current.left)
			if current.right:
				queue.append(current.right)
				
				
				
if __name__=="__main__":
	tree = BST()
	root = None
	
	while True:
		print("\n---Binary search tree menu---")
		print("1. Insert")
		print("2. Delete")
		print("3. search")
		print("4. dislay (Inorder, Preorder, postorder)")
		print("5. display Depth of Tree")
		print("6. Display mirror Image")
		print("7. create copy of tree")
		print("8. display parents with children")
		print("9. display leaf nodes")
		print("10. display level-wise")
		print("11. exit")
		
		choice = int(input("enter choice: "))
		
		if choice == 1:
			val = int(input("enter value: "))
			root = tree.insert(root, val)
			
		elif choice == 2:
			val = int(input("enter value to delete: "))
			root = tree.delete(root, val)
			
		elif choice == 3:
			val = int(input("enter value of search: "))
			res = tree.search(root, val)
			if res:
				print(f"found {val} in tree.")
			else:
				print(f"{val} not found.")
				
		elif choice == 4:
			print("Inorder: ", end=""); tree.inorder(root); print()
			print("preorder: ", end= ""); tree.preorder(root); print()
			print("postorder: ", end=""); tree.postorder(root); print()
			
		elif choice == 5:
			print("depth of tree:", tree.depth(root))
			
		elif choice == 6:
			print("mirror image created.")
			tree.inorder(root); print()
			
		elif choice == 7:
			copy_root = tree.copy(root)
			print("copied tree (inorder)", end="")
			tree.inorder(copy_root); print()
			
		elif choice == 8:
			print("parents with their children: ")
			tree.display_parents(root)
			
		elif choice == 9:
			print("leaf nodes: ", end= "")
			tree,display_leaves(root); print()
			
		elif choice == 10:
			print("level order: ", end= "")
			tree.level_order(root); print()
			
		elif choice == 11:
			print("exiting program....")
			break
			
		else:
			print("invalid choice! try again.")
			
		
		
		
