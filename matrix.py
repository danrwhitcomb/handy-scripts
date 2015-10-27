#!/usr/local/bin/python
import math

class Matrix:
	def __init__(self, matrix):
		self.m = matrix
		self.size = (len(matrix), len(matrix[0]))
		self.small_row = 0
		self.small_col = 0

	def find_small(self):
		row_small_val = float("inf")
		row_small = []
		col_small_val = float("inf")
		col_small = []
		row_total = 0
		col_total = 0

		for i in range(self.size[0]):
			for j in range(self.size[1]):
				if self.m[i][j] != 0:
					row_total += 1

			if row_total < row_small_val:
				row_small = i
				row_small_val = row_total

			row_total = 0

		for i in range(self.size[1]):
			for j in range(self.size[0]):
				if self.m[j][i] != 0:
					col_total += 1

			if col_total < col_small_val:
				col_small = i
				col_small_val = col_total

			col_total = 0

		if row_small_val < col_small_val:
			return True, row_small + 1
		else:
			return False, col_small + 1

	def get_sub_matrix(self, i, j):
		if self.is_two_by_two():
			return None

		new_m = []
		curr_row = []

		for a in range(self.size[0]):
			if a == i-1:
				continue
			else:
				for b in range(self.size[1]):
					if b != j-1:
						curr_row.append(self.m[a][b])
			if len(curr_row) != 0:
				new_m.append(curr_row)
			curr_row = []

		return Matrix(new_m)

	def __str__(self):
		return ''.join(str(e) for e in self.m)

	def determinant(self):
		if self.is_two_by_two():
			#compute 2x2 det
			return self.m[0][0]*self.m[1][1] - self.m[1][0]*self.m[0][1]

		is_row, val = self.find_small()
		total = 0

		if is_row:
			for i in range(self.size[0]):
				if self.m[val-1][i] != 0:
					total += self.m[val-1][i] * self.cofactor(val, i + 1)
		else:
		#is column
			for i in range(self.size[1]):
				if self.m[i][val-1] != 0:
					total += self.m[i][val-1] * self.cofactor(i + 1, val)

		return total

	def cofactor(self, i, j):
		sub = self.get_sub_matrix(i, j)
		return math.pow(-1, i+j) * sub.determinant()

	def is_two_by_two(self):
		return self.size[0] == 2 and self.size[1] == 2



m = Matrix([[1,  3,  3, -4],
			[0,  1,  2, -5],
			[2,  5,  4, -3],
			[-3, -7,  -5, 2]])

print m.determinant()






