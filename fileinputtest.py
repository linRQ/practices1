# fileinputtest.py
import fileinput

# for line in fileinput.input(inplace=True):
#     line = line.rstrip()
#     num = fileinput.lineno()
#     print('%-40s # %2i' % (line, num))
#
# print(fileinput.isfirstline())

print(fileinput.filename)
print(fileinput.filelineno)
