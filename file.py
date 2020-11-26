with open('src/0.jpg', 'rb') as rf:
    with open('src/0_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)


# while len(file_content) > 0:
#    print(file_content,end="*")
#    file_content = f.read(size_to_read)

# f = open("src/test.txt",'r') # w w+ r+ r a(appending)
# f.close()

# f.mode f.close() f.name f.read() f.readline() f.readlines()
# for line in  f:
# print(line,end="")
# f.tell f.seek(0) f.write(content)
# with open('src/0.jpg','rb') as rf:
#    with open('src/0_copy.jpg','wb') as wf:
#        chunk_size = 4096
#        rf_chunk = rf.read(chunk_size)
#        while len(rf_chunk) > 0:
#            wf.write(rf_chunk)
#            rf_chunk = rf.read(chunk_size)
