import os

os.chdir('./test-mkdir')
print(os.getcwd())
print(os.listdir())
	
for m in range(0, 101, 10):
	#print("%02d" % m, end = " ")
	#print('%03d' % m)
	os.makedirs('./testmkdir/sample/my/%03d_test_20180818' % m)

